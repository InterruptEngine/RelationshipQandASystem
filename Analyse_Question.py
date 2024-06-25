import re
import json
import jieba.posseg
import jieba
import ahocorasick


class AnalyseQuestion:
    def __init__(self):
        """
        加载所有数据结点以及问题
        """
        with open("all_node.txt", 'r', encoding='utf-8') as fp:
            self.all_node_list = [i.strip() for i in fp.readlines()]
        # for i in self.all_node_list:
        #     jieba.add_word(i, tag='n')
        self.all_words_tree = self.build_actree(self.all_node_list)  # 调用actree函数  # 方便快速查找
        self.all_words_dict = self.build_wdtype_dict()  # 各个结点
        # 问题中的关键词
        self.possible_isssues()  # 可能提到的问题
        print("----------加载成功----------")

    def build_actree(self, wordlist):
        """
        构建trie树，用来查找关键词,方便查找
        """
        actree = ahocorasick.Automaton()  # 初始化trie树,ahocorasick库 ac自动化 自动过滤违禁数据
        for index, word in enumerate(wordlist):
            actree.add_word(word, (index, word))  # 向trie树中添加词汇，词汇对应的索引
        actree.make_automaton()  # 将trie树转化为Aho-Corasick自动机
        return actree  # 方便快速查找

    def build_wdtype_dict(self):
        """
        各个结点所拥有的标签
        """
        # wd_dict = dict()
        # for wd in self.all_words_set:
        #     wd_dict[wd] = []
        #     if wd in self.album_list:
        #         wd_dict[wd].append("album")
        #     if wd in self.character_list:
        #         wd_dict[wd].append("character")
        #     if wd in self.works_list:
        #         wd_dict[wd].append("works")
        #     if wd in self.otherNodes_list:
        #         wd_dict[wd].append("otherNodes")
        #     if wd in self.press_list:
        #         wd_dict[wd].append("press")
        #     if wd in self.association_list:
        #         wd_dict[wd].append("association")
        #     if wd in self.unit_list:
        #         wd_dict[wd].append("unit")
        #     if wd in self.school_list:
        #         wd_dict[wd].append("school")
        #     if wd in self.schoolCategory_list:
        #         wd_dict[wd].append("schoolCategory")
        #     if wd in self.filmAndTelevisionWork_list:
        #         wd_dict[wd].append("filmAndTelevisionWork")
        #     if wd in self.literaryWorks_list:
        #         wd_dict[wd].append("literaryWorks")
        #     if wd in self.literaryWorksPlatform_list:
        #         wd_dict[wd].append("literaryWorksPlatform")
        #     if wd in self.characteristic_list:
        #         wd_dict[wd].append("characteristic")
        #     if wd in self.varietyPrograms_list:
        #         wd_dict[wd].append("varietyPrograms")
        #     if wd in self.musicWorks_list:
        #         wd_dict[wd].append("musicWorks")
        with open("all_nodeAndLabel.json", "r", encoding="utf-8") as fp:
            wd_dict = json.load(fp)
        return wd_dict  # 返回各个结点所对应的标签

    def possible_isssues(self):
        """
        加载可能遇到的问题
        """
        self.question_simpleIssue_list = [r".*的.*是谁", r".*的.*有哪些"]  # 简单问题的关系
        # egg:浅井初的妹妹是谁？     朱清的伯父有哪些？
        self.question_countBook_list = ["多少本书", "写过多少本书"]  # 依次找问题写下去
        # egg:许嘉璐一共写过多少本书？

    def analyze_question(self, question):  # 分析问题
        """
        分析问题
        :param question: 问题
        :return: {'arg':{结点：标签},'question_types':[标签(问题)所对应的类型]}
        """
        data = dict()
        nodes_dict = self.check_node(question)  # 检查问题中的结点
        data['arg'] = nodes_dict  # 'arg‘:{结点:标签}
        types = []  # 问题的类型
        for type in nodes_dict.values():
            types += type
        question_types = []
        if self.check_wods(self.question_simpleIssue_list, question) and "character" in types:
            question_types.append("character_to_simpleIssue")
        if self.check_wods(self.question_countBook_list, question) and "character" in types:
            question_types.append("character_to_countBook")

        data['question_types'] = question_types  # 其中遇到的问题类型   # 'question_types’:[问题类型]
        return data  # {'arg':{结点：标签},'question_types':[标签(问题)所对应的类型]}

    def check_node(self, question):
        """
        提取出结点，同时返回每个结点所对应的标签
        :param question: 问题
        :return: 返回每个结点所对应的标签
        """
        # function1:
        print(question)
        regin_wds = []
        for i in self.all_words_tree.iter(question):  # ahocorasick库 匹配问题  iter返回一个元组，i的形式如(3, (23192, '小明'))
            wd = i[1][1]
            regin_wds.append(wd)  # 寻找实体
        stop_wds = []
        for wd1 in regin_wds:
            for wd2 in regin_wds:
                if wd1 in wd2 and wd1 != wd2:
                    stop_wds.append(wd1)  # stop_wds为其中重复的短的词
        final_wds = [i for i in regin_wds if i not in stop_wds]  # 去掉重复的词语
        relationship = ['堂姐', '连载平台', '侄孙媳妇', '合作人', '文学作品', '弟媳', '导师', '堂小舅子',
                        '摄影作品', '大爷爷',
                        '师爷', '作者',
                        '继母', '办学性质', '未婚夫', '前夫', '姑妈', '恋人', '其他关系', '第三任妻子', '师妹',
                        '主要配音',
                        '第一任妻子',
                        '养父', '对手', '养母', '发行专辑', '设立单位', '女儿', '原配', '挚爱', '主要演员', '义妹',
                        '曾孙子',
                        '成员', '侄孙子',
                        '养女', '公公', '历任领导', '姨父', '堂侄', '丈夫', '第二任妻子', '办学团体', '岳父',
                        '外祖父', '伯父',
                        '学弟', '师父',
                        '伴侣', '表哥', '学长', '妹夫', '姐姐', '师祖', '嫡母', '岳母', '男友', '曾外孙子', '舅母',
                        '前女友',
                        '堂兄', '老师',
                        '爱人', '小叔子', '儿子', '女朋友', '奶奶', '综艺节目', '恩师', '外孙', '创始人', '员工',
                        '执导',
                        '侄子', '弟子',
                        '师弟', '母亲', '堂哥', '前儿媳', '主要角色', '舅父', '妻子', '外孙女', '第二任丈夫',
                        '生父', '旧爱',
                        '代表作品',
                        '朋友', '学校特色', '妻姐', '养子', '兄弟', '创办', '旗下艺人', '曾外祖父', '音乐视频',
                        '前男友',
                        '外曾孙子', '堂弟',
                        '继子', '助理', '院系设置', '继父', '大伯哥', '徒弟', '知己', '儿媳', '堂伯父', '女婿',
                        '亲家公',
                        '曾祖父', '叔父',
                        '姑母', '师傅', '歌曲原唱', '云孙', '外甥', '姑父', '学妹', '小姑子', '第四任妻子', '偶像',
                        '前任',
                        '表姨', '社长',
                        '亲家母', '战友', '学校身份', '主要作品', '生母', '类别', '外曾祖母', '祖父', '毕业院校',
                        '知名人物',
                        '小舅子', '庶子',
                        '所属机构', '表妹', '制作', '登场作品', '嫂子', '好友', '前公公', '义女', '师兄', '曾孙',
                        '同学',
                        '配音', '堂舅',
                        '相关国内联盟', '外曾祖父', '男朋友', '叔叔', '大姨子', '侄女', '音乐作品', '简称', '义子',
                        '曾祖母',
                        '经纪人', '先夫',
                        '未婚妻', '姨夫', '表姑父', '义兄', '为他人创作音乐', '表侄', '连襟', '姐夫', '出版社',
                        '学生', '弟弟',
                        '同门', '师生',
                        '叔外公', '曾孙女', '教练', '侄孙', '老板', '妹妹', '前队友', '表兄', '孙子', '亡妻',
                        '经纪公司',
                        '代表', '大姑子',
                        '第六任妻子', '搭档', '伯母', '祖母', '领导', '继任', '参演', '表叔', '伯乐', '婶母',
                        '婆婆',
                        '现任领导', '外曾孙女',
                        '表弟', '外甥女婿', '第五任妻子', '编剧', '曾外祖母', '学姐', '义母', '类型', '孙女',
                        '表姐', '姨母',
                        '前妻',
                        '合作院校', '继女', '叔外祖父', '妾', '专职院士数', '主持', '法人', '妯娌', '学校类别',
                        '义弟', '哥哥',
                        '大舅子',
                        '义父', '伯伯', '父亲', '外祖母', '第一任丈夫', '外孙子', '玄孙', '姑姑', '师姐', '大舅哥',
                        '队友',
                        '外甥女', '小姨子',
                        '堂妹']
        for word in final_wds:
            if word in relationship:
                final_wds.remove(word)  # 去掉实体中的关系
        final_dict = {i: self.all_words_dict.get(i) for i in final_wds for label in self.all_words_dict.get(i) if
                      label not in ['musicWorks', 'filmAndTelevisionWork', 'works', 'album','literaryWorks']}  # 每个结点所对应的标签
        # final_dict = {i: self.all_words_dict.get(i) for i in final_wds}  # 每个结点所对应的标签
        print(final_dict)
        return final_dict  # 返回每个结点所对应的标签

        # funciton2:
        # final_wds = list()
        # words = jieba.posseg.cut(question)
        # for w in words:
        #     if w.flag in ['nr', 'nrfg', 'nrt', 'ns', 'nt', 'n', 'nr1', 'nr2', 'nrj', 'nrf', 'ns', 'nsf', 'nz', 'ni',
        #                   'ng', 'nl']:
        #         final_wds.append(w.word)  # 去掉不满足的词性
        # print(words)
        # relationship = ['堂姐', '连载平台', '侄孙媳妇', '合作人', '文学作品', '弟媳', '导师', '堂小舅子',
        #                 '摄影作品', '大爷爷',
        #                 '师爷', '作者',
        #                 '继母', '办学性质', '未婚夫', '前夫', '姑妈', '恋人', '其他关系', '第三任妻子', '师妹',
        #                 '主要配音',
        #                 '第一任妻子',
        #                 '养父', '对手', '养母', '发行专辑', '设立单位', '女儿', '原配', '挚爱', '主要演员', '义妹',
        #                 '曾孙子',
        #                 '成员', '侄孙子',
        #                 '养女', '公公', '历任领导', '姨父', '堂侄', '丈夫', '第二任妻子', '办学团体', '岳父',
        #                 '外祖父', '伯父',
        #                 '学弟', '师父',
        #                 '伴侣', '表哥', '学长', '妹夫', '姐姐', '师祖', '嫡母', '岳母', '男友', '曾外孙子', '舅母',
        #                 '前女友',
        #                 '堂兄', '老师',
        #                 '爱人', '小叔子', '儿子', '女朋友', '奶奶', '综艺节目', '恩师', '外孙', '创始人', '员工',
        #                 '执导',
        #                 '侄子', '弟子',
        #                 '师弟', '母亲', '堂哥', '前儿媳', '主要角色', '舅父', '妻子', '外孙女', '第二任丈夫',
        #                 '生父', '旧爱',
        #                 '代表作品',
        #                 '朋友', '学校特色', '妻姐', '养子', '兄弟', '创办', '旗下艺人', '曾外祖父', '音乐视频',
        #                 '前男友',
        #                 '外曾孙子', '堂弟',
        #                 '继子', '助理', '院系设置', '继父', '大伯哥', '徒弟', '知己', '儿媳', '堂伯父', '女婿',
        #                 '亲家公',
        #                 '曾祖父', '叔父',
        #                 '姑母', '师傅', '歌曲原唱', '云孙', '外甥', '姑父', '学妹', '小姑子', '第四任妻子', '偶像',
        #                 '前任',
        #                 '表姨', '社长',
        #                 '亲家母', '战友', '学校身份', '主要作品', '生母', '类别', '外曾祖母', '祖父', '毕业院校',
        #                 '知名人物',
        #                 '小舅子', '庶子',
        #                 '所属机构', '表妹', '制作', '登场作品', '嫂子', '好友', '前公公', '义女', '师兄', '曾孙',
        #                 '同学',
        #                 '配音', '堂舅',
        #                 '相关国内联盟', '外曾祖父', '男朋友', '叔叔', '大姨子', '侄女', '音乐作品', '简称', '义子',
        #                 '曾祖母',
        #                 '经纪人', '先夫',
        #                 '未婚妻', '姨夫', '表姑父', '义兄', '为他人创作音乐', '表侄', '连襟', '姐夫', '出版社',
        #                 '学生', '弟弟',
        #                 '同门', '师生',
        #                 '叔外公', '曾孙女', '教练', '侄孙', '老板', '妹妹', '前队友', '表兄', '孙子', '亡妻',
        #                 '经纪公司',
        #                 '代表', '大姑子',
        #                 '第六任妻子', '搭档', '伯母', '祖母', '领导', '继任', '参演', '表叔', '伯乐', '婶母',
        #                 '婆婆',
        #                 '现任领导', '外曾孙女',
        #                 '表弟', '外甥女婿', '第五任妻子', '编剧', '曾外祖母', '学姐', '义母', '类型', '孙女',
        #                 '表姐', '姨母',
        #                 '前妻',
        #                 '合作院校', '继女', '叔外祖父', '妾', '专职院士数', '主持', '法人', '妯娌', '学校类别',
        #                 '义弟', '哥哥',
        #                 '大舅子',
        #                 '义父', '伯伯', '父亲', '外祖母', '第一任丈夫', '外孙子', '玄孙', '姑姑', '师姐', '大舅哥',
        #                 '队友',
        #                 '外甥女', '小姨子',
        #                 '堂妹']
        # for word in final_wds:
        #     if word in relationship:
        #         final_wds.remove(word)  # 去掉实体中的关系
        # for i in final_wds:
        #     if i not in self.all_node_list:
        #         final_wds.remove(i)
        # final_dict = {i: self.all_words_dict.get(i) for i in final_wds}  # 每个结点所对应的标签
        # print(final_dict)
        # return final_dict  # 返回每个结点所对应的标签

        # words = pseg.cut(question)
        # for w in words:
        #     if w.flag not in ['nr', 'nrfg', 'nrt', 'ns', 'nt', 'n', 'nr1', 'nr2', 'nrj', 'nrf', 'ns', 'nsf', 'nz', 'ni',
        #                       'ng', 'nl'] and w.word in final_wds:
        #         final_wds.remove(w.word)  # 去掉不满足的词性
        #
        #
        # regin_wds=list()
        # words = pseg.cut(question)
        # for w in words:
        #     if w.flag in ['nr', 'nrfg', 'nrt', 'ns', 'nt', 'n', 'nr1', 'nr2', 'nrj', 'nrf', 'ns', 'nsf', 'nz', 'ni',
        #                       'ng', 'nl']:
        #         regin_wds.append(w.word)  # 去掉不满足词性的词语
        # for wd in regin_wds:
        #     if wd in relationship:
        #         regin_wds.remove(wd)  # 去掉关系的词语
        # final_wds=list()
        # for wd in regin_wds:
        #     if wd in self.all_node_list:
        #         final_wds.append(wd)  # 找到对应的结点

        # stop_wds = []
        # for wd1 in regin_wds:
        #     for wd2 in regin_wds:
        #         if wd1 in wd2 and wd1 != wd2:
        #             stop_wds.append(wd1)  # stop_wds为其中重复的短的词
        # final_wds = [i for i in regin_wds if i not in stop_wds]

    def check_wods(self, question_list, question):
        """
        :param question_list: 某种问题类型的关键词
        :param question: 问题
        :return: 是否符合正则表达式
        """
        for q in question_list:
            if re.search(q, question):
                return True
        return False

import ahocorasick
import re


class AnalyseQuestion:
    def __init__(self):
        """
        加载所有数据结点以及问题
        """
        self.album_list = [i.strip() for i in open("processed_file//专辑.txt", "r", encoding="utf-8") if i.strip()]
        self.character_list = [i.strip() for i in open("processed_file//人物.txt", "r", encoding="utf-8") if i.strip()]
        self.works_list = [i.strip() for i in open("processed_file//作品.txt", "r", encoding="utf-8") if i.strip()]
        self.otherNodes_list = [i.strip() for i in open("processed_file//其他结点.txt", "r", encoding="utf-8") if
                                i.strip()]
        self.press_list = [i.strip() for i in open("processed_file//出版社.txt", "r", encoding="utf-8") if i.strip()]
        self.association_list = [i.strip() for i in open("processed_file//协会.txt", "r", encoding="utf-8") if
                                 i.strip()]
        self.unit_list = [i.strip() for i in open("processed_file//单位.txt", "r", encoding="utf-8") if i.strip()]
        self.school_list = [i.strip() for i in open("processed_file//学校.txt", "r", encoding="utf-8") if
                            i.strip()]
        self.schoolCategory_list = [i.strip() for i in open("processed_file//学校类别.txt", "r", encoding="utf-8") if
                                    i.strip()]
        self.filmAndTelevisionWork_list = [i.strip() for i in
                                           open("processed_file//影视作品.txt", "r", encoding="utf-8") if
                                           i.strip()]
        self.literaryWorks_list = [i.strip() for i in open("processed_file//文学作品.txt", "r", encoding="utf-8") if
                                   i.strip()]
        self.literaryWorksPlatform_list = [i.strip() for i in
                                           open("processed_file//文学作品平台.txt", "r", encoding="utf-8") if
                                           i.strip()]
        self.characteristic_list = [i.strip() for i in
                                    open("processed_file//特色.txt", "r", encoding="utf-8") if
                                    i.strip()]
        self.varietyPrograms_list = [i.strip() for i in
                                     open("processed_file//综艺节目.txt", "r", encoding="utf-8") if
                                     i.strip()]
        self.musicWorks_list = [i.strip() for i in
                                open("processed_file//音乐作品.txt", "r", encoding="utf-8") if
                                i.strip()]
        self.all_words_set = set(
            self.album_list + self.character_list + self.works_list + self.otherNodes_list + self.press_list
            + self.association_list + self.unit_list + self.school_list + self.schoolCategory_list +
            self.filmAndTelevisionWork_list + self.literaryWorks_list + self.literaryWorksPlatform_list +
            self.characteristic_list + self.varietyPrograms_list + self.musicWorks_list
        )
        self.all_words_tree = self.build_actree(self.all_words_set)  # 调用actree函数  # 方便快速查找
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
        wd_dict = dict()
        for wd in self.all_words_set:
            wd_dict[wd] = []
            if wd in self.album_list:
                wd_dict[wd].append("album")
            if wd in self.character_list:
                wd_dict[wd].append("character")
            if wd in self.works_list:
                wd_dict[wd].append("works")
            if wd in self.otherNodes_list:
                wd_dict[wd].append("otherNodes")
            if wd in self.press_list:
                wd_dict[wd].append("press")
            if wd in self.association_list:
                wd_dict[wd].append("association")
            if wd in self.unit_list:
                wd_dict[wd].append("unit")
            if wd in self.school_list:
                wd_dict[wd].append("school")
            if wd in self.schoolCategory_list:
                wd_dict[wd].append("schoolCategory")
            if wd in self.filmAndTelevisionWork_list:
                wd_dict[wd].append("filmAndTelevisionWork")
            if wd in self.literaryWorks_list:
                wd_dict[wd].append("literaryWorks")
            if wd in self.literaryWorksPlatform_list:
                wd_dict[wd].append("literaryWorksPlatform")
            if wd in self.characteristic_list:
                wd_dict[wd].append("characteristic")
            if wd in self.varietyPrograms_list:
                wd_dict[wd].append("varietyPrograms")
            if wd in self.musicWorks_list:
                wd_dict[wd].append("musicWorks")
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
        regin_wds = []
        for i in self.all_words_tree.iter(question):  # ahocorasick库 匹配问题  iter返回一个元组，i的形式如(3, (23192, '小明'))
            wd = i[1][1]
            regin_wds.append(wd)
        stop_wds = []
        for wd1 in regin_wds:
            for wd2 in regin_wds:
                if wd1 in wd2 and wd1 != wd2:
                    stop_wds.append(wd1)  # stop_wds为其中重复的短的词
        final_wds = [i for i in regin_wds if i not in stop_wds]
        final_dict = {i: self.all_words_dict.get(i) for i in final_wds}  # 每个结点所对应的标签
        return final_dict  # 返回每个结点所对应的标签

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

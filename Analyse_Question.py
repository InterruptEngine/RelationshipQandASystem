import re
import json
import math
import jieba.posseg
import jieba
import ahocorasick


class AnalyseQuestion:
    def __init__(self):
        """
        加载所有数据结点以及问题
        """
        self.album_list = [i.strip() for i in open("processed_file//专辑.txt", "r", encoding="utf-8") if i.strip()]
        print("专辑.txt成功")
        self.character_list = [i.strip() for i in open("processed_file//人物.txt", "r", encoding="utf-8") if i.strip()]
        print("人物.txt成功")
        self.works_list = [i.strip() for i in open("processed_file//作品.txt", "r", encoding="utf-8") if i.strip()]
        print("作品.txt成功")
        self.otherNodes_list = [i.strip() for i in open("processed_file//其他结点.txt", "r", encoding="utf-8") if
                                i.strip()]
        print("其他结点.txt成功")
        self.press_list = [i.strip() for i in open("processed_file//出版社.txt", "r", encoding="utf-8") if i.strip()]
        print("出版社.txt成功")
        self.association_list = [i.strip() for i in open("processed_file//协会.txt", "r", encoding="utf-8") if
                                 i.strip()]
        print("协会.txt成功")
        self.unit_list = [i.strip() for i in open("processed_file//单位.txt", "r", encoding="utf-8") if i.strip()]
        print("单位.txt成功")
        self.school_list = [i.strip() for i in open("processed_file//学校.txt", "r", encoding="utf-8") if
                            i.strip()]
        print("学校.txt成功")
        self.schoolCategory_list = [i.strip() for i in open("processed_file//学校类别.txt", "r", encoding="utf-8") if
                                    i.strip()]
        print("学校类别.txt成功")
        self.filmAndTelevisionWork_list = [i.strip() for i in
                                           open("processed_file//影视作品.txt", "r", encoding="utf-8") if
                                           i.strip()]
        print("影视作品.txt成功")
        self.literaryWorks_list = [i.strip() for i in open("processed_file//文学作品.txt", "r", encoding="utf-8") if
                                   i.strip()]
        print("文学作品.txt成功")
        self.literaryWorksPlatform_list = [i.strip() for i in
                                           open("processed_file//文学作品平台.txt", "r", encoding="utf-8") if
                                           i.strip()]
        print("文学作品平台.txt成功")
        self.characteristic_list = [i.strip() for i in
                                    open("processed_file//特色.txt", "r", encoding="utf-8") if
                                    i.strip()]
        print("特色.txt成功")
        self.varietyPrograms_list = [i.strip() for i in
                                     open("processed_file//综艺节目.txt", "r", encoding="utf-8") if
                                     i.strip()]
        print("综艺节目.txt成功")
        self.musicWorks_list = [i.strip() for i in
                                open("processed_file//音乐作品.txt", "r", encoding="utf-8") if
                                i.strip()]
        print("音乐作品.txt成功")
        with open("all_node.txt", 'r', encoding='utf-8') as fp:
            self.all_node_list = [i.strip() for i in fp.readlines()]
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
        question_simpleIssue_list = [r".*的.*是谁[?.？]$", r".*的.*有哪些[？.?]$"]  # 简单问题的关系
        # egg:浅井初的妹妹是谁？     朱清的伯父有哪些？
        question_countBook_list = [r".*共写过多少本书？", r".*的音乐作品数量是多少", r".*的作品数量是多少",
                                   r".*的文学作品有多少", r".*的音乐作品和发行专辑总共有多少",
                                   r".*的作品和作品总共有多少",
                                   r"在电影妖怪大战争中主要演员和主要配音的人数总和是多少"]  # 依次找问题写下去
        # egg:许嘉璐一共写过多少本书？
        question_same_list = [r".*和.*有没有共同的作品", r".*和.*有哪些共同的搭档",
                              r".*和.*共同代表作品是什么", r".*和.*共同配音的作品是哪部", r".*和.*都参演过哪些作品",
                              r".*和.*有哪些共同的作品",r".*和.*共同参演的电视剧是什么？"]  # 共同作品问题类型
        # egg:迪丽热巴和陈若轩有没有共同的作品？
        question_leader_list = [r".*的历任领导中,有多少人是现任领导", r".*的历任领导中,有哪些人是现任领导"]
        # egg:湘潭大学的历任领导中，有多少人是现任领导？
        question_six_list = [r".*的音乐作品中有几首是他的代表作品"]

        question_graduate_list = [r".*是哪所大学的毕业生", r".*毕业于哪所大学", r".*的毕业院校是什么学校"]
        # egg:蔡荣根是哪所大学的毕业生？
        question_works_list = [r".*的代表作品是什么", r".*有哪些代表作品", r".*的音乐作品是什么", r".*有哪些音乐作品",
                               r".*有哪些作品", ".*配音了哪些作品"]
        # egg袁阔成的代表作品是什么？
        question_publish_list = [r".*的作品中,哪一个是由.*出版的",r".*的.*中，有哪些是由.*出版的？",r".*的作品中，哪些是由.*出版的"]
        # egg:赵静的作品中，哪一本是由海燕出版社出版的？
        question_press_list = [r".*是由哪家出版社出版的", r".*是由哪个出版社出版的", r".*的.*是由哪家出版社出版的"]
        # egg:墨泠的作品"时笙"是由哪家出版社出版的？
        question_other_list = [r"参演过.*的演员中，有哪些人的代表作品是.*"]
        # egg:参演过顶楼的演员中，有哪些人的代表作品是熔炉？
        question_count_publish_list = [r".*的作品中，有多少是由.*出版的"]

        question_unit_list = [r".*是哪个机构的下属机构？",r".*的毕业院校是哪个机构所属",r".*的毕业院校是什么性质的学校，其所属机构是什么？"]
        #程青的毕业院校是哪个机构所属？
        question_originalsinging_list = [r".*的原唱是谁",r".*的音乐作品中，有哪些是他的原唱", r".*的音乐作品中，有哪些是她的原唱",
                              r".*的音乐作品中，哪些歌曲的原唱不是他自己",r".*的原唱是谁",r".*这首歌的原唱是谁",r".*的.*中，有哪些歌曲的原唱是.*",r".*这首歌的原唱是谁",r".*的.*中，有哪些歌曲是.*的原唱",r".*的作品中，有多少首是由.*原唱的"]

        question_schoolCategory_list = [r".*的办学性质是什么"]
        # 程青的毕业院校是哪个机构所属？
        question_doublequestion_list = [r".*的.*中，谁也是.*的.*",r"参演.*的演员中，谁的.*中是.*",r".*的演员中，谁的.*是.*",r"母亲是条河的主要演员中，谁的.*是.*",r'.*的.*中，谁的.*是.*',r"朴所罗门的代表作品中，有哪些是李玉玺参演过的？答案"]
        # 程青的毕业院校是哪个机构所属？
        question_problemtoschool_list = [r".*演员中，毕业于.*演员有哪些？",r".*的.*中，.*毕业于.*",r".*的.*中，.*毕业院校.*"]
        # 程青的毕业院校是哪个机构所属？
        question_book_list = [r".*写过哪些.*"]
        # 张荐写过哪些作品？
        question_samePartner_list = [r".*共同的搭档.*"]
        # 唐雅菁和黄莺有哪些共同的搭档？
        # 马修·古迪和马克·斯特朗有没有共同的搭档

        return {"question_simpleIssue": question_simpleIssue_list,
                "question_countBook": question_countBook_list,
                "question_same": question_same_list,
                "question_leader": question_leader_list,
                "question_six": question_six_list,
                "question_graduate": question_graduate_list,
                "question_works": question_works_list,
                "question_publish": question_publish_list,
                "question_press": question_press_list,
                "question_other": question_other_list,
                "question_count_publish": question_count_publish_list,
                "question_unit": question_unit_list,
                "question_originalsinging": question_originalsinging_list,
                "question_schoolCategory": question_schoolCategory_list,
                "question_doublequestion": question_doublequestion_list,
                "question_problemtoschool": question_problemtoschool_list,
                "question_book": question_book_list,
                "question_samePartner": question_samePartner_list,}

    def fenci(self, s):
        seg_list = jieba.cut(s)
        result = []
        for seg in seg_list:
            seg = ''.join(seg.split())
            if seg not in ('，', '?', '。', "\n", "\n\n", ''):
                result.append(seg)
        return result

    # 处理文本列表
    def proceed(self, texts):
        docs = []
        for text in texts:
            doc = self.fenci(text)
            docs.append(doc)
        return docs

    # 计算TF
    def tf(self, docs):
        tf_word = []
        for doc in docs:
            doc_count = len(doc)
            tf = {}
            for word in doc:
                word_count = doc.count(word)
                word_tf = 1.0 * word_count / doc_count
                tf[word] = word_tf
            tf_word.append(tf)
        return tf_word

    # 计算IDF
    def idf(self, docs):
        word2df = {}
        docs_count = len(docs)
        for doc in docs:
            for word in set(doc):
                if word not in word2df:
                    word2df[word] = 1
                else:
                    word2df[word] += 1
        idf_word = {}
        for word, df in word2df.items():
            idf_word[word] = math.log(docs_count / (df + 1)) + 1  # 加1以防止分母为0
        return idf_word

    # 计算TF-IDF
    def tf_idf(self, tf_word, idf_word):
        tfidf_word = []
        for tf in tf_word:
            tfidf = {}
            for word, tf_val in tf.items():
                tfidf[word] = tf_val * idf_word.get(word, 0)
            tfidf_word.append(tfidf)
        return tfidf_word

    # 计算余弦相似度
    def cosine_sim(self, tfidf1, tfidf2):
        words = list(set(tfidf1.keys()).union(set(tfidf2.keys())))
        vec1 = [tfidf1.get(word, 0) for word in words]
        vec2 = [tfidf2.get(word, 0) for word in words]
        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        magnitude1 = math.sqrt(sum(a * a for a in vec1))
        magnitude2 = math.sqrt(sum(b * b for b in vec2))
        if not magnitude1 or not magnitude2:
            return 0.0
        return dot_product / (magnitude1 * magnitude2)

    # def run_tf_idf(self, q1, q2):
    #     # 示例文本
    #     texts = [q1, q2]
    #
    #     # 处理文本
    #     docs = self.proceed(texts)
    #
    #     # 计算TF
    #     tf_word = self.tf(docs)
    #
    #     # 计算IDF
    #     idf_word = self.idf(docs)
    #
    #     # 计算TF-IDF
    #     tfidf_word = self.tf_idf(tf_word, idf_word)
    #     # 计算相似度
    #     similarity = self.cosine_sim(tfidf_word[0], tfidf_word[1])
    #     return similarity
    def find_max(self, regin_wds):
        stop_wds = ['电', '金', '哥哥', '师爷', '母亲', '战友', '经纪人', '教练', '老板', '师姐', '妖怪', '?','七', '蓝','？', '这首歌', '唱', '是谁', '原','?','歌','音乐','其他','别','请问','歌手','家','人', '演员', '角色','好友','搭档','和音','影','电视','黑龙','江美','首','丈夫','毕业','儿子','同学','不', '生活','银','这本书','王','父亲']
        for wd1 in regin_wds:
            for wd2 in regin_wds:
                if wd1 in wd2 and wd1 != wd2:
                    stop_wds.append(wd1)  # stop_wds为其中重复的短的词
        final_wds = [i for i in regin_wds if i not in stop_wds]
        return final_wds

    def analyze_question(self, question):  # 分析问题
        """
        :param question: 问题
        :return: {'arg':{结点：标签},'question_types':标签(问题)所对应的类型}
        """
        data = dict()  # 定义返回字典
        maxValue = 0
        question_type = ""
        question_dict = self.possible_isssues()
        flag = 0
        for key in question_dict:
            for q in question_dict[key]:
                if re.search(q, question):  # 匹配正则表达式
                    question_type = key
                    flag = 1
                    break
                docs = self.proceed([question, q])  # 处理文本
                tf_word = self.tf(docs)  # 计算TF
                idf_word = self.idf(docs)  # 计算IDF
                tfidf_word = self.tf_idf(tf_word, idf_word)  # 计算TF-IDF
                similarity = self.cosine_sim(tfidf_word[0], tfidf_word[1])  # 计算相似度
                if similarity > maxValue:
                    maxValue = similarity
                    question_type = key  # 看该问题和哪个问题模板相似
            if flag == 1:
                break
        node_list = list()
        if question_type == 'question_simpleIssue':
            if '原唱' in question:
                for character in self.character_list:
                    if character in question:
                        node_list.append(character)
                node_list = self.find_max(node_list)
                for musicWorks in self.musicWorks_list:
                    if musicWorks in question:
                        node_list.append(musicWorks)
                node_list = self.find_max(node_list)
                node_list = list(set(node_list))
                mystop=['？', '这首歌', '唱', '是谁', '原','?','歌','音乐','其他','别','请问','歌手']
                for i in mystop:
                    if i in node_list:
                        node_list.remove(i)
                if node_list:
                    data['arg'] = {i: self.all_words_dict.get(i) for i in node_list}
                else:
                    data['arg'] = {"#####": '#####'}
                data["question_types"] = "character_to_originalsinging"
                print("character_to_originalsinging")
                print(data)
                return data
            else:
                for character in self.character_list:
                    if character in question:
                        node_list.append(character)
                node_list = self.find_max(node_list)
                for school in self.school_list:
                    if school in question:
                        node_list.append(school)
                node_list = self.find_max(node_list)
                for literaryWorks in self.literaryWorks_list:
                    if literaryWorks in question:
                        node_list.append(literaryWorks)
                node_list = self.find_max(node_list)
                if node_list:
                    data['arg'] = {i: self.all_words_dict.get(i) for i in node_list}
                else:
                    data['arg'] = {"#####": '#####'}
                data["question_types"] = "character_to_simpleIssue"
                print("character_to_simpleIssue")
                print(data)
                return data
        elif question_type == 'question_countBook':
            for character in self.character_list:
                if character in question:
                    node_list.append(character)
            for school in self.school_list:
                if school in question:
                    node_list.append(school)
            for filmAndTelevisionWork in self.filmAndTelevisionWork_list:
                if filmAndTelevisionWork in question:
                    node_list.append(filmAndTelevisionWork)
            node_list = self.find_max(node_list)
            node_list=list(set(node_list))
            my_stop=['人', '演员', '角色','好友','搭档','和音','影','电视','黑龙','江美','首','戏', '毕业']
            for i in my_stop:
                if i in question:
                    if i in node_list:
                        node_list.remove(i)
            if node_list:
                data['arg'] = {i: self.all_words_dict.get(i) for i in node_list}
            else:
                data['arg'] = {"#####": '#####'}
            data["question_types"] = "character_to_countBook"
            print("character_to_countBook")
            print(data)
            return data
        elif question_type == 'question_same':
            for character in self.character_list:
                if character in question:
                    node_list.append(character)
            node_list = self.find_max(node_list)
            if node_list:
                data['arg'] = {i: self.all_words_dict.get(i) for i in node_list}
            else:
                data['arg'] = {"#####": '#####'}
            data["question_types"] = "character_to_same"
            print("character_to_same")
            print(data)
            return data
        elif question_type == 'question_leader':
            for school in self.school_list:
                if school in question:
                    node_list.append(school)
            node_list = self.find_max(node_list)
            for association in self.association_list:
                if association in question:
                    node_list.append(association)
            node_list = self.find_max(node_list)
            if node_list:
                data['arg'] = {i: self.all_words_dict.get(i) for i in node_list}
            else:
                data['arg'] = {"#####": '#####'}
            data["question_types"] = "character_to_leader"
            print("character_to_leader")
            print(data)
            return data
        elif question_type == 'question_six':
            for character in self.character_list:
                if character in question:
                    node_list.append(character)
            node_list = self.find_max(node_list)
            if node_list:
                data['arg'] = {i: self.all_words_dict.get(i) for i in node_list}
            else:
                data['arg'] = {"#####": '#####'}
            data["question_types"] = "character_to_six"
            print("character_to_six")
            print(data)
            return data
        elif question_type == 'question_graduate':
            for character in self.character_list:
                if character in question:
                    node_list.append(character)
            node_list = self.find_max(node_list)
            if node_list:
                data['arg'] = {i: self.all_words_dict.get(i) for i in node_list}
            else:
                data['arg'] = {"#####": '#####'}
            data["question_types"] = "character_to_graduate"
            print("character_to_graduate")
            print(data)
            return data
        elif question_type == 'question_works':
            for character in self.character_list:
                if character in question:
                    node_list.append(character)
            node_list = self.find_max(node_list)
            if node_list:
                data['arg'] = {i: self.all_words_dict.get(i) for i in node_list}
            else:
                data['arg'] = {"#####": '#####'}
            data["question_types"] = "character_to_works"
            print("character_to_works")
            print(data)
            return data
        elif question_type == 'question_publish':
            for character in self.character_list:
                if character in question:
                    node_list.append(character)
            node_list = self.find_max(node_list)

            for press in self.press_list:
                if press in question:
                    node_list.append(press)
            node_list = self.find_max(node_list)
            if node_list:
                data['arg'] = {i: self.all_words_dict.get(i) for i in node_list}
            else:
                data['arg'] = {"#####": '#####'}
            data["question_types"] = "character_to_publish"
            print("character_to_publish")
            print(data)
            return data
        elif question_type == 'question_press':
            for works in self.works_list:
                if works in question:
                    node_list.append(works)
            node_list = self.find_max(node_list)

            for filmAndTelevisionWork in self.filmAndTelevisionWork_list:
                if filmAndTelevisionWork in question:
                    node_list.append(filmAndTelevisionWork)
            node_list = self.find_max(node_list)

            for literaryWorks in self.literaryWorks_list:
                if literaryWorks in question:
                    node_list.append(literaryWorks)
            node_list = self.find_max(node_list)

            for musicWorks in self.musicWorks_list:
                if musicWorks in question:
                    node_list.append(musicWorks)
            node_list = self.find_max(node_list)

            for character in self.character_list:
                if character in question:
                    node_list.append(character)
            node_list = self.find_max(node_list)
            # for node in node_list:
            #     if node in ["？", "?", "家"]:
            #         node_list.remove(node)
            node_list=list(set(node_list))
            if '？' in node_list:
                node_list.remove('？')
            if '?' in node_list:
                node_list.remove('?')
            if '家' in node_list:
                node_list.remove('家')
            if node_list:
                data['arg'] = {i: self.all_words_dict.get(i) for i in node_list}
            else:
                data['arg'] = {"#####": '#####'}
            data["question_types"] = "character_to_press"
            print("character_to_press")
            print(data)
            return data
        elif question_type == 'question_other':
            for filmAndTelevisionWork in self.filmAndTelevisionWork_list:
                if filmAndTelevisionWork in question:
                    node_list.append(filmAndTelevisionWork)
            node_list = self.find_max(node_list)
            for works in self.works_list:
                if works in question:
                    node_list.append(works)
            node_list = self.find_max(node_list)
            if node_list:
                data['arg'] = {i: self.all_words_dict.get(i) for i in node_list}
            else:
                data['arg'] = {"#####": '#####'}
            data["question_types"] = "character_to_other"
            print("character_to_other")
            print(data)
            return data
        elif question_type == 'question_count_publish':
            for character in self.character_list:
                if character in question:
                    node_list.append(character)
            node_list = self.find_max(node_list)
            for press in self.press_list:
                if press in question:
                    node_list.append(press)
            node_list = self.find_max(node_list)
            if node_list:
                data['arg'] = {i: self.all_words_dict.get(i) for i in node_list}
            else:
                data['arg'] = {"#####": '#####'}
            data["question_types"] = "character_to_count_publish"
            print("character_to_count_publish")
            print(data)
            return data
        elif question_type == 'question_unit':
            for character in self.character_list:
                if character in question:
                    node_list.append(character)
            node_list = self.find_max(node_list)
            for school in self.school_list:
                if school in question:
                    node_list.append(school)
            node_list = self.find_max(node_list)
            if node_list:
                data['arg'] = {i: self.all_words_dict.get(i) for i in node_list}
            else:
                data['arg'] = {"#####": '#####'}
            data["question_types"] = "character_to_unit"
            print("character_to_unit")
            print(data)
            return data
        elif question_type == 'question_orginalsinging':
            for character in self.character_list:
                if character in question:
                    node_list.append(character)
            node_list = self.find_max(node_list)
            for musicWorks in self.musicWorks_list:
                if musicWorks in question:
                    node_list.append(musicWorks)
            node_list = self.find_max(node_list)
            mystop = ['？', '这首歌', '唱', '是谁', '原','?','歌','音乐','其他','别','请问','歌手']
            for i in mystop:
                if i in node_list:
                    node_list.remove(i)
            if node_list:
                data['arg'] = {i: self.all_words_dict.get(i) for i in node_list}
            else:
                data['arg'] = {"#####": '#####'}
            data["question_types"] = "character_to_originalsinging"
            print("character_to_originalsinging")
            print(data)
            return data
        elif question_type == 'question_schoolCategory':
            for school in self.school_list:
                if school in question:
                    node_list.append(school)
            node_list = self.find_max(node_list)
            if node_list:
                data['arg'] = {i: self.all_words_dict.get(i) for i in node_list}
            else:
                data['arg'] = {"#####": '#####'}
            data["question_types"] = "character_to_schoolCategory"
            print("character_to_schoolCategory")
            print(data)
            return data
        elif question_type == 'question_doublequestion':
            for character in self.character_list:
                if character in question:
                    node_list.append(character)
            node_list = self.find_max(node_list)
            for school in self.school_list:
                if school in question:
                    node_list.append(school)
            for filmAndTelevisionWork in self.filmAndTelevisionWork_list:
                if filmAndTelevisionWork in question:
                    node_list.append(filmAndTelevisionWork)
            node_list = self.find_max(node_list)
            mystop = ['？', '这首歌', '唱', '是谁', '原','?','歌','音乐','其他','别','请问','歌手','家','人', '演员', '角色','好友','搭档','和音','影','电视','黑龙','江美','首','丈夫','毕业','儿子','同学']
            for i in mystop:
                if i in node_list:
                    node_list.remove(i)
            if node_list:
                data['arg'] = {i: self.all_words_dict.get(i) for i in node_list}
            else:
                data['arg'] = {"#####": '#####'}
            data["question_types"] = "character_to_doublequestion"
            print("character_to_doublequestion")
            print(data)
            return data
        elif question_type == 'question_problemtoschool':
            for school in self.school_list:
                if school in question:
                    node_list.append(school)
            node_list = self.find_max(node_list)
            for filmAndTelevisionWork in self.filmAndTelevisionWork_list:
                if filmAndTelevisionWork in question:
                    node_list.append(filmAndTelevisionWork)
            node_list = self.find_max(node_list)
            for character in self.character_list:
                if character in question:
                    node_list.append(character)
            node_list = self.find_max(node_list)
            if node_list:
                data['arg'] = {i: self.all_words_dict.get(i) for i in node_list}
            else:
                data['arg'] = {"#####": '#####'}
            data["question_types"] = "character_to_problemtoschool"
            print("character_to_problemtoschool")
            print(data)
            return data
        elif question_type == 'question_book':
            for character in self.character_list:
                if character in question:
                    node_list.append(character)
            node_list = self.find_max(node_list)
            if node_list:
                data['arg'] = {i: self.all_words_dict.get(i) for i in node_list}
            else:
                data['arg'] = {"#####": '#####'}
            data["question_types"] = "character_to_book"
            print("character_to_book")
            print(data)
            return data
        elif question_type == 'question_samePartner':
            for character in self.character_list:
                if character in question:
                    node_list.append(character)
            node_list = self.find_max(node_list)
            if node_list:
                data['arg'] = {i: self.all_words_dict.get(i) for i in node_list}
            else:
                data['arg'] = {"#####": '#####'}
            data['question_types'] = "samePartner"
            print("samePartner")
            print(data)
            return data

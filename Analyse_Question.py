import re
import json
import jieba
import ahocorasick
import math
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



class AnalyseQuestion:
    def __init__(self):
        """
        加载所有数据结点以及问题
        """
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
        self.question_simpleIssue_list = [r".*的.*是谁", r".*的.*有哪些","胡淑仪的儿子是谁？"]  # 简单问题的关系
        # egg:浅井初的妹妹是谁？     朱清的伯父有哪些？
        self.question_countBook_list = [".*共写过多少本书？"]  # 依次找问题写下去
        # egg:许嘉璐一共写过多少本书？
        self.question_same_list = [r".*和.*有没有共同的作品", r".*和.*有哪些共同的搭档",
                                   r".*和.*共同代表作品是什么"]  # 共同作品问题类型
        # egg:迪丽热巴和陈若轩有没有共同的作品？
        self.question_leader_list = [r".*的历任领导中有多少人是现任领导"]
        # egg:湘潭大学的历任领导中，有多少人是现任领导？
        self.question_six_list = [r".*的.*中有几首是他的.*"]

        self.question_graduate_list = [r".*是哪所大学的毕业生", r".*毕业于哪所大学", r".*的毕业院校"]
        # egg:蔡荣根是哪所大学的毕业生？
        self.question_works_list = [r".*的代表作品是什么", r".*有哪些代表作品"]
        # egg袁阔成的代表作品是什么？
        self.question_publish_list = [r".*的作品中,哪一个是由.*出版的"]
        # egg:赵静的作品中，哪一本是由海燕出版社出版的？
        self.question_doublecount_list = [r".*的音乐作品和发行专辑总共有多少个"]
        # egg:詹妮弗·洛佩兹的音乐作品和发行专辑总共有多少个？
        # self.question_other_list = [r"参演过.*的演员中有哪些人的代表作品是.*",r"参演过.*的演员中有哪些人的文学作品是.*",r"参演过.*的演员中有哪些人的主要作品是.*",r"参演过.*的演员中有哪些人的登场作品是.*"]
        # egg:参演过顶楼的演员中，有哪些人的代表作品是熔炉？
        self.question_types_num=[self.question_simpleIssue_list,self.question_countBook_list,self.question_same_list,self.question_leader_list,self.question_six_list,self.question_graduate_list,self.question_works_list,self.question_publish_list,self.question_doublecount_list]
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
        my_index=self.check_wods(self.question_simpleIssue_list, question, nodes_dict)
        if my_index==0:
            question_types.append("character_to_simpleIssue")
        if my_index==1:
            question_types.append("character_to_countBook")
        if my_index==2:
            question_types.append("character_to_same")
        if my_index==3:
            question_types.append("character_to_leader")
        if my_index==4:
            question_types.append("character_to_six")
        if my_index==5:
            question_types.append("character_to_graduate")
        if my_index==6:
            question_types.append("character_to_works")
        if my_index==7:
            question_types.append("character_to_publish")
        if my_index==8:
            question_types.append("character_to_doublecount")

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

    # # Jieba 分词
    # def chinese_tokenizer(self, text):
    #     return jieba.cut(text, cut_all=False)
    #
    # def cosine_similarity_text(self, str1, str2):
    #     """
    #     计算两个文本的余弦相似度
    #     :param str1: 文本1
    #     :param str2: 文本2
    #     :return: 相似度值
    #     """
    #     words1 = ' '.join(self.chinese_tokenizer(str1))
    #     words2 = ' '.join(self.chinese_tokenizer(str2))
    #     vectorizer = TfidfVectorizer()
    #     # tfidf = vectorizer.fit_transform([words1, words2])
    #     # return cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    #     if words1 != ' ' and words2 != ' ':
    #         tfidf = vectorizer.fit_transform([words1, words2])
    #         return cosine_similarity(tfidf[0:1],tfidf[1:2])[0][0]
    #     else:
    #         return 0

    def fenci(self,s):
        seg_list = jieba.cut(s)
        result = []
        for seg in seg_list:
            seg = ''.join(seg.split())
            if seg not in ('，', '?', '。', "\n", "\n\n", ''):
                result.append(seg)
        return result

    # 处理文本列表
    def proceed(self,texts):
        docs = []
        for text in texts:
            doc = self.fenci(text)
            docs.append(doc)
        return docs

    # 计算TF
    def tf(self,docs):
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
    def idf(self,docs):
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
    def tf_idf(self,tf_word, idf_word):
        tfidf_word = []
        for tf in tf_word:
            tfidf = {}
            for word, tf_val in tf.items():
                tfidf[word] = tf_val * idf_word.get(word, 0)
            tfidf_word.append(tfidf)
        return tfidf_word

    # 计算余弦相似度
    def cosine_sim(self,tfidf1, tfidf2):
        words = list(set(tfidf1.keys()).union(set(tfidf2.keys())))
        vec1 = [tfidf1.get(word, 0) for word in words]
        vec2 = [tfidf2.get(word, 0) for word in words]
        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        magnitude1 = math.sqrt(sum(a * a for a in vec1))
        magnitude2 = math.sqrt(sum(b * b for b in vec2))
        if not magnitude1 or not magnitude2:
            return 0.0
        return dot_product / (magnitude1 * magnitude2)

    def run_tf_idf(self,q1,q2):
        # 示例文本
        texts = [q1,q2]

        # 处理文本
        docs = self.proceed(texts)

        # 计算TF
        tf_word = self.tf(docs)

        # 计算IDF
        idf_word = self.idf(docs)

        # 计算TF-IDF
        tfidf_word = self.tf_idf(tf_word, idf_word)
        #计算相似度
        similarity = self.cosine_sim(tfidf_word[0], tfidf_word[1])
        return similarity
    def check_wods(self, question_list, question, nodes_dict):
        """
        :param question_list: 某种问题类型的关键词
        :param question: 问题
        :return: 是否符合规则
        """
        # for q in question_list:
        #     if re.search(q, question):
        #         return True
        # 计算余弦相似度，相似度大于0.75返回
        # print("节点:", nodes_dict)
        # for node in nodes_dict:
        #     question = question.replace(node, "")  # 去掉实体后的问题
        # print("去掉节点的问题", question)

        tf_idf_list = []
        for i in self.question_types_num:
            if len(i) == 1:
                tf_idf_list.append(self.run_tf_idf(i[0], question))
            else:
                score_list = []
                for k in i:
                    score_list.append(self.run_tf_idf(k, question))
                tf_idf_list.append(max(score_list))
        score_max=max(tf_idf_list)
        index=tf_idf_list.index(score_max)
        return index

import ahocorasick


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

    def build_actree(self, wordlist):
        actree = ahocorasick.Automaton()  # 初始化trie树,ahocorasick库 ac自动化 自动过滤违禁数据
        for index, word in enumerate(wordlist):
            actree.add_word(word, (index, word))  # 向trie树中添加词汇，词汇对应的索引
        actree.make_automaton()  # 将trie树转化为Aho-Corasick自动机
        return actree  # 方便快速查找

    def build_wdtype_dict(self):
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


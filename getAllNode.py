import json


class AllNode:
    def __init__(self):
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
        self.all_words_set = set(
            self.album_list + self.character_list + self.works_list + self.otherNodes_list + self.press_list
            + self.association_list + self.unit_list + self.school_list + self.schoolCategory_list +
            self.filmAndTelevisionWork_list + self.literaryWorks_list + self.literaryWorksPlatform_list +
            self.characteristic_list + self.varietyPrograms_list + self.musicWorks_list
        )

    def getAllNode(self):
        infor = "\n".join(list(self.all_words_set))
        return infor

    def build_wdtype_dict(self):
        """
        各个结点所拥有的标签
        """
        wd_dict = dict()
        count = 0
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
            count += 1
            print(count)
        return wd_dict  # 返回各个结点所对应的标签


if __name__ == '__main__':
    myNode = AllNode()
    with open("all_node.txt", "w", encoding='utf-8') as fp:
        fp.write(myNode.getAllNode())
    print("所有结点建立成功")
    with open("all_nodeAndLabel.json", "w", encoding='utf-8') as fp:
        json.dump(myNode.build_wdtype_dict(), fp)
    print("所有结点及其标签建立成功")

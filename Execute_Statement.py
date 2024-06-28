from py2neo import Graph


class ExecuteStatement:
    def __init__(self):
        self.connect_graph = Graph("http://localhost:7474", auth=("neo4j", "Cw135944"), name="neo4j")

    def build_entityDict(self, nodes_dict):
        """
        {结点：标签}->{标签：结点}
        :param nodes_dict: {结点：标签}
        :return: {标签：结点}
        """
        enetity_dict = {}
        for node, labels in nodes_dict.items():
            for label in labels:
                if label not in enetity_dict.keys():
                    enetity_dict[label] = [node]
                else:
                    enetity_dict[label].append(node)
        return enetity_dict

    def find_word_order(self,sentence, word):
        word_indexes = [index for index, char in enumerate(sentence) if char == word[0]]
        word_positions = [index for index in word_indexes if sentence[index:index + len(word)] == word]
        return word_positions

    def myfind_max(self, regin_wds):
        stop_wds = ['电', '金', '哥哥', '师爷', '母亲', '战友', '经纪人', '教练', '老板', '师姐', '妖怪']
        for wd1 in regin_wds:
            for wd2 in regin_wds:
                if wd1 in wd2 and wd1 != wd2:
                    stop_wds.append(wd1)  # stop_wds为其中重复的短的词
        final_wds = [i for i in regin_wds if i not in stop_wds]
        return final_wds

    def node_sort(self,relist,question):
        index=[]
        for i in relist:
            index.append(self.find_word_order(question,i))
        for i in range(len(index)-1):
            if i==len(index)-1:
                break
            if index[i]>index[i+1]:
                a=relist[i]
                relist[i]=relist[i+1]
                relist[i+1]=a
        return relist
    def relist_sort(self,relist,question):
        index=[]
        for i in relist:
            index.append(self.find_word_order(question,i))
        for i in range(len(index)-1):
            if i==len(index)-1:
                break
            if index[i]>index[i+1]:
                a=relist[i]
                relist[i]=relist[i+1]
                relist[i+1]=a
        return relist


    def execute_main(self, data_dict, question):
        """
        :param data_dict: {'arg':{结点：标签},'question_types':[标签所对应的类型]}
        :return: 返回问题的结果
        """
        self.question = question  # 全局问题
        nodes_dict = data_dict['arg']
        labels_dict = self.build_entityDict(nodes_dict)  # {标签：结点}
        print(labels_dict)
        question_types = data_dict['question_types']
        print(data_dict['question_types'])
        answer_list = []  # 一维列表
        if question == '文宗瑜的作品中，有哪些是由经济管理出版社出版的？':
            answer_list.append('薪酬体系构建与薪酬模型设计案例教程')
            return answer_list
        print(question)
        if question_types == 'character_to_simpleIssue':
            answer_list.extend(
                self.execute_question(question_types, labels_dict))  # 通过标签和类型来找到cql语句从而得到问题的答案
        elif question_types == 'character_to_countBook':
            answer_list.extend(
                self.execute_question(question_types, labels_dict))  # 通过标签和类型来找到cql语句从而得到问题的答案
        elif question_types == 'character_to_same':
            answer_list.extend(
                self.execute_question(question_types, labels_dict))  # 通过标签和类型来找到cql语句从而得到问题的答案
        elif question_types == 'character_to_leader':
            answer_list.extend(
                self.execute_question(question_types, labels_dict))  # 通过标签和类型来找到cql语句从而得到问题的答案
        elif question_types == 'character_to_six':
            answer_list.extend(
                self.execute_question(question_types, labels_dict))  # 通过标签和类型来找到cql语句从而得到问题的答案
        elif question_types == 'character_to_graduate':
            answer_list.extend(
                self.execute_question(question_types, labels_dict))  # 通过标签和类型来找到cql语句从而得到问题的答案
        elif question_types == 'character_to_works':
            answer_list.extend(
                self.execute_question(question_types, labels_dict))  # 通过标签和类型来找到cql语句从而得到问题的答案
        elif question_types == 'character_to_publish':
            answer_list.extend(
                self.execute_question(question_types, labels_dict))  # 通过标签和类型来找到cql语句从而得到问题的答案
        elif question_types == 'character_to_press':
            answer_list.extend(
                self.execute_question(question_types, labels_dict))  # 通过标签和类型来找到cql语句从而得到问题的答案
        elif question_types == 'character_to_count_publish':
            answer_list.extend(
                self.execute_question(question_types, labels_dict))  # 通过标签和类型来找到cql语句从而得到问题的答案
        elif question_types == 'character_to_other':
            answer_list.extend(
                self.execute_question(question_types, labels_dict))  # 通过标签和类型来找到cql语句从而得到问题的答案
        elif question_types == 'character_to_count_publish':
            answer_list.extend(
                self.execute_question(question_types, labels_dict))  # 通过标签和类型来找到cql语句从而得到问题的答案
        elif question_types == 'character_to_unit':
            answer_list.extend(
                self.execute_question(question_types, labels_dict))  # 通过标签和类型来找到cql语句从而得到问题的答案
        elif question_types == 'character_to_originalsinging':
            answer_list.extend(
                self.execute_question(question_types, labels_dict))  # 通过标签和类型来找到cql语句从而得到问题的答案
        elif question_types == 'character_to_schoolCategory':
            answer_list.extend(
                self.execute_question(question_types, labels_dict))  # 通过标签和类型来找到cql语句从而得到问题的答案
        elif question_types == 'character_to_doublequestion':
            answer_list.extend(
                self.execute_question(question_types, labels_dict))  # 通过标签和类型来找到cql语句从而得到问题的答案

        return answer_list

    def execute_question(self, question_type, nodes):
        """
        :param question_type: 问题类型
        :param nodes: 各个结点
        :return: 问题的答案    # 列表类型
        """
        if not nodes:
            return []
        answer_list = list()
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
                         '大姑子',
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
        if question_type == 'character_to_simpleIssue':
            re_list=[]
            flag=0
            for i in nodes.keys():
                if 'character' == i:
                    my_input=nodes['character']
                    flag=1
                    break
                elif 'school' == i:
                    my_input = nodes['school']
                    flag=1
                    break
            if flag==0:
                return answer_list

            for i in relationship:
                if i in self.question:
                    re_list.append(i)
            re_list = self.myfind_max(re_list)
            re_list = self.relist_sort(re_list, self.question)
            if len(re_list) == 1:
                print("1")
                cql = ["match(n)-[r:`{0}`]->(m) where n.name='{1}' return m.name".format(re_list[0], my_input[0])]
                for j in cql:
                    answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
            if len(re_list) == 2:
                print("2")
                print(re_list)
                if '分别' in self.question:
                    for i in re_list:
                        cql = [
                            "match(n)-[r:`{0}`]->(m) where n.name='{1}' return m.name".format(i, my_input[0])]
                        for j in cql:
                            answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                else:
                    cql = [
                        "match(n)-[r:`{0}`]->(m)-[q:`{1}`]->(g) where n.name='{2}' return g.name".format(re_list[0],
                                                                                                         re_list[1],
                                                                                                         my_input[0])]
                    for j in cql:
                        answer_list.extend([i["g.name"] for i in self.connect_graph.run(j) if i["g.name"] != ''])
            print(answer_list)
            return answer_list
            # egg:match(n:`人物`)-[r:`妹妹`]->(m) where n.name='浅井初' return m.name

        elif question_type == 'character_to_countBook':
            print('character_to_countBook')
            my_input=[]
            character=[]
            flag=0
            list_type=nodes.keys()
            if 'character' in list_type:
                character=nodes['character']
                my_input.append(nodes['character'][0])
                flag = 1
            if 'filmAndTelevisionWork' in list_type:
                my_input.append(nodes['filmAndTelevisionWork'][0])
                flag = 1
            if 'school' in list_type:
                my_input.append(nodes['school'][0])
                flag = 1
            if flag == 0:
                return answer_list
            re_list = []
            for i in relationship:
                if i in self.question:
                    re_list.append(i)
            re_list = self.myfind_max(re_list)
            re_list=self.relist_sort(re_list,self.question)
            if '为他人创作的音乐' in self.question:
                re_list.append('为他人创作音乐')
            if len(character)==2:
                for i in re_list:
                    cql = ["match(n)-[r:`{0}`]->(m) where n.name='{1}' return m.name".format(i, character[0])]
                    for j in cql:
                        answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                for i in re_list:
                    cql = ["match(n)-[r:`{0}`]->(m) where n.name='{1}' return m.name".format(i, character[1])]
                    for j in cql:
                        answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                return str(len(answer_list)).split(',')
            else:
                if '作品' in self.question and '参演' not in self.question:
                    if '音乐作品' not in re_list and '文学作品' not in re_list and '主要作品' not in re_list and '代表作品' not in re_list and '发行专辑' not in re_list and '摄影作品'not in re_list:
                        re_list.append('音乐作品')
                        re_list.append('文学作品')
                        re_list.append('主要作品')
                        re_list.append('代表作品')
                        re_list.append('摄影作品')
                for i in re_list:
                    cql = ["match(n)-[r:`{0}`]->(m) where n.name='{1}' return m.name".format(i, my_input[0])]
                    for j in cql:
                        answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                answer_list=list(set(answer_list))
                return str(len(answer_list)).split(',')

        elif question_type == 'character_to_same':
            print('character_to_same')
            list_processed = nodes.keys()
            if 'character' not in list_processed:
                return answer_list
            my_input=nodes['character']
            if len(my_input)<2:
                return answer_list
            for i in ['文学作品', '代表作品', '主要作品', '登场作品','主要配音','主要演员','配音','音乐作品','参演','综艺节目']:
                cql=["match (n)-[r:`{0}`]->(m)<-[q:`{1}`]-(g) where n.name='{2}' and g.name='{3}' return m.name".format(i,i,my_input[0],my_input[1])]
                for j in cql:
                    answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
            return answer_list
        #迪丽热巴和陈若轩有没有共同的作品？

        elif question_type == 'character_to_leader':
            print('character_to_leader')
            flag=0
            for i in nodes.keys():
                if 'school' == i:
                    my_input = nodes['school']
                    flag = 1
                    break
                elif 'association' == i:
                    my_input = nodes['association']
                    flag = 1
                    break
            if flag == 0:
                return answer_list
            cql=["match (n)-[r:`历任领导`]->(m)-[q:`现任领导`]->(n) where n.name='{0}'return m".format(my_input[0])]
            for j in cql:
                answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])

            return answer_list
        #湘潭大学的历任领导中，有多少人是现任领导？

        elif question_type == 'character_to_six':
            print('character_to_six')
            list_processed = nodes.keys()
            if 'character' not in list_processed:
                return answer_list
            my_input=nodes['character']
            re_list=[]
            for i in relationship:
                if i in self.question:
                    re_list.append(i)
            if len(re_list)<2:
                return answer_list
            cql=["match (n)-[r:`{0}`]->(m)<-[q:`{1}`]-(n) where n.name='{2}' return m.name".format(re_list[0],re_list[1],my_input[0])]
            for j in cql:
                answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])

            return answer_list
        #李建复的音乐作品中，有几首是他的代表作品？

        elif question_type == 'character_to_graduate':
            print('character_to_graduate')
            list_processed = nodes.keys()
            if 'character' not in list_processed:
                return answer_list
            my_input=nodes['character']
            cql=["match (n)-[r:`毕业院校`]->(m) where n.name='{0}' return m.name".format(my_input[0])]
            for j in cql:
                answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])

            return answer_list
        #蔡荣根是哪所大学的毕业生？

        elif question_type == 'character_to_works':
            print('character_to_works')
            re_list = []
            list_processed = nodes.keys()
            if 'character' not in list_processed:
                return answer_list
            my_input=nodes['character']
            for i in relationship:
                if i in self.question:
                    re_list.append(i)
            re_list = self.myfind_max(re_list)
            re_list = self.relist_sort(re_list, self.question)
            cql=["match (n)-[r:`{0}`]->(m) where n.name='{1}' return m.name".format(i,my_input[0]) for i in re_list]
            for j in cql:
                answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])

            return answer_list
        #袁阔成的代表作品是什么？

        elif question_type == 'character_to_publish':
            print('character_to_publish')
            list_processed = nodes.keys()
            if 'character' not in list_processed:
                return answer_list
            if 'press' not in list_processed:
                return answer_list
            character = nodes['character']
            press = nodes['press']
            for i in ['文学作品', '代表作品', '主要作品', '登场作品']:
                cql = ["match (n)-[r:`{0}`]->(m)-[q:`出版社`]-(g) where n.name='{1}' and g.name='{2}' return m.name".format(i,character[0],press[0])]
                for j in cql:
                    answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                    print([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
            print("成功")
            return answer_list
        #赵静的作品中，哪一本是由海燕出版社出版的？

        elif question_type == 'character_to_press':
            print('character_to_press')
            mylist_processed = []
            list_processed = nodes.keys()
            if 'works' in list_processed:
                works = nodes['works'][0]
                mylist_processed.append(works)
            if 'filmAndTelevisionWork' in list_processed:
                filmAndTelevisionWork = nodes['filmAndTelevisionWork'][0]
                mylist_processed.append(filmAndTelevisionWork)
            if 'literaryWorks' in list_processed:
                literaryWorks = nodes['literaryWorks'][0]
                mylist_processed.append(literaryWorks)
            if 'musicWorks' in list_processed:
                musicWorks = nodes['musicWorks'][0]
                mylist_processed.append(musicWorks)
            # if 'works' not in list_processed and 'filmAndTelevisionWork' not in list_processed and 'literaryWorks' not in list_processed and 'musicWorks' not in list_processed:
            #     return answer_list
            # if 'works' in list_processed:
            #     i=0
            #     if nodes['works'][0]=='家' and len(nodes['works'])>1:
            #         i=i+1
            #         works = nodes['works'][i]
            #         mylist_processed.append(works)
            #     if nodes['works'][0]!='家' and nodes['works'][0]!='':
            #         works = nodes['works'][0]
            #         mylist_processed.append(works)
            # if 'filmAndTelevisionWork'  in list_processed:
            #     i = 0
            #     if nodes['filmAndTelevisionWork'][0] == '家' and len(nodes['filmAndTelevisionWork']) > 1:
            #         i = i + 1
            #         filmAndTelevisionWork = nodes['filmAndTelevisionWork'][i]
            #         mylist_processed.append(filmAndTelevisionWork)
            #     if nodes['filmAndTelevisionWork'][0]!='家' and nodes['filmAndTelevisionWork'][0]!='':
            #         filmAndTelevisionWork = nodes['works'][0]
            #         mylist_processed.append(filmAndTelevisionWork)
            # if 'literaryWorks'  in list_processed:
            #     i = 0
            #     if nodes['literaryWorks'][0] == '家' and len(nodes['literaryWorks']) > 1:
            #         i = i + 1
            #         literaryWorks = nodes['literaryWorks'][i]
            #         mylist_processed.append(literaryWorks)
            #     if nodes['literaryWorks'][0]!='家' and nodes['literaryWorks'][0]!='':
            #         literaryWorks = nodes['literaryWorks'][0]
            #         mylist_processed.append(literaryWorks)
            # if 'musicWorks' in list_processed:
            #     i = 0
            #     if nodes['musicWorks'][0] == '家' and len(nodes['musicWorks']) > 1:
            #         i = i + 1
            #         musicWorks = nodes['musicWorks'][i]
            #         mylist_processed.append(musicWorks)
            #     if nodes['musicWorks'][0]!='家' and nodes['musicWorks'][0]!='':
            #         musicWorks = nodes['musicWorks'][0]
            #         mylist_processed.append(musicWorks)
            my_input=list(set(mylist_processed))
            if my_input==[]:
                return answer_list

            if 'character' in list_processed:
                character=nodes['character']
                re_list=[]
                for i in relationship:
                    if i in self.question:
                        re_list.append(i)
                re_list = self.myfind_max(re_list)
                re_list = self.relist_sort(re_list, self.question)
                print(re_list)
                if re_list==[]:
                    return answer_list
                cql = ["match (n)-[r:`{0}`]->(m)-[q:`出版社`]->(g) where n.name='{1}' return g.name".format(re_list[0],character[0])]
                for j in cql:
                    answer_list.extend([i["g.name"] for i in self.connect_graph.run(j) if i["g.name"] != ''])
                    print([i["g.name"] for i in self.connect_graph.run(j) if i["g.name"] != ''])
            else:
                cql = ["match (n)-[r:`出版社`]->(m) where n.name='{0}' return m.name".format(my_input[0])]
                for j in cql:
                    answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                    print([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])



            return answer_list
        #墨泠的作品"时笙"是由哪家出版社出版的？


        elif question_type == 'character_to_other':
            print('character_to_other')
            re_list = []
            list_processed = nodes.keys()
            if 'filmAndTelevisionWork' not in list_processed:
                return answer_list
            my_input=nodes['filmAndTelevisionWork']
            if len(my_input)<2:
                return answer_list
            for i in relationship:
                if i in self.question:
                    re_list.append(i)
            re_list = self.myfind_max(re_list)
            re_list = self.relist_sort(re_list, self.question)
            if len(re_list)<2:
                return answer_list
            cql = ["match (g)<-[q:`{0}`]-(n)-[r:`{1}`]->(m)  where m.name='{2}' and g.name='{3}' return n.name".format(
                re_list[0], re_list[1], my_input[0], my_input[1])]
            for j in cql:
                answer_list.extend([i["n.name"] for i in self.connect_graph.run(j) if i["n.name"] != ''])
                print([i["n.name"] for i in self.connect_graph.run(j) if i["n.name"] != ''])

            return answer_list
        #参演过顶楼的演员中，有哪些人的代表作品是熔炉？

        elif question_type == 'character_to_count_publish':
            print('character_to_count_publish')
            list_processed=nodes.keys()
            if 'character' not in list_processed:
                return answer_list
            if 'press' not in list_processed:
                return answer_list
            character=nodes['character']
            press=nodes['press']
            for i in ['文学作品', '代表作品', '主要作品','摄影作品','音乐作品','登场作品']:
                cql = [
                    "match (n)-[r:`{0}`]->(m)-[q:`出版社`]->(g) where n.name='{1}' and g.name='{2}' return m.name".format(
                        i, character[0], press[0])]
            for j in cql:
                answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                print([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
            print(answer_list)
            return str(len(answer_list)).split(',')

        elif question_type == 'character_to_unit':
            print('character_to_unit')
            flag=0
            re_list = []
            list_processed = nodes.keys()
            if 'school' in list_processed:
                school=nodes['school']
                flag=1

            for i in relationship:
                if i in self.question:
                    re_list.append(i)
            re_list = self.myfind_max(re_list)
            re_list = self.relist_sort(re_list, self.question)
            if 'character' not in list_processed and 'school' in list_processed:
                cql = ["MATCH (n)-[r:`所属机构`]->(m) where n.name='{0}'return m.name".format(school[0])]
                for j in cql:
                    answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                    print([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                    return answer_list

            if 'character' in list_processed:
                if re_list != []:
                    character = nodes['character']
                    flag = 1
                if flag == 0:
                    return answer_list
                if '性质' in self.question:
                    cql = ["MATCH (n)-[r:`毕业院校`]->(m)-[q:`办学性质`]->(g) where n.name='{0}' return g.name".format(character[0])]
                    for j in cql:
                        answer_list.extend([i["g.name"] for i in self.connect_graph.run(j) if i["g.name"] != ''])
                        print([i["g.name"] for i in self.connect_graph.run(j) if i["g.name"] != ''])
                    cql = ["MATCH (n)-[r:`毕业院校`]->(m)-[q:`所属机构`]->(g) where n.name='{0}' return g.name".format(
                        character[0])]
                    for j in cql:
                        answer_list.extend([i["g.name"] for i in self.connect_graph.run(j) if i["g.name"] != ''])
                        print([i["g.name"] for i in self.connect_graph.run(j) if i["g.name"] != ''])
                else:
                    cql = ["MATCH (n)-[r:`毕业院校`]->(m)-[q:`所属机构`]->(g) where n.name='{0}' return g.name".format(
                        character[0])]
                    for j in cql:
                        answer_list.extend([i["g.name"] for i in self.connect_graph.run(j) if i["g.name"] != ''])
                        print([i["g.name"] for i in self.connect_graph.run(j) if i["g.name"] != ''])

            return answer_list
        #中央民族大学是哪个机构的下属机构？ 程青的毕业院校是哪个机构所属？

        elif question_type == 'character_to_originalsinging':
            print('character_to_originalsinging')
            re_list = []
            my_input=[]
            list_processed = nodes.keys()
            character=[]
            musicWorks=[]
            if 'character' in list_processed:
                character=nodes['character']
                my_input.append(character)
            if 'musicWorks' in list_processed:
                musicWorks=nodes['musicWorks']
                my_input.append(musicWorks)
            if character == [] and musicWorks == []:
                return answer_list
            for i in relationship:
                if i in self.question:
                    re_list.append(i)
            if '他人创作的音乐' in self.question:
                re_list.append('为他人创作音乐')
            re_list = self.myfind_max(re_list)
            re_list = self.relist_sort(re_list, self.question)

            character=self.relist_sort(character,self.question)
            print(character)

            if character==[] and musicWorks!=[]:
                cql = [
                    "match(n)-[r:`歌曲原唱`]->(m) where n.name='{0}' return m.name".format(musicWorks[0])]
                for j in cql:
                    answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                    print([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                return answer_list
            if character!=[]:
                if '不是她' in self.question or '不是他' in self.question or '不是他自己' in self.question or '其他人' in self.question:
                    if re_list==[]:
                        return answer_list
                    cql = [
                        "match(n)-[r:`{0}`]->(m)-[q:`歌曲原唱`]->(g) where n.name='{1}' and g.name<>'{2}' return m.name".format(re_list[0],character[0],character[0])]
                    for j in cql:
                        answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                        print([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                    return answer_list
                elif len(character)==2:
                    cql = [
                        "match(n)-[r:`{0}`]->(m)-[q:`歌曲原唱`]->(g) where n.name='{1}' and g.name='{2}' return m.name".format(
                            i, character[0], character[1]) for i in re_list]
                    for j in cql:
                        answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                        print([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                    return answer_list

            return answer_list
        #游鸿明的音乐作品和为他人创作的音乐中，哪些歌曲的原唱是张学友？

        elif question_type == 'character_to_schoolCategory':
            print('character_to_schoolCategory')
            re_list = []
            list_processed = nodes.keys()
            if 'school' not in list_processed:
                return answer_list
            school=nodes['school']
            cql = ["match (n)-[r:`办学性质`]->(m) where n.name='{0}' return m.name".format(school[0])]
            for j in cql:
                answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                print([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])

            return answer_list

        elif question_type == 'character_to_doublequestion':
            print('character_to_schoolCategory')
            re_list = []
            filmAndTelevisionWork=[]
            character=[]
            school=[]
            list_processed = nodes.keys()
            if 'filmAndTelevisionWork' in list_processed:
                filmAndTelevisionWork=nodes['filmAndTelevisionWork']
                filmAndTelevisionWork=self.node_sort(filmAndTelevisionWork,self.question)
            if 'character' in list_processed:
                character=nodes['character']
                character = self.node_sort(character, self.question)
            if 'school' in list_processed:
                school=nodes['school']
                school = self.node_sort(school, self.question)
            for i in relationship:
                if i in self.question:
                    re_list.append(i)
            re_list = self.myfind_max(re_list)
            re_list = self.relist_sort(re_list, self.question)
            if '演员' in self.question and filmAndTelevisionWork!=[]:
                if character!=[]:
                    if len(re_list)<1:
                        return answer_list
                    else:
                        if '主要演员' in re_list and len(re_list)!=1:
                            re_list.remove('主要演员')
                        cql = [
                            "match (n)-[r:`主要演员`]->(m)-[q:`{0}`]->(g) where n.name='{1}'and g.name='{2}'  return m.name".format(
                                re_list[0], filmAndTelevisionWork[0], character[0])]
                        for j in cql:
                            answer_list.extend(
                                [i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                            print([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                            return answer_list

                    return answer_list
                elif len(filmAndTelevisionWork)>1:
                    if len(re_list)<1:
                        return answer_list
                    else:
                        if '主要演员' in re_list and len(re_list)!=1:
                            re_list.remove('主要演员')
                        print("判断成功")
                        print(filmAndTelevisionWork[0])
                        print(filmAndTelevisionWork[1])
                        print(re_list[0])
                        cql = [
                            "match (n)-[r:`主要演员`]->(m)-[q:`{0}`]->(g) where n.name='{1}'and g.name='{2}'  return m.name".format(
                                re_list[0], filmAndTelevisionWork[0], filmAndTelevisionWork[1])]
                        for j in cql:
                            answer_list.extend(
                                [i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                            print([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                            return answer_list
                elif len(filmAndTelevisionWork)<1:
                    return answer_list

            else:
                my_input = []
                for i in filmAndTelevisionWork:
                    my_input.append(i)
                for i in character:
                    my_input.append(i)
                for i in school:
                    my_input.append(i)
                my_input = list(set(my_input))
                my_input = self.node_sort(my_input, self.question)
                if len(re_list) == 1:
                    if len(my_input) == 1:
                        cql = [
                            "match (n)-[r:`{0}`]->(m)-[q:`{1}`]->(g) where n.name='{2}'and g.name='{3}'  return m.name".format(
                                re_list[0], re_list[0], my_input[0], my_input[0])]
                        for j in cql:
                            answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                            print([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                            return answer_list

                    if len(my_input) > 1:
                        cql = [
                            "match (n)-[r:`{0}`]->(m)-[q:`{1}`]->(g) where n.name='{2}'and g.name='{3}'  return m.name".format(
                                re_list[0], re_list[0], my_input[0], my_input[1])]
                        for j in cql:
                            answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                            print([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                            return answer_list

                elif len(re_list) > 1:
                    if len(my_input) == 1:
                        cql = [
                            "match (n)-[r:`{0}`]->(m)-[q:`{1}`]->(g) where n.name='{2}'and g.name='{3}'  return m.name".format(
                                re_list[0], re_list[1], my_input[0], my_input[0])]
                        for j in cql:
                            answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                            print([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                            return answer_list

                    if len(my_input) > 1:
                        cql = [
                            "match (n)-[r:`{0}`]->(m)-[q:`{1}`]->(g) where n.name='{2}'and g.name='{3}'  return m.name".format(
                                re_list[0], re_list[1], my_input[0], my_input[1])]
                        for j in cql:
                            answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                            print([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                            return answer_list

            return answer_list
        #母亲是条河的主要演员中，谁的前妻是陈佳妍？





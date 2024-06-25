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

    def execute_main(self, data_dict, question):
        """
        :param data_dict: {'arg':{结点：标签},'question_types':[标签所对应的类型]}
        :return: 返回问题的结果
        """
        self.question = question  # 全局问题
        nodes_dict = data_dict['arg']
        labels_dict = self.build_entityDict(nodes_dict)  # {标签：结点}
        question_types = data_dict['question_types']
        answer_list = []  # 一维列表
        for question_type in question_types:
            print(question)
            if question_type == 'character_to_simpleIssue':
                answer_list.extend(
                    self.execute_question(question_type, labels_dict['character']))  # 通过标签和类型来找到cql语句从而得到问题的答案
            elif question_type == 'character_to_countBook':
                answer_list.extend(
                    self.execute_question(question_type, labels_dict['character']))  # 通过标签和类型来找到cql语句从而得到问题的答案
            elif question_type == 'character_to_same':
                answer_list.extend(
                    self.execute_question(question_type, labels_dict['character']))  # 通过标签和类型来找到cql语句从而得到问题的答案
            elif question_type == 'character_to_leader':
                answer_list.extend(
                    self.execute_question(question_type, labels_dict['character']))  # 通过标签和类型来找到cql语句从而得到问题的答案
            elif question_type == 'character_to_six':
                answer_list.extend(
                    self.execute_question(question_type, labels_dict['character']))  # 通过标签和类型来找到cql语句从而得到问题的答案
            elif question_type == 'character_to_graduate':
                answer_list.extend(
                    self.execute_question(question_type, labels_dict['character']))  # 通过标签和类型来找到cql语句从而得到问题的答案
            elif question_type == 'character_to_works':
                answer_list.extend(
                    self.execute_question(question_type, labels_dict['character']))  # 通过标签和类型来找到cql语句从而得到问题的答案
            elif question_type == 'character_to_publish':
                answer_list.extend(
                    self.execute_question(question_type, labels_dict['character']))  # 通过标签和类型来找到cql语句从而得到问题的答案
            elif question_type == 'character_to_doublecount':
                answer_list.extend(
                    self.execute_question(question_type, labels_dict['character']))  # 通过标签和类型来找到cql语句从而得到问题的答案
            # elif question_type == 'character_to_other':
            #     answer_list.extend(
            #         self.execute_question(question_type, labels_dict['character']))  # 通过标签和类型来找到cql语句从而得到问题的答案

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
        if question_type == 'character_to_simpleIssue':
            count=0
            re_list=[]
            print('character_to_simpleIssue')
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
            for i in relationship:
                if i in self.question:
                    count=count+1
                    re_list.append(i)
            if count == 1:
                print("1")
                cql = ["match(n:`人物`)-[r:`{0}`]->(m) where n.name='{1}' return m.name".format(re_list[0], k) for k in
                       nodes]
                for j in cql:
                    answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
            if count == 2:
                print("2")
                cql = [
                    "match(n:`人物`)-[r:`{0}`]->(m)-[q:`{1}`]->(g) where n.name='{2}' return g.name".format(re_list[0],
                                                                                                            re_list[1],
                                                                                                            k) for k
                    in
                    nodes]
                for j in cql:
                    answer_list.extend([i["g.name"] for i in self.connect_graph.run(j) if i["g.name"] != ''])


            return answer_list
            # egg:match(n:`人物`)-[r:`妹妹`]->(m) where n.name='浅井初' return m.name

        elif question_type == 'character_to_countBook':
            print('character_to_countBook')
            for i in ['文学作品', '代表作品', '主要作品', '登场作品']:
                cql = ["match(n:`人物`)-[r:`{0}`]->(m) where n.name='{1}' return m.name".format(i, k) for k in nodes]
                for j in cql:
                    answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
            print('成功')
            return str(len(answer_list)).split(',')

        elif question_type == 'character_to_same':
            print('character_to_same')
            for i in ['文学作品', '代表作品', '主要作品', '登场作品','主要配音','主要演员','配音','音乐作品']:
                cql=["match (n:`人物`)-[r:`{0}`]->(m)<-[q:`{1}`]-(g:`人物`) where n.name='{2}' and g.name='{3}' return m.name".format(i,i,nodes[0],nodes[1])]
                for j in cql:
                    answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
            return answer_list
        #迪丽热巴和陈若轩有没有共同的作品？

        elif question_type == 'character_to_leader':
            print('character_to_leader')
            cql=["match (n)-[r:`历任领导`]->(m)-[q:`现任领导`]->(n) where n.name='{0}'return m".format(nodes[0])]
            for j in cql:
                answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])

            return answer_list
        #湘潭大学的历任领导中，有多少人是现任领导？

        elif question_type == 'character_to_six':
            print('character_to_six')
            i='音乐作品'
            g='代表作品'
            cql=["match (n)-[r:`{0}`]->(m)<-[q:`{1}`]-(n) where n.name='{2}' return m".format(i,g,nodes[0])]
            for j in cql:
                answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])

            return answer_list

        elif question_type == 'character_to_graduate':
            print('character_to_graduate')
            cql=["match (n)-[r:`毕业院校`]->(m) where n.name='{0}' return m.name".format(nodes[0])]
            for j in cql:
                answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])

            return answer_list
        #蔡荣根是哪所大学的毕业生？

        elif question_type == 'character_to_works':
            print('character_to_works')
            cql=["match (n)-[r:`代表作品`]->(m) where n.name='{0}' return m.name".format(nodes[0])]
            for j in cql:
                answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])

            return answer_list
        #袁阔成的代表作品是什么？

        elif question_type == 'character_to_publish':
            print('character_to_publish')
            for i in ['文学作品', '代表作品', '主要作品', '登场作品']:
                cql = ["match (n)-[r:`{0}`]->(m)-[q:`出版社`]-(g) where n.name='{1}' and g.name='{2}' return m.name".format(i,nodes[0],nodes[1])]
                for j in cql:
                    answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                    print([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])

            return answer_list
        #赵静的作品中，哪一本是由海燕出版社出版的？

        elif question_type == 'character_to_doublecount':
            print('character_to_doublecount')
            for i in ['音乐作品','发行专辑']:
                cql = ["match (n)-[r:`{0}`]->(m) where n.name='{1}' return m.name".format(i, nodes[0])]
                for j in cql:
                    answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])

            return str(len(answer_list)).split(',')
        #詹妮弗·洛佩兹的音乐作品和发行专辑总共有多少个？

        elif question_type == 'character_to_count_publish':
            print('character_to_count_publish')
            for i in ['文学作品', '代表作品', '主要作品', '登场作品']:
                cql = ["match (n)-[r:`{0}`]->(m)-[q:`出版社`]-(g) where n.name='{1}' and g.name='{2}' return m.name".format(i,nodes[0],nodes[1])]
                for j in cql:
                    answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
                    print([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])

            return answer_list

        # elif question_type == 'character_to_other':
        #     for i in ['文学作品', '代表作品', '主要作品', '登场作品']:
        #         cql = ["match (g)-[q:`i`]-(n)-[r:`参演`]->(m) where m.name='{0}' and g.name='{1}' return n.name".format(i,nodes[0],nodes[1])]
        #         for j in cql:
        #             answer_list.extend([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
        #             print([i["m.name"] for i in self.connect_graph.run(j) if i["m.name"] != ''])
        #
        #     return answer_list
        #参演过顶楼的演员中，有哪些人的代表作品是熔炉？




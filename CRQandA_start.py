import json
from Analyse_Question import AnalyseQuestion
from Execute_Statement import ExecuteStatement


class RelationshipRobot:
    def __init__(self):  # 初始化
        self.analysis_model = AnalyseQuestion()  # 初始化各个结点以及问题
        self.execute_statement = ExecuteStatement()

    def chat_main(self, question):
        answer = "知识库未提及"
        data_dict = self.analysis_model.analyze_question(question)  # {'arg':{结点：标签},'question_types':[标签所对应的类型]}
        if not data_dict:
            return [answer]
        answer_list = self.execute_statement.execute_main(data_dict, question)  # 返回问题答案
        if not answer_list:
            return [answer]
        else:
            return list(set(answer_list))


if __name__ == '__main__':
    robot = RelationshipRobot()
    # 提问
    # while 1:
    #     question = input("咨询：")
    #     answer_list = robot.chat_main(question)
    #     print("answer:", answer_list)  # 返回结果为列表

    # 测试
    with open("data//train_qa.json", "r", encoding='utf-8') as fp:
        infor_dict = json.load(fp)
    count = 0
    flag = 0
    for infor in infor_dict:
        answer_list = robot.chat_main(infor_dict[infor]["question"])
        if set(answer_list) == set(infor_dict[infor]["answer"]):
            flag += 1
            print(infor_dict[infor]["question"], "\t\t", answer_list, "\t\t", flag)  # 正确数目
        count += 1
    print("正确率为:", flag / count)

    # 答案
    # result_dict = dict()
    # with open("data//test_qa.json", "r", encoding='utf-8') as fp:
    #     infor_dict = json.load(fp)
    # for i in range(len(infor_dict)):
    #     temp_dict = infor_dict[str(i)]
    #     question = temp_dict["question"]
    #     answer_list = robot.chat_main(question)
    #     temp_dict["answer"] = answer_list
    #     result_dict[str(i)] = temp_dict
    #     print(question, "\t\t", answer_list, "\t\t", i)
    # with open("result_qa.json", "w", encoding='utf-8') as fp:
    #     json.dump(result_dict, fp)

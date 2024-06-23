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
            return answer
        answer_list = self.execute_statement.execute_main(data_dict, question)  # 返回问题答案
        if not answer_list:
            return answer
        else:
            return list(set(answer_list))


if __name__ == '__main__':
    robot = RelationshipRobot()
    while 1:
        question = input("咨询：")
        answer_list = robot.chat_main(question)
        print("answer:", answer_list)  # 返回结果为列表

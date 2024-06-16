

class RelationshipRobot:
    def __init__(self):  # 初始化
        self.analysis_model = AnalyzeQuestion()  #


if __name__ == '__main__':
    robot = RelationshipRobot()
    while 1:
        question = input("咨询：")
        answer = robot.chat_main(question)
        print("answer:", answer)

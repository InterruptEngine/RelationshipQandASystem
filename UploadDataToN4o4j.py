from py2neo import Graph, Node, Relationship
import os


def generateGraph_Node(graph, lable, name):
    """
    创建节点
    :param graph:
    :param lable:
    :param name:
    :return:
    """
    node = Node(lable, name=name)
    graph.create(node)


def generateGraph_Relation(graph, node_1, relation, node_2):
    """
    创建关系
    :param graph:
    :param node_1:
    :param relation:
    :param node_2:
    :return:
    """
    relationship = Relationship(node_1, relation, node_2)
    graph.create(relationship)


def create_graph():
    connect_graph = Graph("http://localhost:7474", auth=("neo4j", "123456789"), name="neo4j")
    connect_graph.delete_all()  # 删掉所有结点
    dir_list = os.listdir("processed_file")
    node_dict = {}
    count = 1
    for cur_file in dir_list:
        path = os.path.join("processed_file", cur_file)
        with open(path, "r", encoding="utf-8") as fp:
            for line in fp.readlines():
                line = line.strip()
                label = cur_file.strip('.txt')
                node = generateGraph_Node(connect_graph, label, line)  # 创建结点
                node_dict[label+line] = node
                print(count)
                count += 1
        print(path + ' is success')
        count = 1
    count = 1
    with open(r'data/kg(utf8).txt', 'r', encoding='utf-8') as fp:
        for line in fp.readlines():
            line = line.split('\t')
            start = line[0]
            relationship = line[1]
            end = line[2]
            end = end.strip('\n')
            # print(start, relationship, end)
            generateGraph_Relation(connect_graph, start, relationship, end)
            print(count)
            count += 1


if __name__ == '__main__':
    create_graph()
from py2neo import Graph, Node, Relationship
import os


def generateGraph_Node(graph, label, name):
    """
    创建节点
    :param graph:Graph()
    :param label:结点label
    :param name:结点name
    :return:node
    """
    node = Node(label, name=name)
    graph.create(node)
    return node


def generateGraph_Relation(graph, node_1, relation, node_2):
    """
    创建关系
    :param graph:Graph()
    :param node_1:头实体结点
    :param relation:关系
    :param node_2:尾实体结点
    """
    relationship = Relationship(node_1, relation, node_2)
    graph.create(relationship)


def create_graph():
    connect_graph = Graph("http://localhost:7474", auth=("neo4j", "123456789"), name="neo4j")
    connect_graph.delete_all()  # 删掉所有结点
    count = 0
    with open(r"processed_file//result_data.txt", "r", encoding='utf-8') as fp:
        for line in fp.readlines():
            line_list = line.split('\t')
            start = line_list[0]
            relationship = line_list[1]
            end = line_list[2].strip('\n')
            start_label, start_node = start.split('$$$')
            end_label, end_node = end.split('$$$')
            node1 = generateGraph_Node(connect_graph, start_label, start_node)  # 创建结点
            node2 = generateGraph_Node(connect_graph, end_label, end_node)  # 创建结点
            generateGraph_Relation(connect_graph, node1, relationship, node2)  # 创建关系
            print(count)
            count += 1
    # dir_list = os.listdir("processed_file")
    # node_dict = {}
    # count = 1
    # for cur_file in dir_list:
    #     path = os.path.join("processed_file", cur_file)
    #     with open(path, "r", encoding="utf-8") as fp:
    #         for line in fp.readlines():
    #             line = line.strip()
    #             label = cur_file.strip('.txt')
    #             node = generateGraph_Node(connect_graph, label, line)  # 创建结点
    #             node_dict[label + '$$$' + line] = node
    #             print(count)
    #             count += 1
    #     print(path + ' is success')
    #     count = 1
    # count = 1
    # with open(r'processed_file//result_data.txt', 'r', encoding='utf-8') as fp:
    #     for line in fp.readlines():
    #         line = line.split('\t')
    #         start = line[0]
    #         relationship = line[1]
    #         end = line[2]
    #         end = end.strip('\n')
    #         # print(start, relationship, end)
    #         start_node = node_dict[start]
    #         end_node = node_dict[end]
    #         generateGraph_Relation(connect_graph, start_node, relationship, end_node)
    #         print(count)
    #         count += 1


if __name__ == '__main__':
    create_graph()

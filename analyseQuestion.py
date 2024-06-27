import jieba
import json
import torch
import numpy as np
from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer
# 示例数据，模拟包含 1000 条自然语言问题的数据集
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

os.environ['CURL_CA_BUNDLE'] = ''
os.environ['HTTP_PROXY'] = "http://127.0.0.1:7890"
os.environ['HTTPS_PROXY'] = "http://127.0.0.1:7890"
os.environ['ALL_PROXY'] = "socks5://127.0.0.1:7890"


def kmeans_clustering():
    with open(r'data//test_qa.json', 'r', encoding='utf-8') as f:
        qa_data = json.loads(f.read())
        sample_data = [qa_data[i]['question'] for i in qa_data.keys()]
        # print(sample_data)

    # 加载 Sentence-BERT 模型
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    model = SentenceTransformer('msmarco-distilbert-base-tas-b').to(device)
    # 使用 Sentence-BERT 将问题转换为向量表示
    question_embeddings = model.encode(sample_data)

    # 定义要聚类的簇数
    num_clusters = 24

    # 使用 K 均值聚类算法进行聚类
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(question_embeddings)
    cluster_centers = kmeans.cluster_centers_
    cluster_labels = kmeans.labels_

    # 从每个簇中选择代表性的问题
    representative_questions = []
    for cluster_id in range(num_clusters):
        cluster_questions = [sample_data[i] for i in range(len(sample_data)) if cluster_labels[i] == cluster_id]
        cluster_center = cluster_centers[cluster_id]
        distances = [np.linalg.norm(model.encode([question])[0] - cluster_center) for question in cluster_questions]
        representative_question_index = np.argmin(distances)
        representative_question = cluster_questions[representative_question_index]
        representative_questions.append(representative_question)

    vital_question = list()
    # 打印代表性问题
    for i, question in enumerate(representative_questions):
        print(f"代表性问题 {i + 1}: {question}")
        vital_question.append(question)
    with open("vital_question.txt", "w", encoding="utf-8") as fp:
        fp.write("\n".join(vital_question))


# Jieba 分词
def chinese_tokenizer(text):
    return jieba.cut(text, cut_all=False)


def cosine_similarity_text(str1, str2):
    """
    计算两个文本的余弦相似度
    :param str1: 文本1
    :param str2: 文本2
    :return: 相似度值
    """
    words1 = ' '.join(chinese_tokenizer(str1))
    words2 = ' '.join(chinese_tokenizer(str2))
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([words1, words2])
    return cosine_similarity(tfidf)[0][1]


if __name__ == '__main__':
    kmeans_clustering()
    # vital_question_list = list()
    # with open("vital_question.txt", "r", encoding="utf-8") as fp:
    #     for i in fp.readlines():
    #         vital_question_list.append(i.strip("\n"))
    # with open("data//test_qa.json", "r", encoding="utf-8") as fp:
    #     data = json.loads(fp.read())
    # test_qa_list = [data[i]["question"] for i in data.keys()]
    # # print(vital_question_list)
    # # print(test_qa_list)
    # total_max = 0  # 计算总和
    # extra_question_list = list()
    # for i in range(len(test_qa_list)):  # 计算相似度
    #     flag = 0
    #     max = 0
    #     for j in range(len(vital_question_list)):
    #         result = cosine_similarity_text(test_qa_list[i], vital_question_list[j])
    #         if max < result:
    #             flag = j
    #             max = result
    #     if max < 0.15:  # 相似度小于0.15的就加入到其中
    #         extra_question_list.append(test_qa_list[i])
    #     print(test_qa_list[i], vital_question_list[flag], max)
    #     total_max += max
    # print("相似度之和为{0}".format(total_max / len(test_qa_list)))
    # with open("real_question.txt", "w", encoding="utf-8") as fp:
    #     fp.write("\n".join(vital_question_list + extra_question_list))

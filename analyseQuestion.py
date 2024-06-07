import json
import torch
import numpy as np
from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer
# 示例数据，模拟包含 1000 条自然语言问题的数据集
import os
os.environ['CURL_CA_BUNDLE'] = ''
os.environ['HTTP_PROXY'] = "http://127.0.0.1:7890"
os.environ['HTTPS_PROXY'] = "http://127.0.0.1:7890"
os.environ['ALL_PROXY'] = "socks5://127.0.0.1:7890"
def kmeans_clustering():
    with open(r'data//train_qa.json', 'r', encoding='utf-8') as f:
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
    num_clusters = 300

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

    # 打印代表性问题
    for i, question in enumerate(representative_questions):
        print(f"代表性问题 {i+1}: {question}")


if __name__=='__main__':
    kmeans_clustering()
from TextReader import TextReader
import math
from random import *


def read_all_texts():
    reader = TextReader()
    texts = []
    for i in range(1, 11):
        texts.append(reader.getText(f"text_{i}.txt"))

    return texts


def get_unique_words():
    unique_words = []
    texts = read_all_texts()
    for text in texts:
        for word in text:
            if word not in unique_words:
                unique_words.append(word)

    return unique_words


def calculate_TF(unique_words, texts):
    TF = []
    for text in texts:
        words = dict()
        for word in unique_words:
            words[word] = text.count(word)
        TF.append(words)

    return TF


def calculate_IDF(unique_words, texts):
    words = dict()
    number_of_documents = 10
    for word in unique_words:
        counter = 0
        for text in texts:
            if word in text:
                counter += 1
        words[word] = math.log(number_of_documents / counter)

    return words


def calculate_TF_IDF(TF, IDF, unique_words):
    total_result = []
    for tf in TF:
        result = []
        for word in unique_words:
            result.append(tf[word] * IDF[word])
        total_result.append(result)

    return total_result


def create_random_centriods(clusters_num, len, max):
    centroids = []
    for i in range(0, clusters_num):
        centroid = []
        for coordinate in range(0, len):
            centroid.append(uniform(0, max[0]))
        centroids.append(centroid)

    return centroids


def make_clusters(matrix, centroids):
    cluster1 = []
    cluster2 = []
    cluster3 = []
    for i in matrix:
        min_distance = 1000000000000000
        centroid_index = -1
        for centroid in centroids:
            if centroid:
                curr = math.dist(centroid, i)
                if curr < min_distance:
                    min_distance = curr
                    centroid_index += 1

        if centroid_index == 0:
            cluster1.append(i)
        elif centroid_index == 1:
            cluster2.append(i)
        elif centroid_index == 2:
            cluster3.append(i)

    return cluster1, cluster2, cluster3


if __name__ == '__main__':
    texts = read_all_texts()
    for text in texts:
        print(text)

    print()
    unique_words = get_unique_words()
    print(unique_words)
    print()

    TF = calculate_TF(unique_words, texts)
    for i in TF:
        print(i)
    print()

    IDF = calculate_IDF(unique_words, texts)
    print(IDF)
    print()

    final_matrix = calculate_TF_IDF(TF, IDF, unique_words)
    maxNum = []
    for i in final_matrix:
        print(i)
        maxNum.append(max(i))
    print()

    print("maxNum:" + str(max(maxNum)))
    print()

    centroids = create_random_centriods(3, len(unique_words), maxNum)
    for centroid in centroids:
        print("initial random centroid: " + str(centroid))
    print()

    centroid1 = centroids[0]
    centroid2 = centroids[1]
    centroid3 = centroids[2]
    for i in range(0, 10):
        cluster1, cluster2, cluster3 = make_clusters(final_matrix, centroids)
        print("cluster length: "+str(len(cluster1))+" cluster1:" + str(cluster1))
        print("cluster length: "+str(len(cluster2))+" cluster2:" + str(cluster2))
        print("cluster length: "+str(len(cluster3))+" cluster3:" + str(cluster3))
        print()
        if cluster1:
            centroid1 = [sum(x) / len(x) for x in zip(*cluster1)]
        if cluster2:
            centroid2 = [sum(x) / len(x) for x in zip(*cluster2)]
        if cluster3:
            centroid3 = [sum(x) / len(x) for x in zip(*cluster3)]
        centroids = [centroid1, centroid2, centroid3]
        print("centroid1:" + str(centroids[0]))
        print("centroid2:" + str(centroids[1]))
        print("centroid3:" + str(centroids[2]))
        print()

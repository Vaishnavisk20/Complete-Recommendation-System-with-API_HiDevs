import math

def precision_at_k(recommended, relevant, k=5):
    recommended = recommended[:k]
    return len(set(recommended) & set(relevant)) / k

def recall_at_k(recommended, relevant, k=5):
    recommended = recommended[:k]
    return len(set(recommended) & set(relevant)) / len(relevant)

def ndcg_at_k(recommended, relevant, k=5):
    dcg = 0
    for i, item in enumerate(recommended[:k]):
        if item in relevant:
            dcg += 1 / math.log2(i + 2)

    idcg = sum([1 / math.log2(i + 2) for i in range(min(len(relevant), k))])
    return dcg / idcg if idcg > 0 else 0
from engine.evaluator import precision_at_k, recall_at_k, ndcg_at_k

recommended = [1,2,3,4,5]
relevant = [3,4,7]

print("Precision@5:", precision_at_k(recommended, relevant))
print("Recall@5:", recall_at_k(recommended, relevant))
print("NDCG@5:", ndcg_at_k(recommended, relevant))
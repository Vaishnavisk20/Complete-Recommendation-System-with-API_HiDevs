def score_content(content, similarity, interest_match):
    score = 0
    score += 0.5 * content.popularity
    score += 0.3 * similarity
    score += 5 if interest_match else 0
    return score
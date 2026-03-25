from engine.candidate_gen import generate_candidates
from engine.scorer import score_content
from engine.similarity import cosine_similarity

class RecommendationOrchestrator:
    def __init__(self, content_repo, interaction_repo, user_repo):
        self.content_repo = content_repo
        self.interaction_repo = interaction_repo
        self.user_repo = user_repo
        self.cache = {}

    def get_recommendations(self, user_id, limit=5):

        if user_id in self.cache:
            return self.cache[user_id]

        user = self.user_repo.get(user_id)
        history = self.interaction_repo.get_user_history(user_id)
        all_content = self.content_repo.all()

        history_ids = [h.content_id for h in history]

        # Cold start
        if not history:
            recs = sorted(all_content, key=lambda x: -x.popularity)[:limit]
        else:
            candidates = generate_candidates(all_content, history_ids)

            scored = []
            for c in candidates:
                similarity = cosine_similarity([c.popularity], [5])
                interest_match = user and c.category in user.interests

                score = score_content(c, similarity, interest_match)

                scored.append((c, score))

            scored.sort(key=lambda x: -x[1])
            recs = [c[0] for c in scored[:limit]]

        result = []
        for c in recs:
            reason = "Popular content"
            if user and c.category in user.interests:
                reason = "Matches your interests"

            result.append({
                "id": c.id,
                "title": c.title,
                "score": c.popularity,
                "reason": reason
            })

        self.cache[user_id] = result
        return result
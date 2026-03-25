def generate_candidates(all_content, user_history_ids):
    # Remove already interacted content
    return [c for c in all_content if c.id not in user_history_ids]
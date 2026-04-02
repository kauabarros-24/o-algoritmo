
class Recommend:
    def __init__(self):
        self.recommend_based_friends
        self.recommend_based_like
        self.add_history

    def recommend_based_like(self, user_id: str, history: dict):
        if not user_id: 
            raise ValueError("User ID cannot be empty | Potassio don't like empty user ID")
    
    def recommend_based_friends(self, user_id: str, friend_id: str, history: dict):
        pass

 
    
from src.utils import potas_message


class Recommend:
    def __init__(self):
        self.recommend

    def recommmend(self, user_id: str, history: dict, content: dict):
        if not user_id:
            raise ValueError("User ID is required", potas_message)
        
        counter = 0
        for c in content:
            for i in history.content:
                if c == i:
                    counter+=1
        response = {
            "user_id": user_id,
            "recommendation": content[:counter]
        }
        return response
    
        

                
    

 
    
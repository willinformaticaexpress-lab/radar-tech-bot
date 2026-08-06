class UserBehavior:

    def __init__(self):
        self.history = []


    def register_action(
        self,
        user_id,
        product,
        action
    ):

        self.history.append({
            "user_id": user_id,
            "product": product,
            "action": action
        })


    def recommend(
        self,
        user_id
    ):

        interests = []

        for item in self.history:

            if item["user_id"] == user_id:

                if item["action"] in [
                    "click",
                    "view",
                    "purchase"
                ]:
                    interests.append(
                        item["product"]
                    )

        return interests

from app.models.base import BaseModel


class Review(BaseModel):
    def __init__(self, text, rating, place_id, user_id):
        super().__init__()

        if len(text) > 1024:
            raise ValueError("Text length exceeds 1024 characters")

        if rating is None or rating < 0 or rating > 5:
            raise ValueError("Rating must be between 0 and 5")

        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id

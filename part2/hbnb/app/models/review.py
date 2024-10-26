from app.models.base import BaseModel
from app.services import facade


class Review(BaseModel):
    """
    Class representing a review of a place.
    """

    def __init__(self, text, rating, place_id, user_id):
        """
        Initialize a review.
        """
        super().__init__()

        self.validate(text, rating, place_id, user_id)
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id

    @staticmethod
    def validate(text, rating, place_id, user_id):
        """
        Validate review data.
        """
        if len(text) > 1024:
            raise ValueError('Text length exceeds 1024 characters')

        if rating is None or rating < 1 or rating > 5:
            raise ValueError('Rating must be between 1 and 5')

        if not place_id or not isinstance(place_id, str):
            raise ValueError('Place must be provided')

        if not user_id or not isinstance(user_id, str):
            raise ValueError('User must be provided')

    def update_review(self, **kwargs):
        """
        Update the review.
        """
        if 'text' in kwargs:
            text = kwargs['text']
        else:
            text = self.text

        if 'rating' in kwargs:
            rating = kwargs['rating']
        else:
            rating = self.rating

        if 'place' in kwargs:
            place_id = kwargs['place']
        else:
            place_id = self.place_id

        if 'user' in kwargs:
            user_id = kwargs['user']
        else:
            user_id = self.user_id

        self.validate(
            text,
            rating,
            place_id,
            user_id
        )
        self.update(kwargs)

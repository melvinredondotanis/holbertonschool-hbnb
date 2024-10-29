from app.models.base import BaseModel


class Review(BaseModel):
    """
    Class representing a review of a place.
    """

    def __init__(
            self,
            text,
            rating,
            place_id,
            user_id):
        """
        Initialize a review.
        """
        super().__init__()

        self.__text = text
        self.__rating = rating
        self.__place_id = place_id
        self.__user_id = user_id

    @property
    def text(self):
        """
        Get the review text.
        """
        return self.__text

    @text.setter
    def text(self, value):
        """
        Set the review text.
        """
        if len(value) > 2048:
            raise ValueError('Text length exceeds 2048 characters')
        self.__text = value

    @property
    def rating(self):
        """
        Get the review rating.
        """
        return self.__rating

    @rating.setter
    def rating(self, value):
        """
        Set the review rating.
        """
        if value < 1 or value > 5:
            raise ValueError('Rating must be between 1 and 5')
        self.__rating = value

    @property
    def place_id(self):
        """
        Get the place ID.
        """
        return self.__place_id

    @place_id.setter
    def place_id(self, value):
        """
        Set the place ID.
        """
        if not value or not isinstance(value, str):
            raise ValueError('Place must be provided')
        self.__place_id = value

    @property
    def user_id(self):
        """
        Get the user ID.
        """
        return self.__user_id

    @user_id.setter
    def user_id(self, value):
        """
        Set the user ID.
        """
        if not value or not isinstance(value, str):
            raise ValueError('User must be provided')
        self.__user_id = value

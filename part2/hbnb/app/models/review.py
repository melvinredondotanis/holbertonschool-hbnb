from app.models.base import BaseModel
from app.models.user import User
from app.models.place import Place


class Review(BaseModel):
    """
    Class representing a review of a place.
    """

    def __init__(
            self,
            text,
            rating,
            place,
            user):
        """
        Initialize a review.
        """
        super().__init__()

        self.__text = text
        self.__rating = rating
        self.__place = place
        self.__user = user

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
    def place(self):
        """
        Get the place ID.
        """
        return self.__place

    @place.setter
    def place_id(self, value):
        """
        Set the place ID.
        """
        if not value or not isinstance(value, Place):
            raise ValueError('Place must be provided')
        self.__place = value

    @property
    def user(self):
        """
        Get the user ID.
        """
        return self.__user

    @user.setter
    def user(self, value):
        """
        Set the user ID.
        """
        if not value or not isinstance(value, User):
            raise ValueError('User must be provided')
        self.__user = value

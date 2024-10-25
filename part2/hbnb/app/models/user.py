import re

from app.models.base import BaseModel


class User(BaseModel):
    """
    Class representing a user of the application.
    """

    def __init__(self, first_name, last_name, email, is_admin=False):
        """
        Initialize a user.
        """
        super().__init__()

        self.validate(first_name, last_name, email, is_admin)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

    @staticmethod
    def validate(first_name, last_name, email, is_admin):
        """
        Validate user data.
        """
        if not first_name or len(first_name) > 50:
            raise ValueError(
                'First name must be provided and be less than 50 characters'
                )

        if not last_name or len(last_name) > 50:
            raise ValueError(
                'Last name must be provided and be less than 50 characters'
                )

        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise ValueError('Invalid email format')

        if not isinstance(is_admin, bool):
            raise ValueError('is_admin must be a boolean')

    def update_profile(self, **kwargs):
        """
        Update the user's profile.
        """
        self.update(kwargs)
        self.validate(
            self.first_name,
            self.last_name,
            self.email,
            self.is_admin
            )

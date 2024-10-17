import re

from base import BaseModel


class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()

        if not first_name or len(first_name) > 50:
            raise ValueError("First name must be provided and be less than 50 characters")

        if not last_name or len(last_name) > 50:
            raise ValueError("Last name must be provided and be less than 50 characters")

        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise ValueError("Invalid email format")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

    def update_profile(self, **kwargs):
        self.update(kwargs)
        self.validate()

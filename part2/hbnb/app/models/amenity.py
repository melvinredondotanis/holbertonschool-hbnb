from app.models.base import BaseModel


class Amenity(BaseModel):
    """
    Class representing an amenity.
    """

    def __init__(self, name):
        """
        Initialize an amenity.
        """
        super().__init__()

        self.validate(name)
        self.name = name

    @staticmethod
    def validate(name):
        """
        Validate amenity data.
        """
        if not name or len(name) > 50:
            raise ValueError(
                'Name must be provided and be less than 50 characters'
            )

    def update(self, data):
        """
        Update the amenity.
        """
        if 'name' in data:
            self.name = data['name']
        self.validate(self.name)

    def __str__(self):
        """
        Return a string representation of the amenity.
        """
        return 'Amenity(id={}, name={})'.format(self.id, self.name)

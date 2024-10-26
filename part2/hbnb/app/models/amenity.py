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

    def update_amenity(self, **kwargs):
        """
        Update the amenity.
        """
        name = None
        if 'name' in kwargs:
            name = kwargs['name']

        self.validate(name)
        self.update(kwargs)

    def __str__(self):
        """
        Return a string representation of the amenity.
        """
        return 'Amenity(id={}, name={})'.format(self.id, self.name)

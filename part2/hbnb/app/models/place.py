from app.models.base import BaseModel


class Place(BaseModel):
    """
    Class representing a place.
    """

    def __init__(
            self,
            title,
            description,
            price,
            latitude,
            longitude,
            owner_id
            ):
        """
        Initialize a place.
        """
        super().__init__()

        self.validate(
            title,
            description,
            price,
            latitude,
            longitude,
            owner_id
        )
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.reviews = []
        self.amenities = []

    @staticmethod
    def validate(
        title,
        description,
        price,
        latitude,
        longitude,
        owner_id
    ):
        """
        Validate place data.
        """
        if not isinstance(title, str) or len(title) > 100:
            raise ValueError(
                'Title must a maximum length of 100 characters'
            )

        if description is not None and not isinstance(description, str):
            raise ValueError(
                'Description must be a string'
            )

        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError(
                'Price must be a positive number'
            )

        if not isinstance(
            latitude,
            (int, float)
        ) or not (
            -90.0 <= latitude <= 90.0
        ):
            raise ValueError(
                'Latitude must be a number between -90.0 and 90.0'
            )

        if not isinstance(
            longitude,
            (int, float)
        ) or not (
            -180.0 <= longitude <= 180.0
        ):
            raise ValueError(
                'Longitude must be a number between -180.0 and 180.0'
            )

        if not isinstance(owner_id, str):
            raise ValueError(
                'Owner ID must be a string or a valid user ID'
            )

    def update_place(self, **kwargs):
        """
        Update the place.
        """
        if 'title' in kwargs:
            self.title = kwargs['title']
        if 'description' in kwargs:
            self.description = kwargs['description']
        if 'price' in kwargs:
            self.price = kwargs['price']
        if 'latitude' in kwargs:
            self.latitude = kwargs['latitude']
        if 'longitude' in kwargs:
            self.longitude = kwargs['longitude']
        if 'owner_id' in kwargs:
            self.owner_id = kwargs['owner_id']

        self.validate(
            self.title,
            self.description,
            self.price,
            self.latitude,
            self.longitude,
            self.owner_id
        )
        self.update(kwargs)

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

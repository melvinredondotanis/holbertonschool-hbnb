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
            owner_id,
            amenities
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
            owner_id,
            amenities
        )
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner_id
        self.reviews = []
        self.amenities = amenities

    @staticmethod
    def validate(
        title,
        description,
        price,
        latitude,
        longitude,
        owner,
        amenities
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

        if not isinstance(owner, str):
            raise ValueError(
                'Owner ID must be a string or a valid user ID'
                )

        if not isinstance(amenities, list):
            raise ValueError(
                'Amenities must be a list of amenities'
            )

    def update_place(self, **kwargs):
        """
        Update the place.
        """
        title = None
        description = None
        price = None
        latitude = None
        longitude = None
        owner = None
        amenities = None
        if 'title' in kwargs:
            title = kwargs['title']

        # Else, keep the current description
        # Note: description can be set to None
        if 'description' in kwargs:
            description = kwargs['description']
        else:
            description = self.description

        if 'price' in kwargs:
            price = kwargs['price']

        if 'latitude' in kwargs:
            latitude = kwargs['latitude']

        if 'longitude' in kwargs:
            longitude = kwargs['longitude']

        if 'owner' in kwargs:
            owner = kwargs['owner']

        if 'amenities' in kwargs:
            amenities = kwargs['amenities']

        self.validate(
            title,
            description,
            price,
            latitude,
            longitude,
            owner,
            amenities
        )
        self.update(kwargs)

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def remove_review(self, review):
        """Remove a review from the place."""
        self.reviews.remove(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

from app.models.base import BaseModel


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.validate(title, description, price, latitude, longitude)
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

    @staticmethod
    def validate(title, description, price, latitude, longitude):
        if not isinstance(title, str) or len(title) > 100:
            raise ValueError("Title must be a string with a maximum length of 100 characters")

        if description is not None and not isinstance(description, str):
            raise ValueError("Description must be a string")

        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number")

        if not isinstance(latitude, (int, float)) or not (-90.0 <= latitude <= 90.0):
            raise ValueError("Latitude must be a number between -90.0 and 90.0")

        if not isinstance(longitude, (int, float)) or not (-180.0 <= longitude <= 180.0):
            raise ValueError("Longitude must be a number between -180.0 and 180.0")

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner.id,
            'owner': self.owner.to_dict(),
            'amenities': [amenity.id for amenity in self.amenities]
        }
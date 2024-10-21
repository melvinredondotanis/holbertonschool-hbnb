from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass

    def create_amenity(self, amenity_data):
        # Create new amenity
        new_amenity = Amenity(**amenity_data)
        return self.amenity_repo.add(new_amenity)
    
    def get_amenity(self, amenity_id):
        # Retrieve an amenity by ID
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        # Retrieve all amenities
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        # Update an existing amenity
        amenity = self.amenity_repo.get(amenity_id)
        if amenity:
            for key, value in amenity_data.items():
                setattr(amenity, key, value)
            return self.amenity_repo.update(amenity)
        return None
    
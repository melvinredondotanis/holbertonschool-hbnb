from app.models.user import User
from app.models.place import Place
from app.models.amenity import Amenity

from app.persistence.repository import InMemoryRepository
from app.models.review import Review


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


    def create_amenity(self, amenity_data):
        new_amenity = Amenity(**amenity_data)
        self.amenity_repo.add(new_amenity)
        return new_amenity
    
    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)
        if amenity:
            return self.amenity_repo.update(amenity_id, amenity_data)
        return None


    def create_place(self, place_data):
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)
        if place:
            for key, value in place_data.items():
                setattr(place, key, value)
            return self.place_repo.update(place, place_data)
        return None

    def create_review(self, review_data):
        # Create a review, including validation for user_id, place_id, and rating
        new_review = Review(**review_data)
        self.review_repo.add(new_review)
        return new_review

    def get_review(self, review_id):
        # Retrieve a review by ID
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        # Retrieve all reviews
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        # Placeholder for logic to retrieve all reviews for a specific place
        return self.place_repo.get(place_id.reviews)

    def update_review(self, review_id, review_data):
        # Update a review
        if self.review_repo.get(review_id):
            return self.review_repo.update(review_id, review_data)
        return None

    def delete_review(self, review_id):
        # Placeholder for logic to delete a review
        return self.review_repo.delete(review_id)
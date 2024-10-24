from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
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

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass

    def create_amenity(self, amenity_data):
        # Create new amenity
        new_amenity = Amenity(**amenity_data)
        self.amenity_repo.add(new_amenity)
        return new_amenity
    
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
            return self.amenity_repo.update(amenity_id, amenity_data)
        return None
    
    def create_review(self, review_data):
        # Create a review, including validation for user_id, place_id, and rating
        if all(key in review_data for key in ('user_id', 'place_id', 'rating')):
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
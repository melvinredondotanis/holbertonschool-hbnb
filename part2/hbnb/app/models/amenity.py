from app.models.base import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()

        if not isinstance(name, str) or len(name) > 50:
            raise ValueError("Name must be a string with a maximum length of 50 characters")
        
        self.name = name

    def __str__(self):
        return f"Amenity(id={self,id}, name={self.name})"
        
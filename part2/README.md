# HBNB - Part 2

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Explanation](#Explanation)
- [Authors](#authors)

## Description
HBNB is a web application that allows users to manage and book places. This project is part of the Holberton School curriculum and focuses on implementing a full-stack web application.

## Installation
To install and run this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/melvinredondotanis/holbertonschool-hbnb
    ```
2. Navigate to the project directory:
    ```bash
    cd holbertonschool-hbnb/part2/hbnb
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To start the application, run the following command:
```bash
python3 run.py
```
Open your web browser and navigate to `http://localhost:5000` to access the application.

## File Structure
```
part2/hbnb/
├── api
│   ├── __init__.py
│   ├── v1
│   │   ├── __init__.py
│   │   ├── amenities.py
│   │   ├── places.py
│   │   ├── reviews.py
│   │   └── users.py
├── models
│   ├── __init__.py
│   ├── base.py
│   ├── amenity.py
│   ├── place.py
│   ├── review.py
│   └── user.py
├── persistence
│   ├── __init__.py
│   └── repository.py
├── services
│   ├── __init__.py
│   └── facade.py
├── config.py
├── requirements.txt
└── run.py
```
* The 'app/' directory contains the core application code.
* The 'api/' directory contains the API endpoints, organized by version ('v1/').
* The 'models/' directory contains the business logic classes.
* The 'services/' directory is where the Facade pattern is implemented, managing the interaction between layers.
* The 'persistence/' directory is where the in-memory repository is implemented, This will be replaced by database-backed solution using SQL alchemy.
* 'run.py' is the entry point for flask application running.
* 'config.py' is where the configuration for the application is stored.
* 'requirements.txt' is where the dependencies for the application are listed.
* 'test/' directory is where all the note about the testing result will be stored.

## Explanation

### Amenity
A POST method is sent to register a new amenity. It retrieves the data from the API payload and create a new amenity using a **'facade.create_amenity'**. When a ValueError occurs, it returns an 400 status code error message. If successful, it returns the newly created aneminy's ID and name with a 201 status code.
```python
    def post(self):
        """Register a new amenity"""
        amenity_data = api.payload
        try:
            amenity = facade.create_amenity(amenity_data)
        except ValueError as e:
            return {'error': str(e)}, 400
        return {
            'id': amenity.id,
            'name': amenity.name
            }, 201
```

**Expected input:**
```http
POST /api/v1/amenities/
Content-Type: application/json

{
  "name": "Wi-Fi"
}
```

**Expected Response:**

```jsonc
{
  "id": "1fa85f64-5717-4562-b3fc-2c963f66afa6",
  "name": "Wi-Fi"
}

// 201 Created
```

**Possible Status Codes:**

- 201 Created: When the amenity is successfully created.
- 400 Bad Request: If input data is invalid.
---
### Places
The get method retrieves a list of all places by calling **'facade.get_all_places()'**. It initializes an empty list, iterates through the retrieved places, and appends each place's id, title, latitude, and longitude to the list. Finally, it returns this list with a status code of 200 to indicate success.
```python
    def get(self):
        """Retrieve a list of all places"""
        places = []
        for place in facade.get_all_places():
            places.append(
                {
                    'id': place.id,
                    'title': place.title,
                    'latitude': place.latitude,
                    'longitude': place.longitude
                }
                )
        return places, 200
```

**Expected input:**
```http
GET /api/v1/places/
Content-Type: application/json
```

**Expected Response:**

```jsonc
[
  {
    "id": "1fa85f64-5717-4562-b3fc-2c963f66afa6",
    "title": "Cozy Apartment",
    "latitude": 37.7749,
    "longitude": -122.4194
  },
  ...
]

// 200 OK
```

**Possible Status Codes:**

- 200 OK: List of places retrieved successfully.

---
### Reviews
The put method updates an existing review based on the provided **'review_id'**. By checking the Review existence, it returns a 404 status code in case it doesn't exist. Check the input data if it's empty. If not, it updates the review using **'facade.update_review'** and returns a 200 status code if successful.
```python
    def put(self, review_id):
        """Update a review's information"""
        if facade.get_review(review_id) is None:
            return {'error': 'Review not found'}, 404

        review_data = api.payload
        if review_data == {}:
            return {'error': 'Invalid input data'}, 400
        try:
            facade.update_review(review_id, review_data)
        except ValueError as e:
            return {'error': str(e)}, 400
        return {'message': 'Review updated successfully'}, 200
```

**Expected input:**
```http
PUT /api/v1/reviews/<review_id>
Content-Type: application/json

{
  "text": "Amazing stay!",
  "rating": 4
}
```

**Expected Response:**

```jsonc
{
  "message": "Review updated successfully"
}

// 200 OK
```

**Possible Status Codes:**

- 200 OK: When the review is successfully updated.
- 404 Not Found: If the review does not exist.
- 400 Bad Request: If input data is invalid.

## Authors
- **Meinvin Redondotanis** - [GitHub](https://github.com/melvinredondotanis)
- **Benoit Marin** - [GitHub](https://github.com/SadScourge)
- **Zakaria Aattache** - [GitHub](https://github.com/FYUDerma)

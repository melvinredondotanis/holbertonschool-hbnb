# TESTS

## USERS

### POST /api/v1/users/

**Registering a new user with valid informations**
```
curl -X 'POST' \
    'http://127.0.0.1:5000/api/v1/users/' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "first_name": "john",
    "last_name": "holberton",
    "email": "john@holberton.com"
}'
```
Expected Response:
```
{
  "id": "138e9f33-422b-4fd6-8e4b-d37c2d089d94",
  "first_name": "john",
  "last_name": "holberton",
  "email": "john@holberton.com"
}
// 200 OK
```

**Non-valid email**
```
curl -X 'POST' \
    'http://127.0.0.1:5000/api/v1/users/' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "first_name": "john",
    "last_name": "holberton",
    "email": "johnholberton.com"
}'
```
Expected Response:
```
{
  "error": "Invalid email format"
}
// 400 BAD REQUEST
```

**Already used email**
```
curl -X 'POST' \
    'http://127.0.0.1:5000/api/v1/users/' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "first_name": "john",
    "last_name": "holberton",
    "email": "john@holberton.com"
}'
```
Expected Response:
```
{
  "error": "Email already registered"
}
// 400 BAD REQUEST
```

### GET /api/v1/users/

**Retrieving a list of all users**
```
curl -X 'GET' \
  'http://127.0.0.1:5000/api/v1/users/' \
  -H 'accept: application/json'
```
Expected Response:
```
[
  {
    "id": "138e9f33-422b-4fd6-8e4b-d37c2d089d94",
    "first_name": "john",
    "last_name": "holberton",
    "email": "john@holberton.com"
  },
  {
    "id": "4d1d3708-8b4a-4f47-b0ef-3574b3aac50a",
    "first_name": "second",
    "last_name": "user",
    "email": "valid@mail.com"
  }
]
// 200 OK
```

### GET /api/v1/users/{user_id}

**Retrieving a user with valid ID**
```
curl -X 'GET' \
  'http://127.0.0.1:5000/api/v1/users/4d1d3708-8b4a-4f47-b0ef-3574b3aac50a' \
  -H 'accept: application/json'
```
Expected Response:
```
{
  "id": "4d1d3708-8b4a-4f47-b0ef-3574b3aac50a",
  "first_name": "second",
  "last_name": "user",
  "email": "valid@mail.com"
}
// 200 OK
```

**Retrieving a user with invalid ID**
```
curl -X 'GET' \
  'http://127.0.0.1:5000/api/v1/users/thisisanid' \
  -H 'accept: application/json'
```
Expected Response:
```
{
  "error": "User not found"
}
// 400 BAD REQUEST
```

### PUT /api/v1/users/{user_id}

**Updating an user with valid informations and valid ID**
```
curl -X 'PUT' \
  'http://127.0.0.1:5000/api/v1/users/4d1d3708-8b4a-4f47-b0ef-3574b3aac50a' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "first_name": "harry",
  "last_name": "potter",
  "email": "harry@hogwart.com"
}'
```
Expected Response:
```
{
  "id": "4d1d3708-8b4a-4f47-b0ef-3574b3aac50a",
  "first_name": "harry",
  "last_name": "potter",
  "email": "harry@hogwart.com"
}
// 200 OK
```

**Non-valid ID**
```
curl -X 'PUT' \
  'http://127.0.0.1:5000/api/v1/users/thisisanid' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "first_name": "harry",
  "last_name": "potter",
  "email": "harry@hogwart.com"
}'
```
Expected Response:
```
{
  "error": "User not found"
}
// 404 NOT FOUND
```

**Non-valid informations(mail)**
```
curl -X 'PUT' \
  'http://127.0.0.1:5000/api/v1/users/4d1d3708-8b4a-4f47-b0ef-3574b3aac50a' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "first_name": "ronald",
  "last_name": "weasley",
  "email": "ron@hogwartcom"
}'
```
Expected Response:
```
{
  "error": "Invalid email format"
}
// 400 BAD REQUEST
```

**Non-valid informations(empty string)**
```
curl -X 'PUT' \
  'http://127.0.0.1:5000/api/v1/users/4d1d3708-8b4a-4f47-b0ef-3574b3aac50a' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "first_name": "",
  "last_name": "",
  "email": "ron@hogwart.com"
}'
```
Expected Response:
```
{
  "error": "First name must be provided and be less than 50 characters"
}
// 400 BAD REQUEST
```

## AMENITIES

### POST /api/v1/amenities/
**Creating a new amenity with a valid name**
```
curl -X 'POST' \
  'http://127.0.0.1:5000/api/v1/amenities/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "shower"
}'
```
Expected Response:
```
{
  "id": "db234ac5-e8a7-45e2-be1e-4d02b0b68fbc",
  "name": "shower"
}
// 200 OK
```

**testing with an empty string**
```
curl -X 'POST' \
  'http://127.0.0.1:5000/api/v1/amenities/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": ""
}'
```
Expected Response:
```
{
  "error": "Name must be provided and be less than 50 characters"
}
// 400 BAD REQUEST
```

### GET /api/v1/amenities/
**Retrieving a list of all amenities**
```
curl -X 'GET' \
  'http://127.0.0.1:5000/api/v1/amenities/' \
  -H 'accept: application/json'
```
Expected Response:
```
[
  {
    "id": "db234ac5-e8a7-45e2-be1e-4d02b0b68fbc",
    "name": "shower"
  },
  {
    "id": "6c0eb0ee-f9d1-419a-989c-f79dc35a86e7",
    "name": "Swimming pool"
  }
]
// 200 OK
```

### GET /api/v1/amenities/{amenity_id}
**Retrieving an amenity by ID**
```
curl -X 'GET' \
  'http://127.0.0.1:5000/api/v1/amenities/6c0eb0ee-f9d1-419a-989c-f79dc35a86e7' \
  -H 'accept: application/json'
```
Expected Response:
```
{
  "id": "6c0eb0ee-f9d1-419a-989c-f79dc35a86e7",
  "name": "Swimming pool"
}
// 200 OK
```

**With an invalid ID**
```
curl -X 'GET' \
  'http://127.0.0.1:5000/api/v1/amenities/thisisanid' \
  -H 'accept: application/json'
```
Expected Response:
```
{
  "error": "Amenity not found"
}
// 404 NOT FOUND
```

### PUT /api/v1/amenities/{amenity_id}
**Updating an amenity with valid informations**
```
curl -X 'PUT' \
  'http://127.0.0.1:5000/api/v1/amenities/6c0eb0ee-f9d1-419a-989c-f79dc35a86e7' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Jacuzzi"
}'
```
Expected Response:
```
{
  "message": "Amenity updated successfully"
}
// 200 OK
```

**Updating an amenity with invalid informations(id)**
```
curl -X 'PUT' \
  'http://127.0.0.1:5000/api/v1/amenities/thisisanid' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "jacuzzi"
}'
```
Expected Response:
```
{
  "error": "Amenity not found"
}
// 404 NOT FOUND
```

**Updating an amenity with invalid informations(empty string)**
```
curl -X 'PUT' \
  'http://127.0.0.1:5000/api/v1/amenities/6c0eb0ee-f9d1-419a-989c-f79dc35a86e7' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": ""
}'
```
Expected Response:
```
{
  "error": "Name must be provided and be less than 50 characters"
}
// 400 BAD REQUEST
```

## PLACES

### POST /api/v1/places/
**Creating a place with valid informations**
```
curl -X 'POST' \
  'http://127.0.0.1:5000/api/v1/places/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Big House",
  "description": "it'\''s really big",
  "price": 1000,
  "latitude": 50,
  "longitude": 30,
  "owner_id": "af500c39-d68c-4632-8082-91be1f346d06"
}'
```
Expected Response:
```
{
  "id": "dfb63de7-23b7-4b5c-8539-bcbf39c802e7",
  "title": "Big House",
  "description": "it's really big",
  "price": 1000,
  "latitude": 50,
  "longitude": 30,
  "owner_id": "af500c39-d68c-4632-8082-91be1f346d06"
}
// 201 CREATED
```

**Creating a place with an invalid user ID**
```
curl -X 'POST' \
  'http://127.0.0.1:5000/api/v1/places/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Big House",
  "description": "it'\''s really big",
  "price": 1000,
  "latitude": 50,
  "longitude": 30,
  "owner_id": "this is an id"
}'
```
Expected Response:
```
{
  "error": "Invalid owner_id"
}
// 400 BAD REQUEST
```

**Creating a place with an empty string**
```
curl -X 'POST' \
  'http://127.0.0.1:5000/api/v1/places/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "",
  "description": "",
  "price": 1000,
  "latitude": 50,
  "longitude": 30,
  "owner_id": "af500c39-d68c-4632-8082-91be1f346d06"
}'
```
Expected Response:
```
{
  "error": "Name must be provided and be less than 50 characters"
}
// 400 BAD REQUEST
```
Response Received:
```
{
  "id": "da167086-426b-43a9-b8d6-4fc72fcdc1ba",
  "title": "",
  "description": "",
  "price": 1000,
  "latitude": 50,
  "longitude": 30,
  "owner_id": "af500c39-d68c-4632-8082-91be1f346d06"
}
// 200 OK
```

### GET /api/v1/places/
**Retrieves a lsit of all places**
```
curl -X 'GET' \
  'http://127.0.0.1:5000/api/v1/places/' \
  -H 'accept: application/json'
```
Expected Response:
```
[
  {
    "id": "dfb63de7-23b7-4b5c-8539-bcbf39c802e7",
    "title": "Big House",
    "latitude": 50,
    "longitude": 30
  },
  {
    "id": "da167086-426b-43a9-b8d6-4fc72fcdc1ba",
    "title": "House 2",
    "latitude": 50,
    "longitude": 30
  },
]
// 200 OK
```

### GET /api/v1/places/places/{place_id}/reviews

### GET /api/v1/places/{place_id}
**Retrieve a place with it's ID**
```
curl -X 'GET' \
  'http://127.0.0.1:5000/api/v1/places/dfb63de7-23b7-4b5c-8539-bcbf39c802e7' \
  -H 'accept: application/json'
```
Expected Response:
```
{
  "id": "dfb63de7-23b7-4b5c-8539-bcbf39c802e7",
  "title": "Big House",
  "description": "it's really big",
  "price": 1000,
  "latitude": 50,
  "longitude": 30,
  "owner": {
    "id": "af500c39-d68c-4632-8082-91be1f346d06",
    "first_name": "john",
    "last_name": "holberton",
    "email": "john@holberton.com"
  },
  "amenities": []
}
// 200 OK
```

**Retrieve a place with an incorrect ID**
```
curl -X 'GET' \
  'http://127.0.0.1:5000/api/v1/places/thisisanid' \
  -H 'accept: application/json'
```
Expected Response:
```
{
  "error": "Place not found"
}
// 404 NOT FOUND
```

### PUT /api/v1/places/{place_id}

## REVIEWS

### POST /api/v1/reviews/
### GET /api/v1/reviews/
### GET /api/v1/reviews/{review_id}
### DELETE /api/v1/reviews/{review_id}
### PUT /api/v1/reviews/{review_id}

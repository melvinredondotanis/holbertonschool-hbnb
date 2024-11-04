from flask_restx import Namespace, Resource, fields

from app.services import facade


api = Namespace('places', description='Place operations')

amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(
        description='Amenity ID'
        ),
    'name': fields.String(
        description='Name of the amenity'
        )
})

user_model = api.model('PlaceUser', {
    'id': fields.String(
        description='User ID'
        ),
    'first_name': fields.String(
        description='First name of the owner'
        ),
    'last_name': fields.String(
        description='Last name of the owner'
        ),
    'email': fields.String(
        description='Email of the owner'
        )
})

review_model = api.model('PlaceReview', {
    'id': fields.String(
        description='Review ID'
        ),
    'text': fields.String(
        description='Text of the review'
        ),
    'rating': fields.Integer(
        description='Rating of the place (1-5)'
        ),
    'user_id': fields.String(
        description='ID of the user'
        )
})

place_model = api.model('Place', {
    'title': fields.String(
        required=True,
        description='Title of the place'
        ),
    'description': fields.String(
        description='Description of the place'
        ),
    'price': fields.Float(
        required=True,
        description='Price per night'
        ),
    'latitude': fields.Float(
        required=True,
        description='Latitude of the place'
        ),
    'longitude': fields.Float(
        required=True,
        description='Longitude of the place'
        ),
    'owner_id': fields.String(
        required=True,
        description='ID of the owner'
        ),
    'owner': fields.Nested(
        user_model,
        description='Owner of the place'
        ),
    'amenities': fields.List(
        fields.Nested(amenity_model),
        description='List of amenities'
        ),
    'reviews': fields.List(
        fields.Nested(review_model),
        description='List of reviews'
        )
})


@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model, validate=True)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        place_data = api.payload

        user = facade.get_user(place_data.get('owner_id'))
        if user is None:
            return {'error': 'Invalid owner_id'}, 400

        del place_data['owner_id']
        place_data['owner'] = user
        if place_data.get('amenities'):
            for amenity in place_data.get('amenities'):
                if facade.get_amenity(amenity['id']) is None:
                    return {'error': 'Invalid amenity ID'}, 400

        try:
            place = facade.create_place(place_data)
            return {
                'id': place.id,
                'title': place.title,
                'description': place.description,
                'price': place.price,
                'latitude': place.latitude,
                'longitude': place.longitude,
                'owner_id': place.owner.id,
                }, 201
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.response(200, 'List of places retrieved successfully')
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


@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place(place_id)
        if place:
            return {
                'id': place.id,
                'title': place.title,
                'description': place.description,
                'price': place.price,
                'latitude': place.latitude,
                'longitude': place.longitude,
                'owner': {
                    'id': place.owner.id,
                    'first_name': place.owner.first_name,
                    'last_name': place.owner.last_name,
                    'email': place.owner.email
                    },
                'amenities': [
                    {
                        'id': facade.get_place(place_id).id,
                        'name': facade.get_amenity(amenity['id']).name
                    }
                    for amenity in place.amenities
                    ]
                    }, 200
        return {'error': 'Place not found'}, 404

    @api.expect(place_model, validate=True)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        place_data = api.payload

        user = facade.get_user(place_data.get('owner_id'))
        if user is None:
            return {'error': 'Invalid owner_id'}, 400

        del place_data['owner_id']
        place_data['owner'] = user

        if facade.get_place(place_id) is None:
            return {'error': 'Place not found'}, 404

        if place_data == facade.get_place(place_id):
            return {'error': 'Invalid input data'}, 400

        if place_data.get('amenities'):
            for amenity in place_data.get('amenities'):
                if facade.get_amenity(amenity['id']) is None:
                    return {'error': 'Invalid amenity ID'}, 400

        try:
            facade.update_place(place_id, place_data)
        except ValueError as e:
            return {'error': str(e)}, 400
        return {'message': 'Place updated successfully'}, 200


@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        reviews = facade.get_reviews_by_place(place_id)
        if reviews:
            return [
                {
                    'id': review.id,
                    'text': review.text,
                    'rating': review.rating
                }
                for review in reviews
                ], 200
        return {'error': 'Review not found'}, 404

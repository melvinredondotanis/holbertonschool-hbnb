from flask_restx import Namespace, Resource, fields

from app.services import facade


api = Namespace('places', description='Place operations')

amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'owner': fields.Nested(user_model, description='Owner details'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
})


@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        place_data = api.payload    
        try:
            place = facade.create_place(place_data)
            return {'id': place.id,
                    'title': place.title,
                    'description': place.description,
                    'price': place.price,
                    'latitude': place.latitude,
                    'longitude': place.longitude,
                    'owner_id': place.owner_id,
                    }, 201
        except ValueError as e:
            return {'error': str(e)}, 400


    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        places = []
        for place in facade.get_all_places():
            places.append({'id': place.id,
                           'title': place.title,
                           'latitude': place.latitude,
                           'longitude': place.longitude,
                           })
        return places, 200


@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place(place_id)
        user_id = place.owner_id
        if place:
            user = facade.get_user(user_id)
            return {'id': place.id,
                    'title': place.title,
                    'description': place.description,
                    'price': place.price,
                    'latitude': place.latitude,
                    'longitude': place.longitude,
                    'owner_id': place.owner_id,
                    'owner': {'id': place.owner_id,
                              'first_name': user.first_name,
                              'last_name': user.last_name,
                              'email': user.email
                              },
                              'amenities': [
                                  {'id': amenity.id,
                                   'name': amenity.name
                                   }
                                   for amenity in place.amenities
                                   ]
                    }, 200
        return {'error': 'Place not found'}, 404

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        place_data = api.payload
        if facade.get_place(place_id) is None:
            return {'error': 'Place not found'}, 404

        try:
            facade.update_place(place_id, place_data)               
        except ValueError as e:
            return {'error': str(e)}, 400
        return {'message': 'Place updated successfully'}, 200
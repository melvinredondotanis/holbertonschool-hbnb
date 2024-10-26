from flask_restx import Namespace, Resource, fields

from app.services import facade


api = Namespace('users', description='User operations')

user_model = api.model('User', {
    'first_name': fields.String(
        required=True,
        description='First name of the user'
        ),
    'last_name': fields.String(
        required=True,
        description='Last name of the user'
        ),
    'email': fields.String(
        required=True,
        description='Email of the user'
        )
})


@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(200, 'User successfully created')
    @api.response(400, 'Email already registered')
    def post(self):
        """Register a new user"""
        user_data = api.payload
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        if 'is_admin' in user_data:
            return {'error': 'Invalid input data'}, 400

        try:
            new_user = facade.create_user(user_data)
        except Exception as e:
            return {'error': str(e)}, 400
        return {
            'id': new_user.id,
            'first_name': new_user.first_name,
            'last_name': new_user.last_name,
            'email': new_user.email
            }, 200

    @api.response(200, 'List of users retrieved successfully')
    def get(self):
        """Retrieve a list of all users"""
        users = []
        for user in facade.get_all_users():
            users.append(
                {
                    'id': user.id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email
                }
                )
        return users, 200


@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if user:
            return {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
                }, 200
        return {'error': 'User not found'}, 404

    @api.expect(user_model, validate=True)
    @api.response(200, 'User successfully updated')
    @api.response(404, 'User not found')
    @api.response(400, 'Invalid input data')
    def put(self, user_id):
        """Update user details"""
        user_data = api.payload
        if facade.get_user(user_id) is None:
            return {'error': 'User not found'}, 404

        if 'is_admin' in user_data:
            return {'error': 'Invalid input data'}, 400

        try:
            facade.update_user(user_id, user_data)
        except Exception as e:
            return {'error': str(e)}, 400

        user = facade.get_user(user_id)
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
            }, 200

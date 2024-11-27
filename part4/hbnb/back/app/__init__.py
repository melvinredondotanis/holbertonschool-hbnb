from flask import Flask
from flask_restx import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Create here to avoid circular imports
bcrypt = Bcrypt()
jwt = JWTManager()
db = SQLAlchemy()

import config
from app.api.v1.auth import api as auth_ns
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as places_ns
from app.api.v1.reviews import api as reviews_ns
from app.models.user import User
from app.models.amenity import Amenity


def create_app(config_class=config.DevelopmentConfig):
    """
    Create and configure the Flask application.
    """
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_class)
    api = Api(
        app,
        version='1.0',
        title='HBnB API',
        description='HBnB Application API',
        contact_email='melvin.redondotanis@holbertonstudents.com',
        authorizations={
            'BearerAuth': {
                'type': 'apiKey',
                'in': 'header',
                'name': 'Authorization',
                'description': 'Bearer authentication token'
                }
            },
        security='BearerAuth'
    )

    api.add_namespace(auth_ns, path='/api/v1/auth')
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')

    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
        admin = User.query.filter_by(email='admin@hbnb.com').first()
        if not admin:
            admin = User(
                id='36c9050e-ddd3-4c3b-9731-9f487208bbc1',
                _first_name='Admin',
                _last_name='HBnB',
                _email='admin@hbnb.io',
                _password='$2b$12$yPzwR02tJub1wfuWcCoZ8eL8aK6a2nz5SAeU9KVS7m//K48OuemVW',
                _is_admin=True
            )
            db.session.merge(admin)

            wifi = Amenity.query.filter_by(id='ad6cbba4-33c9-48e3-b6ee-d494ee5a6b45').first()
            if not wifi:
                wifi = Amenity(
                id='ad6cbba4-33c9-48e3-b6ee-d494ee5a6b45',
                _name='WiFi'
                )
                db.session.merge(wifi)

            pool = Amenity.query.filter_by(id='ad6cbba4-33c9-48e3-b6ee-d494ee5a6b46').first()
            if not pool:
                pool = Amenity(
                id='ad6cbba4-33c9-48e3-b6ee-d494ee5a6b46',
                _name='Swimming Pool'
                )
                db.session.merge(pool)

            ac = Amenity.query.filter_by(id='0b8744c5-5c58-4c4a-8467-48392e306e28').first()
            if not ac:
                ac = Amenity(
                id='0b8744c5-5c58-4c4a-8467-48392e306e28',
                _name='Air Conditioning'
                )
                db.session.merge(ac)
                
            db.session.commit()

    return app

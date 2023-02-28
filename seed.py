from app import app, db
from models import Pet


with app.app_context():
    db.drop_all()
    db.create_all()


pet1 = Pet(name='Fluffy', species='Cat', photo_url='https://via.placeholder.com/150', age=3, notes='Likes to nap', available=True)
pet2 = Pet(name='Rover', species='Dog', photo_url='https://via.placeholder.com/150', age=5, notes='Loves to play fetch', available=True)
pet3 = Pet(name='Whiskers', species='Cat', photo_url='https://via.placeholder.com/150', age=1, notes='Very shy', available=False)


db.session.add(pet1)
db.session.add(pet2)
db.session.add(pet3)


db.session.commit()

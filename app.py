from flask import Flask, request, redirect, render_template
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SECRET_KEY'] = 'mike123'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


@app.route('/')
def show_homepage():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)



@app.route('/add', methods=['GET', 'POST'])
def add_pet_form():

    form = AddPetForm()

    if form.validate_on_submit():
        name =  form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()

        return redirect('/')

    return render_template('add_pet.html', form = form)



@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def show_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        form.populate_obj(pet)
        db.session.commit()
        return redirect('/')

    return render_template('edit_pet.html', pet = pet, form = form)



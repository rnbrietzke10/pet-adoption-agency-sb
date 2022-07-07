from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class AddPetForm(FlaskForm):
    """Form for adding a pet"""

    name = StringField("Pet Name", validators=[InputRequired(message="Please enter a pet name.")])
    species = SelectField("Species", choices=[("Cat", "Cat"), ("Dog", "Dog"), ("Porcupine", "Porcupine")],validators=[InputRequired(message="Please enter a species for the pet.")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(message="Please enter a valid URL.")])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30, message="Please enter an age between 0 and 30")])
    notes = StringField("Notes", validators=[Optional()])


class EditPetFrom(FlaskForm):
    """Form for editing pet info"""
    photo_url = StringField("Photo URL", validators=[Optional(), URL(message="Please enter a valid URL.")])
    notes = StringField("Notes", validators=[Optional()])
    available = SelectField("Pet Availability", choices=[(True, "Available"), (False, "Unavailable")], validators=[InputRequired(message="Please Select an availability for the pet.")], coerce=lambda x: x == 'True')

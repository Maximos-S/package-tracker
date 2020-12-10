from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from map.map import map

cities = [(city, city) for city in map.keys()]
print(cities)

class ShippingForm(FlaskForm):
    sender_name = StringField("Sender Name", validators=[DataRequired()])
    recipient_name = StringField("Recipient",  validators=[DataRequired()])
    origin = SelectField("Origin", choices=cities,  validators=[DataRequired()])
    destination = SelectField("Destination", choices=cities,  validators=[DataRequired()])
    submit = SubmitField('Ship It!')
    shipping = BooleanField("Shipping", validators=[DataRequired()])

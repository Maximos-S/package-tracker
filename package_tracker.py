from flask import Flask, render_template
from app.config import Configuration
from app.shipping_form import ShippingForm
from app.models import db, Package
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)
Migrate(app, db)


@app.route("/")
def root():
    return "<h1>Package Tracker</h1>"


@app.route("/new_package", methods=['GET', "POST"])
def new_package():
    form = ShippingForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('shipping_request.html', form=form)

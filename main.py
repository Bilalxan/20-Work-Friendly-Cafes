from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from form import AddForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config["SECRET_KEY"] = "somethinglike"
Bootstrap5(app)
db = SQLAlchemy()
db.init_app(app)
csrf = CSRFProtect(app)

# Cafe Table Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=True)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=True)
    has_toilet = db.Column(db.Boolean(), nullable=False)
    has_wifi = db.Column(db.Boolean(), nullable=False)
    has_sockets = db.Column(db.Boolean(), nullable=False)
    can_take_calls = db.Column(db.Boolean(), nullable=True)
    coffee_price = db.Column(db.String(250), nullable=True)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")
@app.route("/cafe_list")
def cafe_list():
    cafes = db.session.execute(db.select(Cafe).order_by(Cafe.id)).scalars().all()
    return render_template("cafes.html", cafes=cafes)

@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = AddForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.name.data,
            location=form.location.data,
            map_url=form.map_url.data,
            has_toilet=bool(int(form.toilet.data)),
            has_wifi=bool(int(form.wifi.data)),
            has_sockets=bool(int(form.socket.data)),
            coffee_price=bool(int(form.toilet.data)),
            seats=bool(int(form.wifi.data)),
            can_take_calls=bool(int(form.socket.data)),
            img_url=form.map_url.data
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for("cafe_list"))
    return render_template("add.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)

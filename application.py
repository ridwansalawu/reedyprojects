from datetime import date, time, datetime, timedelta
from flask import Flask, url_for, request, render_template, session, redirect
from models import db, User
from forms import SignupForm, LoginForm
import data_list



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://localhost/staff'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
app.secret_key = "development-key"

@app.route('/', methods=["POST", "GET"])
def index():
    current_time = datetime.now().strftime("%H:%M:%S")
    
    current_date =  date.today()
    return render_template("index.html", current_time = current_time, current_date = current_date)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if "email" in session:
        return redirect(url_for("home"))
    form = SignupForm()

    if request.method == "POST":
        if form.validate() == False:
            return render_template('signup.html', form = form)
        else:
            newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()

            session['email'] = newuser.email


            return redirect(url_for('home'))

    elif request.method =="GET":
        return render_template("signup.html", form = form)

@app.route("/login", methods= ["GET", "POST"])
def login():
    if "email" in session:
        return redirect(url_for("home"))
    form = LoginForm()

    if request.method == "POST":
        if form.validate() == False:
            return render_template("login.html", form=form)
        else:
            email = form.email.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()
            if user is not None and user.check_password(password):
                session["email"] = form.email.data
                return redirect(url_for("home"))
            else:
                return redirect(url_for("login"))


    elif request.method == "GET":
        return render_template("login.html", form = form)


@app.route("/logout")
def logout():
    session.pop("email", None)
    return redirect(url_for("index"))


@app.route("/admin")
def admin():
    
    return render_template("admin.html")






@app.route("/home")
def home():
    if "email" not in session:
        return redirect(url_for("login"))
    return render_template("home.html")

   
def main():
    db.create_all()
    app.run(debug=True)
    data_list.list_data()


if __name__ == "__main__":
    with app.app_context():
        main()

    # app.run(debug=True)




# @app.route("/user/<username>")
# def user_profile(self, parameter_list):
#     pass
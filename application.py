from datetime import date, time, datetime, timedelta
from flask import Flask, url_for, request, render_template, session, redirect
from models import db, User, Asset
from forms import SignupForm, LoginForm, SearchAsset
import data_list
import calendar
import pandas as pd


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
            return render_template("login.html", form = form)
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


@app.route("/admin", methods=["GET", "POST"])
def admin():
    # xyz = pd.read_excel("ryd61update.xlsx")
    # # xyz = pd.read_csv("flax.csv")
    # xyz = xyz.to_html
    





    # p = [1,2,3,4,5]

    f = Asset.query.filter(Asset.asset_address.contains("CRANDON")).first()
    

    return render_template("admin.html", f = f)


    # s_list = []
    # s_list.append(f)
   

    # if len(s_list) < 2:
    #     z= s_list[0]
    #     q = len(s_list)
    #     return render_template("admin.html", z = z , q = q)
    # else:

    



    
    
        # return render_template("admin.html", p = p)
    
# @app.route("/find_asset", methods=["GET", "POST"])
# def find_asset():
#     #get information from form
#     asset_name = request.form.get("asset_name")
#     try:
#         pass
#     except expression as identifier:
#         pass


@app.route("/home", methods= ["GET", "POST"])
def home():
    if "email" not in session:
        return redirect(url_for("login"))
    else:
    
    
    # form = SearchAsset()

    # if form.validate() == False:
    #     return render_template("home.html", form = form)
    # else:
    #     asset_id = form.asset.data
        
        

    #     find_asset = Asset.query.filter_by(asset_id = asset_id).first()
    #     # if find_asset is not None:
        return render_template("home.html")
        # else:
        #     return render_template("home.html")






    

   
def main():
    db.create_all()
    app.run(debug=True)
    # data_list.list_data()
    # data_list.select_list()


if __name__ == "__main__":
    with app.app_context():
        main()

    # app.run(debug=True)




# @app.route("/user/<username>")
# def user_profile(self, parameter_list):
#     pass
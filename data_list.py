from flask_sqlalchemy  import SQLAlchemy
import csv
import os

from flask import Flask, url_for, request, render_template, session, redirect
from models import db, User, Asset
from forms import SignupForm, LoginForm



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://localhost/staff'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


def list_data():
  f = open("flax.csv")
  reader = csv.reader(f)
  for  asset_address, asset_id, asset_cpp in reader:
    asset = Asset(asset_address = asset_address, asset_id = asset_id,  asset_cpp = asset_cpp )
    db.session.add(asset)
    print(f"Asset_ID = {asset_id} \n Asset location = {asset_address} \n Control plan page = {asset_cpp}")
    db.session.commit()

# if __name__ == "__main__":
#     with app.app_context():
#         main()
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Enum

import csv
import os

# import geocoder
# import urllib3
# import json

db = SQLAlchemy()

def main():
  f = open("flax.csv")
  reader = csv.reader(f)
  for assetid, add, cp in reader:
    asset = Asset(asset_id = assetid, asset_address = add, asset_cpp =cp )
    db.session.add(asset)
    print(f"Asset_ID = {asset_id} \n Asset location = {asset_address} \n Control plan page = {asset_cpp}")
    db.session.commit()



class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  #level= 
  email = db.Column(db.String(120), unique=True)
  pwdhash = db.Column(db.String(54))

  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)
     
  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)


class Asset(db.Model):
  __tablename__="assets"
  asset_no = db.Column(db.Integer, autoincrement=True, primary_key=True)
  asset_id = db.Column(db.String)
  asset_address = db.Column(db.String(100))
  asset_cpp = db.Column(db.String(100)) #construction plan page
  # asset_size_before = db.Column(db.String(100))
  # asset_size_after = db.Column(db.String(100))
  # asset_mould= db.Column(db.String(100))     #nature of pit before upgrade
  # asset_status = db.Column(db.String(100)) # complete, incomplete, partial completion
  # asset_payment= db.Column(db.String(100)) # paid, pending
  # asset_others = db.Column(db.String(100))
  # pit_id = db.Column(db.String(10))
  

  # def __init__(self, asset_id, asset_address, asset_mould, asset_size_before,pit_id):
  #   self.asset_id = asset_id
  #   self.asset_address = asset_address
  #   self.asset_mould = asset_mould
  #   self.asset_size_before = asset_size_before
  #   self.pit_id = pit_id

  # def asset_detail():
  #   print(f"Asset_ID = {asset_id} \n" f"Asset location = {asset_address}")


# class Wage(db.Model):
#   __tablename__= "wages"
#   pass








# p = Place()
# places = p.query("1600 Amphitheater Parkway Mountain View CA")
# class Place(object):
#   def meters_to_walking_time(self, meters):
#     # 80 meters is one minute walking time
#     return int(meters / 80)  

#   def wiki_path(self, slug):
#     return urllib2.urlparse.urljoin("http://en.wikipedia.org/wiki/", slug.replace(' ', '_'))
  
#   def address_to_latlng(self, address):
#     g = geocoder.google(address)
#     return (g.lat, g.lng)

#   def query(self, address):
#     lat, lng = self.address_to_latlng(address)
    
#     query_url = 'https://en.wikipedia.org/w/api.php?action=query&list=geosearch&gsradius=5000&gscoord={0}%7C{1}&gslimit=20&format=json'.format(lat, lng)
#     g = urllib2.urlopen(query_url)
#     results = g.read()
#     g.close()

#     data = json.loads(results)
    
#     places = []
#     for place in data['query']['geosearch']:
#       name = place['title']
#       meters = place['dist']
#       lat = place['lat']
#       lng = place['lon']

#       wiki_url = self.wiki_path(name)
#       walking_time = self.meters_to_walking_time(meters)

#       d = {
#         'name': name,
#         'url': wiki_url,
#         'time': walking_time,
#         'lat': lat,
#         'lng': lng
#       }

#       places.append(d)

#     return places

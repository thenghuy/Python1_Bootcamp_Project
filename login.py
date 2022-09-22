from pymongo import MongoClient
from weather import dashborad
from weather import my_Weather
from weather import add_favorite
client=MongoClient("mongodb://localhost:27017")
db=client["weather_app"]
collection=db["Login_info"]
def login_user():
 name=input("ENter name")
 password=input("ENter name")
 name_list=[]
 pass_list=[]
 for i in collection.find():
    name_list.append(i['name'])
    pass_list.append(i['password'])
 if (name in name_list) and (password in pass_list):
       dashborad()
       my_Weather()
       add_favorite()
 else:
       print(False)


from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017")
db=client["weather_app"]
collection=db["Login_info"]
def signup():
 name_list=[]
 for i in collection.find():
    name_list.append(i['name'])
 while True:
   name=input("ENter name:")
   password=input("ENter password:")
   confirm_password=input("Re-enter your password:")
   if confirm_password==password and name not in name_list:
      record1={"name":name,"password":password}
      add1 = collection.insert_one(record1)
      print("Account created!")
      break
   elif name in name_list:
       print("Name exist please insert again")
   elif password!=confirm_password:
       print("Password doesnt match enter the new one!")
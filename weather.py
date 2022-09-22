from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017")
db=client["weather_app"]
collection=db["weather_info"]
location=[]
temperature=[]
air_qualitity=[]
weather=[]
for i in collection.find():
    location.append(i['Location'])
    temperature.append(i['temperature'])
    air_qualitity.append(i['Air quality'])
    weather.append(i['Weather'])
def dashborad():
 for i in range(len(location)):
    print(f"+Location:'{location[i]}'\n",
          f"Temperature:{temperature[i]}\n",
          f"Air quality:{air_qualitity[i]}\n",
          f"Weather:{weather[i]}")
def my_Weather():
  while True:
    Find_location=input("Enter your place here or Enter [quit] to stop:")
    for i in range(len(location)):
        if Find_location==location[i]:
          print(f"+Location:'{location[i]}'\n",
                f"Temperature:{temperature[i]}\n",
                f"Air quality:{air_qualitity[i]}\n",
                f"Weather:{weather[i]}")
    if Find_location=="quit":
        break
collection1=db["favo_weather"]
def add_favorite():
 while True:
    fav_location=input("What location you want to add to your favorite?: Insert here:")
    if fav_location in  location:
       for i in collection.find({"Location": f"{fav_location}"}):
           x=collection1.insert_one(i)
    elif fav_location=="quit":
        break
    else:
        print("Invalid location ")
        print("Re enter your location or [quit] to quit")


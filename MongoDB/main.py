from pprint import pprint
from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())

MONGO_PWD = os.environ.get("MONGODB_PWD")

conn_string = f"mongodb+srv://thor:{MONGO_PWD}@basedb.rus3x.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(conn_string)

dbs = client.list_database_names()  # list contained DBS
basedb = client.BaseDB  # access to a single DB
collections = basedb.list_collection_names()  # list collection names

#print(collections)


def insert_doc():  # add 1 single document with meth: insert_one()**
      collection = basedb.Base
      test_document = {
            "name": "Leo",
            "Surname": "Zamba",
            "Sport": "Gym"
      }
      insert_doc = collection.insert_one(test_document).inserted_id
      print(insert_doc)  # -> 627235b4ab4ddaa5afe0b3cf BSON OBJECT

#insert_doc()


# creates a database in case (production) in case the DATABASE does not exhist yet
production = client.production
# creates a collection in case (person_collection) does not exhist yet
person_collection = production.person_collection


def create_docs():  # add multiple documents with meth:
      first_names = ["TIm", "Leo", "Sara", "Lisa", "Denny", "Thor"]
      surnames = ["Kick", "Zam", "Reg", "Mart", "Zam"]
      ages = [12, 24, 21, 22, 4]
      
      docs = []

      for first_names, surnames, ages in zip(first_names, surnames, ages):
            doc = {"first_name": first_names, "last_name": surnames, "age": ages}
            docs.append(doc)
            #person_collection.inset_one(doc)
      
      person_collection.insert_many(docs)

#create_docs()


# ---------------------------------------------------------------------------------------------
# Series of Queries

printer = pprint.PrettyPrinter()

def find_all_people():
      people = person_collection.find()
      
      for person in people:
            printer.pprint(person)

#find_all_people()


def find_leo():
      leo = person_collection.find_one({"first_name": "Leo"})
      printer.pprint(leo)

#find_leo()

def count_all_people():
      count = person_collection.count_documents(filter={})
      print(count)
      
#count_all_people()

def get_by_id(person_id):
      from bson.objectid import ObjectId
      
      _id = ObjectId(person_id)
      person = person_collection.find_one({"_id": _id})
      printer.pprint(person)
      
#get_by_id("6272392ec561707f83ea0686")


def get_age_range(min_age, max_age):
      query = {"$and": [
                  {"age": {"$gte": min_age}},
                  {"age": {"$lte": max_age}}
            ]}
      
      people = person_collection.find(query).sort("age")
      for person in people:
            printer.pprint(person)
      
#get_age_range(1, 22)

def project_columns():
      columns = {"_id": 0, "first_name": 1, "last_name":1}
      people = person_collection.find({}, columns)
      for person in people:
            printer.pprint(person)
            
#project_columns()

def update_person_by_id(person_id):
      from bson.objectid import ObjectId
      
      _id = ObjectId(person_id)

      all_updates = {
            "$set": {"new_field": True},
            "$inc": {"age": 1},
            "$rename": {"first_name": "first", "last_name": "last"}
      }
      person_collection.update_one({"id": _id}, all_updates)

#update_person_by_id("6272392ec561707f83ea0685")


def update_person_by_id2(person_id):
      from bson.objectid import ObjectId
      
      _id = ObjectId(person_id)

      person_collection.update_one({"id": _id}, {"$unset": {"new_field": ""}})

#update_person_by_id2("6272392ec561707f83ea0685")


def replace_one(person_id):
      from bson.objectid import ObjectId
      _id = ObjectId(person_id)

      new_doc = {
            "first_name": "new first name",
            "last_name": "new last name",
            "age": 100
      }
      person_collection.replace_one({"id": _id}, new_doc)

#replace_one("6272392ec561707f83ea0685")

def delete_doc_by_id(person_id):
      from bson.objectid import ObjectId
      _id = ObjectId(person_id)
      person_collection.delete_one(({"_id": _id}))

#delete_doc_by_id("6272392ec561707f83ea0685")





#-------------------RELATIONSHIPS---------------------------#

address = {
      "_id": "6272392ec561707f83ea0685",
      "street": "via le mani",
      "number": 69,
      "city": "ulo",
      "country": "Ita",
      "zip": 566464
}

person = {
      "_id": "3783783847874vekvbks",
      "first_name": "Luca",
      "address": address
}

person_add = {
      "_id": "3783783847874vekvbks",
      "first_name": "Luca",
      "address":{
      "_id": "6272392ec561707f83ea0685",
      "street": "via le mani",
      "number": 69,
      "city": "ulo",
      "country": "Ita",
      "zip": 566464
      }
}

### OR ###
addresss = {
      "_id": "6272392ec561707f83ea0685",
      "street": "via le mani",
      "number": 69,
      "city": "ulo",
      "country": "Ita",
      "zip": 566464,
      "owner_d": "3783783847874vekvbks"
}


# Method 1
def add_address_embed(person_id, address):
      from bson.objectid import ObjectId
      _id = ObjectId(person_id)

      person_collection.update_one({"_id": _id}, {"$addToSet": {'addresses': address}})

#add_address_embed("6272392ec561707f83ea0686", address)


# Method 2
def add_address_relationship(person_id, address):
      from bson.objectid import ObjectId
      _id = ObjectId(person_id)
      
      address = address.copy()
      address["owner_id"] = person_id
      
      address_collection = production.address #add collection address
      address_collection.insert_one((address))

#add_address_relationship("6272392ec561707f83ea0688", address)



import anvil.files
from anvil.files import data_files
import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
import json
import numpy as np
import pickle

@anvil.server.callable
def add_contact_info(name, email, topic, question):
  app_tables.contact.add_row(name=name, email=email, topic=topic, question=question, time=datetime.now())
  anvil.email.send(from_name="Contact Form", 
                   subject="New Web Contact",
                   text=f"New web contact from {name} ({email})\nTopic: {topic}\nComment/Question: {question}")

@anvil.server.callable
def add_ecommerce_info(super_category, main_category, sub_category1, sub_category2, brand, product_name, discounted_price, email):
  app_tables.ecommerce.add_row(super_category=super_category, main_category=main_category, sub_category1=sub_category1, sub_category2=sub_category2, brand = brand, product_name = product_name,discounted_price = discounted_price, email = email,time=datetime.now())
  anvil.email.send(from_name="ICT Ignite", 
                   to = email,
                   subject="New Ecommerce return inquery ",
                   text=f"Ecommerce return inquery\n {main_category} ({super_category})\nbrand: {brand}\n Product name: {product_name}\nPrice: {discounted_price}")

__super_category = None
__data_columns = None
__main_category = None
__model = None
__product_name = None
__sub_category1 = None
__sub_category2 = None
__brand = None

@anvil.server.callable
def category_prediction(super_category, main_category, sub_category1, sub_category2, brand, product_name, discounted_price):
    try:
        loc_index = __data_columns.index(super_category.lower())
    except:
        loc_index = -1
    # print(__main_category)
    x = np.zeros(13)
    x[0] = __product_name[product_name]
    x[1] = __main_category[main_category]
    x[2] = __sub_category1[sub_category1]
    x[3] = __sub_category2[sub_category2]
    x[4] = __brand[brand]
    x[5] = discounted_price

    x[5] = discounted_price
    if loc_index >= 6:
        x[loc_index] = 1
        print(x)
        print(__model.predict([x]))

        if __model.predict([x])[0] == 1:
            result = "There are high changes that customer will return this product."
        else:
            result = "There are less changes that customer will return this product."

    return result

@anvil.server.callable
def load_saved_artefacts():
    print("loading saved artefacts...start")
    global __data_columns
    global __super_category
    global __main_category
    global __product_name
    global __sub_category1
    global __sub_category2
    global __brand

    with open(data_files["columns.json"], "r") as f:
      __data_columns = json.load(f)['data_columns']
      __super_category = __data_columns[6:]

    with open(data_files["main_category_frequency_encoding.json"], "r") as f:
      __main_category = json.load(f)

    with open(data_files["product_name_frequency_encoding.json"], "r") as f:
       __product_name = json.load(f)

    with open(data_files["sub_category1_frequency_encoding.json"], "r") as f:
       __sub_category1 = json.load(f)

    with open(data_files["sub_category2_frequency_encoding.json"], "r") as f:
       __sub_category2 = json.load(f)

    with open(data_files["brand_frequency_encoding.json"], "r") as f:
       __brand = json.load(f)

    print("loading saved artefacts...done")

    global __model
    if __model is None:
        with open(data_files["capstone_model.pkl"], 'rb') as f:
           __model = pickle.load(f)
    print("loading saved artefacts...done")

@anvil.server.callable
def predict(super_category, main_category, sub_category1, sub_category2, brand, product_name, discounted_price):
  load_saved_artefacts()
  prediction = category_prediction(super_category, main_category, sub_category1, sub_category2, brand, product_name, discounted_price)
  return prediction

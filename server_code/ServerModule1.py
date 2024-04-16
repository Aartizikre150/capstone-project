import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime


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
                   subject="New Ecommerce return inquery ",
                   text=f"Ecommerce return inquery\n {main_category} ({super_category})\nbrand: {brand}\n Product name: {product_name}\nPrice: {discounted_price}")
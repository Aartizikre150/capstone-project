from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

# Define the mapping of super_category options to primary_category options
category_mapping = {
    'Fashion': ['Bags, Wallets & Belts ', 'Clothing ', 'Jewellery ', 'Footwear ','Eyewear '],
    'Furniture': ['Home Decor & Festive Needs ', 'Home Furnishing ','Kitchen & Dining ', 'Home Improvement ', 'Household Supplies ',    'Furniture ', 'Home & Kitchen '],
    'Beauty, Health, Personal & Household Care': ['Baby Care ', 'Health & Personal Care Appliances ','Beauty and Personal Care ', 'Pet Supplies ', 'Food & Nutrition '],
    'Toys, Hobby & DIY': ['Toys & School Supplies ', 'Sports & Fitness ','Pens & Stationery ', 'Tools & Hardware ', 'Gaming '],
    'Electronics': ['Mobiles & Accessories ', 'Watches ', 'Computers ','Cameras & Accessories ', 'Wearable Smart Devices '],
    'Automotive': ['Automotive'],
    'Media': ['eBooks ', 'Home Entertainment ']
}

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Populate primary category dropdown
    #self.super_category.items = ['Fashion', 'Furniture', 'Beauty, Health, Personal & Household Care', 'Toys, Hobby & DIY', 'Electronics', 'Automotive', 'Media']
    #self.repeating_panel_1.items = app_tables.pricing.search()

    # Any code you write here will run when the form opens.

  def lets_begin_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    open_form(card_3)
    #self.content_panel.get_components()
    #self.content_panel.add_component(self.card_3, full_width_row=True)
  
  def super_category_change(sender, **event_args):
    
    

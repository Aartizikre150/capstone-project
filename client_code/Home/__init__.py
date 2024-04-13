from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables



class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #self.repeating_panel_1.items = app_tables.pricing.search()

    # Any code you write here will run when the form opens.

  def lets_begin_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    open_form(card_3)
    #self.content_panel.get_components()
    #self.content_panel.add_component(self.card_3, full_width_row=True)
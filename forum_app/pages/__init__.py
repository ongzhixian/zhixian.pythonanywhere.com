################################################################################
# Define package composition
################################################################################

__all__ = [
    "root", "mysql", "test", "authentication", "database", "user", 
    "feature", "shared_data", "markdown_service", "basic_art", 
    "dice", "note",
    "client", "portfolio", "trade"]

# Page UI Components

class menu(object):

    def __init__(self, menu_name, register=False):
        self.menu_name = menu_name
        self.menu_items = {}
        if register and menu_name not in menu.registered_menus:
            menu.registered_menus[menu_name] = self
        
    def add_menu_item(self, menu_item_id, display_text, href=None, is_disabled=False, icon_name=None):
        if menu_item_id in self.menu_items:
            return
        self.menu_items[menu_item_id] = menu_item(menu_item_id, display_text, href, is_disabled, icon_name)

    def remove_menu_item(self, menu_item_id):
        if menu_item_id not in self.menu_items:
            return
        del self.menu_items[menu_item_id]

    # Class variables and methods
    
    registered_menus = {} # Tracks all application registered menus

    # def add_to_menu(menu_name, menu_item_id, display_text, href=None, is_disabled=False, icon_name=None):
    #     if 'menu' not in app_state or menu_name not in app_state['menu']:
    #         return
    #     menu = app_state['menu'][menu_name]
    #     menu.add(menu_item_id, display_text, href, is_disabled, icon_name)

    # def unregister_menu(menu_name):
    #     if menu_name not in menu.registered_menus:
    #         return 
    #     del menu.registered_menus[menu_name]


class menu_item(object):
    def __init__(self, menu_item_id, display_text, href=None, is_disabled=False, icon_name=None):
        self.menu_item_id = menu_item_id
        self.display_text = display_text
        self.is_disabled = is_disabled
        self.href = href 
        self.icon_name = icon_name 
        
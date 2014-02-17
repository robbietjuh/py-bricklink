'''
    bricklink.methods
    --------------------

    A module providing Bricklink API Method implementations
'''


from exceptions import BricklinkInvalidParameterException


class Method:
    client = None

    def __init__(self, client):
        self.client = client


class Orders(Method):
    URL_ORDER_LIST = 'orders'
    URL_ORDER_DETAILS = 'orders/{order_id}'
    URL_ORDER_ITEMS = 'orders/{order_id}/items'
    URL_ORDER_MESSAGES = 'orders/{order_id}/messages'
    URL_ORDER_FEEDBACK = 'orders/{order_id}/feedback'
    URL_ORDER_UPDATE = 'orders/{order_id}'
    URL_ORDER_UPDATE_STATUS = 'order/{order_id}/status'


class Inventory(Method):
    URL_INVENTORY_LIST = 'inventories'
    URL_INVENTORY_DETAILS = 'inventories/{inventory_id}'
    URL_INVENTORY_CREATE = 'inventories'
    URL_INVENTORY_CREATE_BULK = 'inventories'
    URL_INVENTORY_UPDATE = 'inventories/{inventory_id}'
    URL_INVENTORY_DELETE = 'inventories/{inventory_id}'


class Catalog(Method):
    URL_CATALOG_ITEM = 'items/{type}/{no}'
    URL_CATALOG_SUPERSETS = 'items/{type}/{no}/supersets'
    URL_CATALOG_SUBSETS = 'items/{type}/{no}/subsets'
    URL_CATELOG_PRICE_GUIDE = 'items/{type}/{no}/price'


class Feedback(Method):
    URL_FEEDBACK_LIST = 'feedback'
    URL_FEEDBACK_DETAILS = 'feedback/{feedback_id}'
    URL_FEEDBACK_CREATE = 'feedback'
    URL_FEEDBACK_REPLY = 'feedback/{feedback_id}/reply'


class Color(Method):
    URL_COLOR_LIST = 'colors'
    URL_COLOR_DETAIL = 'colors/{color_id}'


class Category(Method):
    pass


class PushNotification(Method):
    pass
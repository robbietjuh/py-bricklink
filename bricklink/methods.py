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
    pass


class Feedback(Method):
    pass


class Color(Method):
    pass


class Category(Method):
    pass


class PushNotification(Method):
    pass
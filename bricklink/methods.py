'''
    bricklink.methods
    --------------------

    A module providing Bricklink API Method implementations
'''


class Method:
    client = None

    def __init__(self, client):
        self.client = client


class Orders(Method):
    pass


class Inventory(Method):
    pass


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
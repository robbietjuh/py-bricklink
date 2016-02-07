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
    URL_ORDER_UPDATE_STATUS = 'orders/{order_id}/status'
    URL_ORDER_UPDATE_PAYMENT_STATUS = 'orders/{order_id}/status'

    def getOrders(self, direction='in', status='', filed=False):
        params = {
            'direction':    direction,
            'status':       status,
            'filed':        filed,
            }
        return self.client.get(self.URL_ORDER_LIST, params)

    def getOrder(self, order_id):
        return self.client.get(self.URL_ORDER_DETAILS.format(order_id=order_id))

    def getOrderItems(self, order_id):
        return self.client.get(self.URL_ORDER_ITEMS.format(order_id=order_id))

    def getOrderMessages(self, order_id):
        return self.client.get(self.URL_ORDER_MESSAGES.format(order_id=order_id))

    def getOrderFeedback(self, order_id):
        return self.client.get(self.URL_ORDER_FEEDBACK.format(order_id=order_id))

    def updateOrder(self, order_id, order_resource):
        params = order_resource
        return self.client.put(self.URL_ORDER_UPDATE.format(order_id=order_id), params)

    def updateOrderStatus(self, order_id, status):
        ORDER_STATUSES = ('PENDING', 'UPDATED',
                          'PROCESSING', 'READY', 'PAID', 'PACKED', 'SHIPPED', 'RECEIVED', 'COMPLETED',
                          'OCR', 'NPB', 'NPX', 'NRS', 'NSS', 'CANCELLED',)

        if not status in ORDER_STATUSES:
            raise BricklinkInvalidParameterException('Invalid status. Should be one of {0}'.format(str(ORDER_STATUSES)),
                                                     status)

        params = {
            'field':        'status',
            'value':        status
        }

        return self.client.put(self.URL_ORDER_UPDATE_STATUS.format(order_id=order_id), params)

    def updateOrderPaymentStatus(self, order_id, status):
        ORDER_PAYMENT_STATUSES = ('None', 'Sent', 'Received', 'Clearing', 'Returned', 'Bounced', 'Completed',)

        if not status in ORDER_PAYMENT_STATUSES:
            raise BricklinkInvalidParameterException('Invalid status. Should be one of {0}'.
                                                     format(str(ORDER_PAYMENT_STATUSES)),
                                                     status)

        params = {
            'field':        'payment_status',
            'value':        status
        }

        return self.client.put(self.URL_ORDER_UPDATE_PAYMENT_STATUS.format(order_id=order_id), params)



class Inventory(Method):
    URL_INVENTORY_LIST = 'inventories'
    URL_INVENTORY_DETAILS = 'inventories/{inventory_id}'
    URL_INVENTORY_CREATE = 'inventories'
    URL_INVENTORY_UPDATE = 'inventories/{inventory_id}'
    URL_INVENTORY_DELETE = 'inventories/{inventory_id}'

    def getInventories(self):
        return self.client.get(self.URL_INVENTORY_LIST)

    def getInventory(self, inventory_id):
        return self.client.get(self.URL_INVENTORY_DETAILS.format(inventory_id=inventory_id))

    def createInventory(self, inventory_resource):
        params = inventory_resource
        return self.client.post(self.URL_INVENTORY_CREATE, params)

    def updateInventory(self, inventory_id, inventory_resource):
        params = inventory_resource
        return self.client.put(self.URL_INVENTORY_UPDATE.format(inventory_id=inventory_id), params)

    def deleteInventory(self, inventory_id):
        return self.client.delete(self.URL_INVENTORY_DELETE.format(inventory_id=inventory_id))


class Catalog(Method):
    URL_CATALOG_ITEM = 'items/{type}/{no}'
    URL_CATALOG_ITEM_IMAGE = 'items/{type}/{no}/images/{color_id}'
    URL_CATALOG_SUPERSETS = 'items/{type}/{no}/supersets'
    URL_CATALOG_SUBSETS = 'items/{type}/{no}/subsets'
    URL_CATALOG_PRICE_GUIDE = 'items/{type}/{no}/price'
    URL_CATALOG_COLORS = 'items/{type}/{no}/colors'

    def getItem(self, item_type='PART', item_no=''):
        ITEM_TYPES = ('MINIFIG', 'PART', 'SET', 'BOOK', 'GEAR', 'CATALOG', 'INSTRUCTION',
                      'UNSORTED_LOT', 'ORIGINAL_BOX')

        if not item_type in ITEM_TYPES:
            raise BricklinkInvalidParameterException('Invalid item type. Should be one of {0}'.format(str(ITEM_TYPES)),
                                                     item_type)

        return self.client.get(self.URL_CATALOG_ITEM.format(type=item_type, no=item_no))

    def getItemImage(self, item_type='PART', item_no='', color_id=None):
        ITEM_TYPES = ('MINIFIG', 'PART', 'SET', 'BOOK', 'GEAR', 'CATALOG', 'INSTRUCTION',
                      'UNSORTED_LOT', 'ORIGINAL_BOX')

        if not item_type in ITEM_TYPES:
            raise BricklinkInvalidParameterException('Invalid item type. Should be one of {0}'.format(str(ITEM_TYPES)),
                                                     item_type)

        return self.client.get(self.URL_CATALOG_ITEM_IMAGE.format(type=item_type, no=item_no, color_id=color_id))

    def getSupersets(self, item_type='PART', item_no='', color_id=None):
        ITEM_TYPES = ('MINIFIG', 'PART', 'SET', 'BOOK', 'GEAR', 'CATALOG', 'INSTRUCTION',
                      'UNSORTED_LOT', 'ORIGINAL_BOX')

        if not item_type in ITEM_TYPES:
            raise BricklinkInvalidParameterException('Invalid item type. Should be one of {0}'.format(str(ITEM_TYPES)),
                                                     item_type)

        params = {
            'color_id': color_id
            }

        return self.client.get(self.URL_CATALOG_SUPERSETS.format(type=item_type, no=item_no), params)

    def getSubsets(self, item_type='PART', item_no='', color_id=None, box=None, instruction=None,
                         break_minifigs=None, break_subsets=None):
        ITEM_TYPES = ('MINIFIG', 'PART', 'SET', 'BOOK', 'GEAR', 'CATALOG', 'INSTRUCTION',
                      'UNSORTED_LOT', 'ORIGINAL_BOX')

        if not item_type in ITEM_TYPES:
            raise BricklinkInvalidParameterException('Invalid item type. Should be one of {0}'.format(str(ITEM_TYPES)),
                                                     item_type)

        params = {
            # 'color_id': color_id,
            # 'box': box,
            # 'instruction': instruction,
            # 'break_minifigs': break_minifigs,
            # 'break_subsets': break_subsets
        }

        return self.client.get(self.URL_CATALOG_SUBSETS.format(type=item_type, no=item_no), params)

    def getPriceGuide(self, item_type='PART', item_no='', color_id=None, guide_type=None, new_or_used=None, vat=False):
        ITEM_TYPES = ('MINIFIG', 'PART', 'SET', 'BOOK', 'GEAR', 'CATALOG', 'INSTRUCTION',
                      'UNSORTED_LOT', 'ORIGINAL_BOX')

        if not item_type in ITEM_TYPES:
            raise BricklinkInvalidParameterException('Invalid item type. Should be one of {0}'.format(str(ITEM_TYPES)),
                                                     item_type)

        params = {
            'guide_type': guide_type,
            'new_or_used': new_or_used,
            'vat': 'Y' if vat else 'N'
        }

        if color_id is not None:
            params['color_id'] = color_id

        return self.client.get(self.URL_CATALOG_PRICE_GUIDE.format(type=item_type, no=item_no), params)

    def getKnownColors(self, item_type='PART', item_no=''):
        ITEM_TYPES = ('MINIFIG', 'PART', 'SET', 'BOOK', 'GEAR', 'CATALOG', 'INSTRUCTION',
                      'UNSORTED_LOT', 'ORIGINAL_BOX')

        if not item_type in ITEM_TYPES:
            raise BricklinkInvalidParameterException('Invalid item type. Should be one of {0}'.format(str(ITEM_TYPES)),
                                                     item_type)

        return self.client.get(self.URL_CATALOG_COLORS.format(type=item_type, no=item_no))


class Feedback(Method):
    URL_FEEDBACK_LIST = 'feedback'
    URL_FEEDBACK_DETAILS = 'feedback/{feedback_id}'
    URL_FEEDBACK_CREATE = 'feedback'
    URL_FEEDBACK_REPLY = 'feedback/{feedback_id}/reply'

    def getFeedbacks(self):
        return self.client.get(self.URL_FEEDBACK_LIST)

    def getFeedbackDetails(self, feedback_id):
        return self.client.get(self.URL_FEEDBACK_DETAILS.format(feedback_id=feedback_id))

    def createFeedback(self, order_id, rating, comment):
        if rating < 0 or rating > 2:
            raise BricklinkInvalidParameterException('Invalid rating. Should be between 0 and 2.')

        params = {
            'order_id': order_id,
            'rating': rating,
            'comment': comment
        }

        return self.client.post(self.URL_FEEDBACK_CREATE, params)

    def createFeedbackReply(self, feedback_id):
        raise Exception('Not yet implemented')


class Color(Method):
    URL_COLOR_LIST = 'colors'
    URL_COLOR_DETAIL = 'colors/{color_id}'

    def getColors(self):
        return self.client.get(self.URL_COLOR_LIST)

    def getColorDetail(self, color_id):
        return self.client.get(self.URL_COLOR_DETAIL.format(color_id=color_id))


class Category(Method):
    URL_CATEGORY_LIST = 'categories'
    URL_CATEGORY_DETAIL = 'categories/{category_id}'

    def getCategories(self):
        return self.client.get(self.URL_CATEGORY_LIST)

    def getCategoryDetail(self, category_id):
        return self.client.get(self.URL_CATEGORY_DETAIL.format(category_id=category_id))


class PushNotification(Method):
    URL_NOTIFICATION_LIST = 'notifications'

    def getNotifications(self):
        return self.client.get(self.URL_NOTIFICATION_LIST)


class Member(Method):
    URL_RATINGS = 'members/{username}/ratings'
    URL_NOTE = 'members/{username}/notes'
    URL_NOTE_CREATE = 'members/{username}/notes'
    URL_NOTE_UPDATE = 'members/{username}/notes'
    URL_NOTE_DELETE = 'members/{username}/notes'

    def getRatings(self, username):
        return self.client.get(self.URL_RATINGS.format(username=username))

    def getNote(self, username):
        return self.client.get(self.URL_NOTE.format(username=username))

    def createNote(self, username, note_resource):
        if not 'note_text' in note_resource:
            raise BricklinkInvalidParameterException('Invalid note resource. Should at least contain note_text')

        return self.client.post(self.URL_NOTE_CREATE.format(username=username))

    def updateNote(self, username, note_resource):
        if not 'note_text' in note_resource:
            raise BricklinkInvalidParameterException('Invalid note resource. Should at least contain note_text')

        return self.client.put(self.URL_NOTE_UPDATE.format(username=username), note_resource)

    def deleteNote(self, username):
        return self.client.delete(self.URL_NOTE_DELETE.format(username=username))

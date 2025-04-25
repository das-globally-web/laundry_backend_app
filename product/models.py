from mongoengine import Document, StringField, DictField, FloatField, ListField

class ProductTable(Document):
    title = StringField(required=True)
    image = StringField(required=True)
    price_json = ListField(DictField(), required=True)
from mongoengine import Document, StringField, FloatField

class ServiceTable(Document):
    banner_image = StringField(required=True)
    icon_image = StringField(required=True)
    title = StringField(required=True)
    rating = FloatField(required=True)
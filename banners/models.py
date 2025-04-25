from mongoengine import Document, StringField

class BannerTable(Document):
    image = StringField(required=True)
    
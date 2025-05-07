from mongoengine import Document, StringField

class BlogCategory(Document):
    title = StringField(required=True)
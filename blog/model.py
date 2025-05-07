from mongoengine import Document, StringField

class BlogsTable(Document):
    categoryId = StringField(required=True)
    title = StringField(required=True)
    content = StringField(required=True)
    created_date = StringField(required=True)
    image = StringField(required=True)
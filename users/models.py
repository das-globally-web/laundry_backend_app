from mongoengine import Document, StringField, FloatField, EmailField, BooleanField, DictField, ListField

class User(Document):
    name = StringField(required=True)
    phone_number = StringField(required=True, unique=True)
    country_code = StringField(required=True)
    current_address = StringField()
    profile_pic_url = StringField()
    staff = BooleanField(default=False)
    
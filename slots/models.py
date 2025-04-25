from mongoengine import Document, StringField, BooleanField

class SlotTable(Document):
    startTime = StringField(required=True)
    endtime = StringField(required=True)
    pickup = BooleanField(required=True)
    


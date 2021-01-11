from motor.document import Document
from motor.fields import StringField


class Park(Document):
    park_name = StringField(required=True)
    asset_id = StringField(required=True)


# from pydantic import BaseModel


# class Park(BaseModel):
#     park_name: str
#     asset_id: str

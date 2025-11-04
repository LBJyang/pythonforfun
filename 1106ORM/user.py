from model import Model
from field import IntegerField, StringField


class User(Model):
    id = IntegerField("id")
    name = StringField("username")
    email = StringField("email")
    password = StringField("password")


u = User(id=12345, name="yangjiaze", email="jiaze@gmail.com", password="my-pwd")
u.save()

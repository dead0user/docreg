from peewee import *


db = SqliteDatabase('documents.db')


class Company(Model):
    name = CharField()

    class Meta():
        database = db

class shortDate(Model):
    name = CharField()

    class Meta():
        database = db

class Document(Model):
    date = DateField()
    netto_quota = FloatField()
    doc_number = CharField()
    company = ForeignKeyField(Company, backref='documents')
    if_short_date = ForeignKeyField(shortDate)
    if_beer = FloatField()
    if_wine = FloatField()
    if_vodka = FloatField()

    class Meta():
        database = db

db.connect()
db.create_tables([Company, shortDate, Document])

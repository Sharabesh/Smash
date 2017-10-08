import peewee
import os
from playhouse import signals
from playhouse.postgres_ext import *
from playhouse.csv_loader import *
from urllib.parse import urlparse

url = urlparse(os.environ["SMASH_URL"])

config = dict(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port,
    sslmode='require'
)

conn = PostgresqlExtDatabase(
    autocommit=True,
    autorollback=True,
    register_hstore=False,
    **config
)


class BaseModel(signals.Model):
    class Meta:
        database = conn


class Library(BaseModel):
    lname = peewee.CharField(null=True,primary_key=True)
    students = peewee.IntegerField(null=True)
    capacity = peewee.IntegerField(null=True)

    class Meta:
        db_table = 'library'


class Users(BaseModel):
    userid = peewee.PrimaryKeyField(null=True)
    username = peewee.CharField(null=True)
    password = peewee.CharField(null=True)
    email = peewee.CharField(null=True)

    class Meta:
        db_table = 'library'





def update_count(lib_id):
    q = Library.update(students= Library.students + 1).where(Library.lname == lib_id).execute()
    val = list(Library.select().where(Library.lname == lib_id).execute())[0]
    return val.students

def get_all_names():
    return list(Library.select(Library.lname).execute())

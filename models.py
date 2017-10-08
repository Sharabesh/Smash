import peewee
import os
from playhouse import signals
from playhouse.postgres_ext import *
from playhouse.csv_loader import *
from urllib.parse import urlparse
import json

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
    val = list(Library.select().where(Library.lname == lib_id).execute())
    if val:
        val = val[0]
    else:
        return 10000
    return val.students


def get_count(lib_id):
    val = list(Library.select().where(Library.lname == lib_id).execute())
    if val:
        val = val[0]
    else:
        return 10000
    return val.students
def get_capacity(lib_id):
    val = list(Library.select().where(Library.lname == lib_id).execute())
    if val:
        val = val[0]
    else:
        return 10000
    return val.capacity

def return_everything():
    val = Library.select().execute()
    output_dict = {}
    for element in val:
        lname  = element.lname
        s = element.students
        c = element.capacity
        output_dict[lname] = [s,c]

    return json.dumps(output_dict)


def get_all_names():
    return list(Library.select(Library.lname).execute())


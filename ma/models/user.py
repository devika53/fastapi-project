from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta

users=Table(
    'users',meta,
    Column('id',Integer,primary_key=True),
    Column('movie_name',String(255)),
    Column('director_name',String(255)),
    Column('synopsis',String(255))
)
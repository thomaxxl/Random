from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect

Base = automap_base()
engine = create_engine("sqlite:///main.db.sqlitedb")
Base.prepare(engine, reflect=True)
session = Session(engine)

for table in Base.classes:
    for column in inspect(table).mapper.columns:
        matches = session.query(table).filter(column.like("%@%.%"))
        for match in matches.all():
            print(table, column.name, getattr(match, column.name))

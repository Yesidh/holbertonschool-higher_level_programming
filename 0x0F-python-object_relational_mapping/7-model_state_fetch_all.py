#!/usr/bin/python3
"""
===================================================================
script that lists all State objects from the database hbtn_0e_6_usa
===================================================================
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    the_session = sessionmaker(bind=engine)
    session = the_session()

    for alguna_cosa in session.query(State):
        print("{}: {}".format(alguna_cosa.id, alguna_cosa.name))

#!/usr/bin/python3
"""
=========================================================================
script that prints the first State object from the database hbtn_0e_6_usa
=========================================================================
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    the_session = sessionmaker(bind=engine)
    session = the_session()

    el_primerito = session.query(State).first()
    if el_primerito is None:
        print("Nothing")
    else:
        print("{}: {}".format(el_primerito.id, el_primerito.name))

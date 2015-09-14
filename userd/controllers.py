#!/usr/bin/env python

import cherrypy
import os

from jinja2 import Environment, PackageLoader

workingin="/home/asklepios/eric-workspace/userd"
templatedir=workingin+"/views"

os.chdir(workingin)


import sqlalchemy as sqa
from sqlalchemy.orm import sessionmaker
from models import User

env = Environment(loader=PackageLoader('views', 'templates'))


engine = sqa.create_engine('mysql+mysqlconnector://root@localhost/user?charset=utf8', echo=True)
connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()

class Root(object):

    @cherrypy.expose
    def index(self):
        our_user = session.query(User).filter_by(uname='ak').first()
        template_index=env.get_template('base.tmpl')
        return template_index.render(user=our_user)

if __name__ == '__main__':
   cherrypy.quickstart(Root(), '/')

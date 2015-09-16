#!/usr/bin/env python

import cherrypy
import os

from jinja2 import Environment, PackageLoader

workingin="/home/asklepios/eric-workspace/userd/userd"
templatedir=workingin+"/views"

os.chdir(workingin)


import sqlalchemy as sqa
from sqlalchemy.orm import sessionmaker
from models import User, Group

env = Environment(loader=PackageLoader('views', 'templates'))


engine = sqa.create_engine('mysql+mysqlconnector://root@localhost/user?charset=utf8', echo=True)
connection = engine.connect()

class Root(object):

    @cherrypy.expose
    def adminuser(self, username):
        Session = sessionmaker(bind=engine)
        session = Session()
        our_user = session.query(User).filter_by(uname=username).first()
        # special case informix: it's not a locationgroup
        ingroups = session.query(Group).filter(Group.gname.like("in%"), ~(Group.gname=='informix')).order_by(Group.gname)
        abtgroups = session.query(Group).filter(Group.gname.like("abt_%")).order_by(Group.gname)
        gremgroups = session.query(Group).filter(Group.gname.like("grem_%")).order_by(Group.gname)
        resgroups = session.query(Group).filter(Group.gname.like("res_%")).order_by(Group.gname)
        irgroups = session.query(Group).filter(Group.gname.like("ir_%")).order_by(Group.gname)
        amqpgroups = session.query(Group).filter(Group.gname.like("amqp_%")).order_by(Group.gname)
        other = session.query(Group).filter((~Group.gname.like("in%")) | (Group.gname=='informix'),
                                            ~Group.gname.like("abt_%"),
                                            ~Group.gname.like("grem_%"),
                                            ~Group.gname.like("res_%"),
                                            ~Group.gname.like("ir%"),
                                            ~Group.gname.like("amqp_%")).order_by(Group.gname)
        groups = [  ('Ortsgruppen', ingroups),
                    ('Abteilungen', abtgroups),
                    ('Gremien', gremgroups),
                    ('Ressors', resgroups),
                    ('Interred', irgroups),
                    ('AMQP-Notifier', amqpgroups),
                    ('Andere', other)]



        template_index=env.get_template('adminuser.tmpl')
        return template_index.render(user=our_user, groups=groups)

    @cherrypy.expose
    def group(self, groupname):
        Session = sessionmaker(bind=engine)
        session = Session()
        our_group = session.query(Group).filter_by(gname=groupname).first()
        allusers = session.query(User).order_by(User.uname)
        # filter by flag this is ugly - but there is no support for "FIND_IN_SET('value',set_col)" in sqlalchemy
        # selecting all 'lock'ed users
        lockedusers = []
        for user in allusers :
            if 'lock' in user.flags:
                lockedusers.append(user)
        # selecting all 'hidden' users
        hiddenusers = []
        for user in allusers:
            if 'hidden' in user.flags:
                hiddenusers.append(user)
        # selecting all users not 'hidden' and not 'lock'ed
        activeusers = []
        for user in allusers :
            if not 'hidden' in user.flags and not 'lock' in user.flags:
                activeusers.append(user)
        users = [   ("aktive", activeusers),
                    ("gesperrte", lockedusers),
                    ("versteckte", hiddenusers)]
        print(list(hiddenusers))

        template_index=env.get_template('group.tmpl')
        return template_index.render(group=our_group, users=users)


    @cherrypy.expose
    def user(self):
        Session = sessionmaker(bind=engine)
        session = Session()
        our_user = session.query(User).filter_by(uname='ak').first()
        template_index=env.get_template('user.tmpl')
        return template_index.render(user=our_user)


if __name__ == '__main__':
    conf = {'/static': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': os.path.join(workingin, 'static')
            }}
    print(os.path.join(workingin, 'static'))
    cherrypy.quickstart(Root(), '/', config=conf)

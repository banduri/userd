import sqlalchemy as sqa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(sqa.Base):
    __tablename__ = 'user'
    id = sqa.Column(sqa.Integer, primary_key = True,  nullable = False)
    uid = sqa.Column(sqa.Integer, nullable = False)
    uname = sqa.Column(sqa.String, nullable = False)
    main_group = sqa.Column(sqa.Integer, nullable = False)
    #flags set('lock','perm','hidden','group_leader','male','adm','multiLogin'
    password = sqa.Column(sqa.String, nullable = False)
    pw_md5 = sqa.Column(sqa.String, nullable = True)
    pw_lan = sqa.Column(sqa.String, nullable = True)
    pw_nt = sqa.Column(sqa.String, nullable = True)
    shell = sqa.Column(sqa.String, nullable = False)
    home = sqa.Column(sqa.String, nullable = False)
    last_host = sqa.Column(sqa.String, nullable = False)
    name1 = sqa.Column(sqa.String, nullable = False)
    name2 = sqa.Column(sqa.String, nullable = False)
    department = sqa.Column(sqa.String, nullable = False)
    expires = sqa.Column(sqa.Integer, nullable = False)
    last_login = sqa.Column(sqa.Integer, nullable = False)
    creator = sqa.Column(sqa.Integer, nullable = False)
    creation_time = sqa.Column(sqa.Integer, nullable = False)
    updater = sqa.Column(sqa.Integer, nullable = False)
    update_time = sqa.Column(sqa.Integer, nullable = False)
    lck_user = sqa.Column(sqa.Integer, nullable = False)
    lck_time = sqa.Column(sqa.Integer, nullable = False)
    lck_ip = sqa.Column(sqa.String, nullable = True)
    note = sqa.Column(sqa.String, nullable = True)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                             self.name, self.fullname, self.password)

class Group(sqa.Base):
    __tablename__ = 'ugroup'
    id = sqa.Column(sqa.Integer,  primary_key = True, nullable = False)
    gid = sqa.Column(sqa.Integer, nullable = False)
    gname = sqa.Column(sqa.String, nullable = False)
    #flags enum('normal','pseudo')
    creator = sqa.Column(sqa.Integer, nullable = False)
    creation_time = sqa.Column(sqa.Integer, nullable = False)
    note = sqa.Column(sqa.String, nullable = True)

class Addr(sqa.Base):
    __tablename__ = 'addr'
    id = sqa.Column(sqa.Integer, primary_key = True, nullable = False)
    id_user = sqa.Column(sqa.Integer, nullable = False)
    name = sqa.Column(sqa.String, nullable = True)
    country = sqa.Column(sqa.String, nullable = True)
    city = sqa.Column(sqa.String, nullable = True)
    zip_code = sqa.Column(sqa.String, nullable = True)
    street_addr = sqa.Column(sqa.String, nullable = True)
    zip_pobox = sqa.Column(sqa.String, nullable = True)
    pobox = sqa.Column(sqa.String, nullable = True)

class Phone(sqa.Base):
    __tablename__ = 'phone'
    id = sqa.Column(sqa.Integer, primary_key = True, nullable = False)
    id_user = sqa.Column(sqa.Integer, nullable = False)
    name = sqa.Column(sqa.String, nullable = False)
    phone = sqa.Column(sqa.String, nullable = False)

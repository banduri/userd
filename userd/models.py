import sqlalchemy as sqa
import sqlalchemy.dialects.mysql as sdm
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy.types as types
import datetime as dt

Base = declarative_base()

association_table = sqa.Table('rel_ugroup', Base.metadata,
    sqa.Column('id_ugroup', sqa.Integer, sqa.ForeignKey('ugroup.id')),
    sqa.Column('id_user', sqa.Integer, sqa.ForeignKey('user.id'))
)

class TimestampAsBigInt(types.TypeDecorator):
    impl = types.BigInteger
    #
    def process_bind_param(self, value, dialect):
        return int(value.timestamp())
    #
    def process_result_value(self, value, dialect):
        return dt.datetime.fromtimestamp(value)


class User(Base):
    __tablename__ = 'user'
    flags_values = {'lock' : 'Sperre',
                    'perm' : 'Sonderrechte',
                    'hidden' : 'Versteckt',
                    'group_leader' : 'Gruppenleiter',
                    'male' : 'männlich',
                    'adm' : 'Admin',
                    'multiLogin' : ' Passwortsperre'}
    id = sqa.Column(sqa.Integer, primary_key = True,  nullable = False)
    uid = sqa.Column(sqa.Integer, nullable = False)
    uname = sqa.Column(sqa.String(30), nullable = False)
    main_group = sqa.Column(sqa.Integer, sqa.ForeignKey('ugroup.id'), nullable = False)
    group = sqa.orm.relationship("Group")
    groups = sqa.orm.relationship("Group", secondary = association_table )
    #set('lock','perm','hidden','group_leader','male','adm','multiLogin'
    # how to use mysql sets in sqlalchemy? BigInt? String?
    flags = sqa.Column(sdm.SET(list(flags_values.keys())), nullable = True)
    password = sqa.Column(sqa.String(16), nullable = False)
    pw_md5 = sqa.Column(sqa.String(36), nullable = True)
    pw_lan = sqa.Column(sqa.String(34), nullable = True)
    pw_nt = sqa.Column(sqa.String(34), nullable = True)
    shell = sqa.Column(sqa.String(255), nullable = False)
    home = sqa.Column(sqa.String(255), nullable = False)
    last_host = sqa.Column(sqa.String(255), nullable = False)
    name1 = sqa.Column(sqa.String(50), nullable = False)
    name2 = sqa.Column(sqa.String(50), nullable = False)
    department = sqa.Column(sqa.String(30), nullable = False)
    expires = sqa.Column(TimestampAsBigInt, nullable = False)
    last_login = sqa.Column(TimestampAsBigInt, nullable = False)
    creator = sqa.Column(sqa.Integer, sqa.ForeignKey('user.id'), nullable = False)
    cuser = sqa.orm.relationship("User", remote_side=[id], foreign_keys = 'User.creator', uselist=False)
    created = sqa.orm.relationship("User", foreign_keys = 'User.creator')
    creation_time = sqa.Column(TimestampAsBigInt, nullable = False)
    updater = sqa.Column(sqa.Integer, sqa.ForeignKey('user.id'), nullable = False)
    uuser = sqa.orm.relationship("User", remote_side=[id], foreign_keys = 'User.updater', uselist=False)
    updated = sqa.orm.relationship("User", foreign_keys = 'User.updater')
    update_time = sqa.Column(TimestampAsBigInt, nullable = False)
    lck_user = sqa.Column(sqa.Integer, sqa.ForeignKey('user.id'), nullable = False)
    luser = sqa.orm.relationship("User", remote_side=[id], foreign_keys = 'User.lck_user', uselist=False)
    lck_time = sqa.Column(TimestampAsBigInt, nullable = False)
    lck_ip = sqa.Column(sqa.String(15), nullable = True)
    note = sqa.Column(sdm.LONGTEXT, nullable = True)
    #
    def __repr__(self):
        return "<User(name='%s', fullname='%s')>" % (self.uname, self.name1+" "+self.name2)

class Group(Base):
    __tablename__ = 'ugroup'
    id = sqa.Column(sqa.Integer,  primary_key = True, nullable = False)
    gid = sqa.Column(sqa.Integer, nullable = False)
    gname = sqa.Column(sqa.String(30), nullable = False)
    users = sqa.orm.relationship("User", secondary = association_table )
    flags = sqa.Enum('normal','pseudo')
    creator = sqa.Column(sqa.Integer, nullable = False)
    creation_time = sqa.Column(TimestampAsBigInt, nullable = False)
    note = sqa.Column(sdm.LONGTEXT, nullable = True)

class Addr(Base):
    __tablename__ = 'addr'
    id = sqa.Column(sqa.Integer, primary_key = True, nullable = False)
    id_user = sqa.Column(sqa.Integer, sqa.ForeignKey('user.id'), nullable = False)
    user = sqa.orm.relationship("User", backref=sqa.orm.backref('addr', uselist=False))
    name = sqa.Column(sqa.String(30), nullable = True)
    country = sqa.Column(sqa.String(30), nullable = True)
    city = sqa.Column(sqa.String(30), nullable = True)
    zip_code = sqa.Column(sqa.String(6), nullable = True)
    street_addr = sqa.Column(sqa.String(50), nullable = True)
    zip_pobox = sqa.Column(sqa.String(6), nullable = True)
    pobox = sqa.Column(sqa.String(6), nullable = True)
    def __repr__(self):
        return "<Addr(name='%s', country='%s', city='%s')>" % (self.name, self.country,  self.city)


class Phone(Base):
    __tablename__ = 'phone'
    id = sqa.Column(sqa.Integer, primary_key = True, nullable = False)
    id_user = sqa.Column(sqa.Integer, sqa.ForeignKey('user.id'), nullable = False)
    user = sqa.orm.relationship("User", backref=sqa.orm.backref('phone', uselist=False))
    name = sqa.Column(sqa.String(30), nullable = False)
    phone = sqa.Column(sqa.String(30), nullable = False)



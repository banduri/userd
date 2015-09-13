import sqlalchemy as sqa
from sqlalchemy.dialects.mysql import SET, LONGTEXT
from sqlalchemy.ext.declarative import declarative_base




Base = declarative_base()

association_table = sqa.Table('rel_ugroup', Base.metadata,
    sqa.Column('id_ugroup', sqa.Integer, sqa.ForeignKey('ugroup.id')),
    sqa.Column('id_user', sqa.Integer, sqa.ForeignKey('user.id'))
)


class User(Base):
    __tablename__ = 'user'
    id = sqa.Column(sqa.Integer, primary_key = True,  nullable = False)
    uid = sqa.Column(sqa.Integer, nullable = False)
    uname = sqa.Column(sqa.String(30), nullable = False)
    main_group = sqa.Column(sqa.Integer, sqa.ForeignKey('ugroup.id'), nullable = False)
    group = sqa.orm.relationship("Group")
    groups = sqa.orm.relationship("Group", secondary = association_table )
    #set('lock','perm','hidden','group_leader','male','adm','multiLogin'
    # how to use mysql sets in sqlalchemy? BigInt? String?
    flags = sqa.Column(SET('lock','perm','hidden','group_leader','male','adm','multiLogin'), nullable = True)
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
    expires = sqa.Column(sqa.BigInteger, nullable = False)
    last_login = sqa.Column(sqa.BigInteger, nullable = False)
    creator = sqa.Column(sqa.Integer, sqa.ForeignKey('user.id'), nullable = False)
    cuser = sqa.orm.relationship("User", remote_side=[id], foreign_keys = 'User.creator', uselist=False)
    created = sqa.orm.relationship("User", foreign_keys = 'User.creator')
    creation_time = sqa.Column(sqa.BigInteger, nullable = False)
    updater = sqa.Column(sqa.Integer, sqa.ForeignKey('user.id'), nullable = False)
    uuser = sqa.orm.relationship("User", remote_side=[id], foreign_keys = 'User.updater', uselist=False)
    updated = sqa.orm.relationship("User", foreign_keys = 'User.updater')
    update_time = sqa.Column(sqa.BigInteger, nullable = False)
    lck_user = sqa.Column(sqa.Integer, sqa.ForeignKey('user.id'), nullable = False)
    luser = sqa.orm.relationship("User", remote_side=[id], foreign_keys = 'User.lck_user', uselist=False)
    locked = sqa.orm.relationship("User", foreign_keys = 'User.lck_user')
    lck_time = sqa.Column(sqa.BigInteger, nullable = False)
    lck_ip = sqa.Column(sqa.String(15), nullable = True)
    note = sqa.Column(LONGTEXT, nullable = True)
    #
    def __repr__(self):
        return "<User(name='%s', fullname='%s')>" % (self.uname, self.name1+" "+self.name2)

class Group(Base):
    __tablename__ = 'ugroup'
    id = sqa.Column(sqa.Integer,  primary_key = True, nullable = False)
    gid = sqa.Column(sqa.Integer, nullable = False)
    gname = sqa.Column(sqa.String(30), nullable = False)
    userss = sqa.orm.relationship("User", secondary = association_table )
    flags = sqa.Enum('normal','pseudo')
    creator = sqa.Column(sqa.Integer, nullable = False)
    creation_time = sqa.Column(sqa.BigInteger, nullable = False)
    note = sqa.Column(LONGTEXT, nullable = True)

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


engine = sqa.create_engine('mysql+mysqlconnector://root@localhost/user?charset=utf8', echo=True)
connection = engine.connect()

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

our_user = session.query(User).filter_by(uname='ak').first()
our_user.cuser

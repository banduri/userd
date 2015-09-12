import sqlalchemy as sqa


class User(sqa.Base):
    __tablename__ = 'user'
    id = sqa.Column(sqa.Integer, primary_key=True,  autoincrement = True)
    uid = sqa.Column(sqa.Integer)
    uname = sqa.Column(sqa.String)
    main_group = sqa.Column(sqa.Integer)
    #flags set('lock','perm','hidden','group_leader','male','adm','multiLogin'
    password = sqa.Column(sqa.String)
    pw_md5 = sqa.Column(sqa.String)
    pw_lan = sqa.Column(sqa.String)
    pw_nt = sqa.Column(sqa.String)
    shell = sqa.Column(sqa.String)
    home = sqa.Column(sqa.String)
    last_host = sqa.Column(sqa.String)
    name1 = sqa.Column(sqa.String)
    name2 = sqa.Column(sqa.String)
    department = sqa.Column(sqa.String)
    expires = sqa.Column(sqa.Integer)
    last_login = sqa.Column(sqa.Integer)
    creator = sqa.Column(sqa.Integer)
    creation_time = sqa.Column(sqa.Integer)
    updater = sqa.Column(sqa.Integer)
    update_time = sqa.Column(sqa.Integer)
    lck_user = sqa.Column(sqa.Integer)
    lck_time = sqa.Column(sqa.Integer)
    lck_ip = sqa.Column(sqa.String)
    note = sqa.Column(sqa.String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                             self.name, self.fullname, self.password)

class Group(sqa.Base):
    __tablename__ = 'ugroup'
    id = sqa.Column(sqa.Integer,  primary_key = True,  autoincrement = True)
    gid = sqa.Column(sqa.Integer)
    gname = sqa.Column(sqa.String)
    #flags enum('normal','pseudo')
    creator = sqa.Column(sqa.Integer)
    creation_time = sqa.Column(sqa.Integer)
    note = sqa.Column(sqa.String)

class Addr(sqa.Base):
    __tablename__ = 'addr'
    id = sqa.Column(sqa.Integer, primary_key = True, autoincrement = True)
    id_user = sqa.Column(sqa.Integer)
    name = sqa.Column(sqa.String)
    country = sqa.Column(sqa.String)
    city = sqa.Column(sqa.String)
    zip_code = sqa.Column(sqa.String)
    street_addr = sqa.Column(sqa.String)
    zip_pobox = sqa.Column(sqa.String)
    pobox = sqa.Column(sqa.String)

class Phone(sqa.Base):
    __tablename__ = 'phone'
    id = sqa.Column(sqa.Integer, primary_key = True, autoincrement = True)
    id_user = sqa.Column(sqa.Integer)
    name = sqa.Column(sqa.String)
    phone = sqa.Column(sqa.String)

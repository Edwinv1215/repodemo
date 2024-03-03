from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
# from datetime import datetime

db = SQLAlchemy()

My_Pokemon = db.Table('My_Pokemon',
                      db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                      db.Column('pokemon_name', db.String, db.ForeignKey('pokemon.name'))
)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password =db.Column(db.String, nullable=False)
    catch = db.relationship('Pokemon', secondary=My_Pokemon,  lazy='dynamic')
        

    def __init__(self, username, email, password):

        self.username  = username
        self.email = email
        self.password =  generate_password_hash(password)


    def save(self):  
        db.session.add(self)  
        db.session.commit() 



class Pokemon(db.Model):
    name = db.Column(db.String, primary_key=True)
    base_hp = db.Column(db.Integer,  nullable=False)
    base_attack = db.Column(db.Integer,  nullable=False)
    base_defense = db.Column(db.Integer,  nullable=False)
    sprite_img = db.Column(db.String(200),  nullable=False)





    def __init__(self,name, base_hp, base_attack, base_defense,sprite_img):
        self.name = name
        self.base_hp = base_hp
        self.base_attack = base_attack
        self.base_defense = base_defense
        self.sprite_img = sprite_img



def save(self):
        db.session.add(self)
        db.session.commit()



# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String, unique=True, nullable=False)
#     email = db.Column(db.String, unique=True, nullable=False)
#     password = db.Column(db.String, nullable=False)
    
#     def __init__(self, username, email, password):
#         self.username = username
#         self.email = email
#         self.password = generate_password_hash(password)

#     def save(self):
#         db.session.add(self)
#         db.session.commit()

# class post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     img_url = db.Column(db.String, nullable=False)
#     caption = db.Column(db.String, nullable=False)
#     location = db.Column(db.String, nullable=True)
#     date = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __init__(self, img_url, caption, user_id, location=''):
#         self.img_url = img_url
#         self.caption = caption
#         self.user_id = user_id
#         self.location = location

    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'restaurant'    
    id = db.Column(db.Integer, primary_key=True)
    restaruant_name = db.Column(db.String)
    owner_name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    phno = db.Column(db.String(120))
    address = db.Column(db.String(120))
    city = db.Column(db.String(120))    
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'restaruant_name': self.restaruant_name,
            'owner_name': self.owner_name,
            'email': self.email,
            'phno': self.phno,
            'address': self.address,
            'city': self.city,
            'state': self.state,
        }
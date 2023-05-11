from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = 'customer'    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    phno = db.Column(db.String(120))
    address = db.Column(db.String(120))
    city = db.Column(db.String(120))    
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phno': self.phno,
            'address': self.address,
            'city': self.city,
            'state': self.state,
        }
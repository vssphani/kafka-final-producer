from config import db

class DbPerson(db.Model):
    __tablename__='employee'
    eno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),index=False,unique=False,nullable=False)
    city=db.Column(db.String(30),index=False,unique=False,nullable=False)
    desig=db.Column(db.String(30),index=False,unique=False,nullable=False)
    age=db.Column(db.Integer,primary_key=True)

    def __init__(self,sno,name,city,desig,age):
        self.eno=eno
        self.name=name
        self.city=city
        self.desig=desig
        self.age=age
    
    def serialize(self):
        return {
            'eno':self.eno,
            'name':self.name,
            'city':self.city,
            'desig':self.desig,
            'age':self.age
            }
    
    def __repr__(self):
        return str(self.serialize())

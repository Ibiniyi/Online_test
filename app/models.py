from app import db

class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True,unique=True,nullable=False)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    score = db.Column(db.Integer)
    matric_no = db.Column(db.String(255),unique=True,nullable=False)
    written = db.Column(db.Integer,default=0)
    def to_dict(self):
        """
        Returns a dictionary representation of the object.
        """
        attributes = {}
        for column in self.__table__.columns:
            attribute_name = column.name
            attribute_value = getattr(self, attribute_name)
            attributes[attribute_name] = attribute_value
        return attributes

class Question(db.Model):
    id = db.Column(db.Integer,primary_key=True,unique=True,nullable=False)
    question = db.Column(db.String(255), nullable=False, unique=True)
    answer = db.Column(db.String(255), nullable=False)
    options = db.Column(db.JSON, nullable=False)
    def to_dict(self):
        """
        Returns a dictionary representation of the object.
        """
        attributes = {}
        for column in self.__table__.columns:
            attribute_name = column.name
            attribute_value = getattr(self, attribute_name)
            attributes[attribute_name] = attribute_value
        return attributes

    
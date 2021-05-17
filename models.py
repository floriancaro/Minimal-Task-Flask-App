from app import db

class Task(db.Model):
    # SQLAlchemy deals with creating and managing the primary_key if it is set to True for a variable
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        # the f'-string syntax is an alternative to the .format syntax
        return f'{self.title}'

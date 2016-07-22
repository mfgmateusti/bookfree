
from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	email = db.Column(db.String, unique=True, nullable=False)
	password = db.Column(db.String, mullable=False)

	name = db.Column(db.String)
	cpf = db.Column(db.String)
	gender = db.Column(db.String)
	birthday = db.Column(db.Date)

	def __repr__(self):
		return "<User %r>" % self.email

class Book(db.model):
	id = db.Column(db.Integer, primary_key=True)

	title = db.Collumn(db.String, nullable=False)
	author = db.Collumn(db.String, nullable=False) # Turn in a new table
	publisher = db.Collumn(db.String, nullable=False) # Turn in a new table
	gender = db.Collumn(db.String, nullable=False) # Turn in a new table
	isbn = db.Collumn(db.String)

	def __repr__(self):
		return "<Book %r>" % self.title

class Borrow(db.model):
	id = db.Collumn(db.Integer, primary_key=True)
	id_lender = db.Collumn(db.Integer, nullable=False)
	id_borrower = db.Collumn(db.Integer, nullable=False)
	id_borrower = db.Collumn(db.Integer, nullable=False)
	final_date = db.Collumn(db.Date, nullable=False)
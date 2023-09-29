from db import db


class BusinessModel(db.Model):
    __tablename__ = "businesses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    category = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String, nullable=True)
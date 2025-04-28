from sqlalchemy.dialects.postgresql import UUID, TEXT
from sqlalchemy import func
from db import db

class Book(db.Model):
    __tablename__ = 'book'
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=func.uuid_generate_v4())
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    description = db.Column(TEXT(), nullable=False)
    isFavorite = db.Column(db.Boolean, nullable=False, default=False)
    isReading = db.Column(db.Boolean, nullable=False, default=False)
    isFinished = db.Column(db.Boolean, nullable=False, default=False)
    
    def as_dict(self):
        return {
            'id' : str(self.id),
            'title' : self.title,
            'author' : self.author, 
            'description' : self.description,
            'isFavorite' : self.isFavorite,
            'isReading' : self.isReading,
            'isFinished' : self.isFinished
        }
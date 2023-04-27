from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

    @validates('name')
    def validate_names(self, key, name):
        names = db.session.query(Author.name).all()
        if not name:
            raise ValueError('Name is required.')

    @validates('phone_number')
    def val_phone(self, key, phone_number):
        if len(phone_number) != 10:
            raise ValueError('Not a valid phone number.')


class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    @validates('title')
    def title_valid(self, key, title):
        clickbait = ["Won't Believe","Secret","Top","Guess"]
        if not any(phrase in title for phrase in clickbait):
            raise ValueError('Not clickbait.')

    @validates('content')
    def content_valid(self, key, content):
        if not len(content) >= 250:
            raise ValueError('Content is 250 char min.')

    @validates('summary')
    def summary_valid(self, key, summary):
        if len(summary) >= 250:
            raise ValueError('Summary is 250 char max.')
    
    @validates('category')
    def category_valid(self, key, category):
        if category != 'Fiction' and category != 'Non-Fiction':
            raise ValueError('Not a valid category.')


        


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'

from src import db

# Note Class
class Note(db.Model):
   """
   Defines the Note model with `id` and `content` fields 
   representing a note in the database.

   Attributes:
      - id (int): The primary key that uniquely identifies a note.
      - content (str): The textual content of the note.
   """

   __tablename__ = 'notes'

   id = db.Column(db.Integer, primary_key=True)
   content = db.Column(db.String(200), nullable=False)

   def __init__(self, content):
      self.content = content

   def serialize(self):
      return {
         'id': self.id,
         'content': self.content
      }

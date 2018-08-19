from app import db
from sqlalchemy.sql import func

class Comment(db.Model):
  id           = db.Column(db.Integer, primary_key=True)
  comment      = db.Column(db.String(), nullable=False)
  email        = db.Column(db.String(120), index=True)
  time_created = db.Column(db.DateTime(timezone=True), server_default=func.now(), index=True) 
  time_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())
  approved     = db.Column(db.Boolean(), default=False)
  active       = db.Column(db.Boolean(), default=True) # inactive goes in the trash prior to full delete
  # do I need a separate Table for these?
  base_url     = db.Column(db.String(2048), index=True) # where the comment came from
  stub_url     = db.Column(db.String(2048), index=True) # where the comment came from

  def __repr__(self):
    return '<Comment {} -> {}>'.format(self.email, self.comment)

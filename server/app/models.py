from flask import abort
import bleach
import hashlib
from urllib.parse import urlparse
from markdown import markdown
from . import db
from sqlalchemy.sql import func

class Comment(db.Model):
  __tablename__ = 'comments'
  id            = db.Column(db.Integer, primary_key=True)
  comment       = db.Column(db.String(), nullable=False)
  name          = db.Column(db.String(120), nullable=False, index=True)
  email         = db.Column(db.String(120), index=True)
  time_created  = db.Column(db.DateTime(timezone=True), server_default=func.now(), index=True) 
  time_updated  = db.Column(db.DateTime(timezone=True), onupdate=func.now())
  approved      = db.Column(db.Boolean(), default=False)
  active        = db.Column(db.Boolean(), default=True) # inactive goes in the trash prior to full delete
  # do I need a separate Table for these?
  base_url      = db.Column(db.String(2048), nullable=False, index=True) # where the comment came from
  stub_url      = db.Column(db.String(2048), nullable=False, index=True) # where the comment came from

  def __repr__(self):
    return '<Comment {} -> {}>'.format(self.email, self.comment)

  @staticmethod
  def create(data):
    comment = Comment()
    comment.from_dict(data)
    return comment

  def from_dict(self, data):
    if 'email' in data:
      self.email = data['email']
    try:
      parsed = urlparse(data['url'])
      self.base_url = parsed.netloc
      self.stub_url = parsed.path
      self.comment = data['comment']
      self.name = data['name']
    except KeyError:
      abort(400)

  def to_dict(self):
    return {
      'id': self.id,
      'comment': self.comment_to_html(),
      'name': self.name,
      'email': hashlib.md5(self.email.lower().encode('utf-8')).hexdigest(),
      'time_created': self.time_created,
      'time_update': self.time_updated,
      'active': self.active,
      'approved': self.approved,
      'base_url': self.base_url,
      'stub_url': self.stub_url
    }

  def comment_to_html(self):
    allowed_tags = ['h1', 'h2', 'ul', 'li', 'a', 'abbr', 'acronym', 'b', 'code', 'pre', 'em', 'i', 'strong']
    return bleach.linkify(bleach.clean(
      markdown(self.comment, output_format='html'),
      tags=allowed_tags,
      strip=True))

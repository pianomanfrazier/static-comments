from flask import Blueprint, jsonify, request
import hashlib
from .authentication import requires_auth
from .models import Comment
from . import db

api = Blueprint('api', __name__)

def validate_comment(comment):
    """
    TODO
    ----
    - check honeypot
    - check url against urls in config
    """
    pass

@api.route('/', methods=['GET'])
def index():
    return jsonify({'msg': 'The static comment api version 1'})

@api.route('/comments', methods=['POST'])
def new_comment():
    """
    public facing api endpoint

    {
        comment: string, # can accept markdown
        name: string,
        email: string,
        honeypot: string,
        url: string
    }
    """
    comment = Comment.create(request.get_json() or {})
    db.session.add(comment)
    db.session.commit()
    
    return jsonify(comment.to_dict()), 201


@requires_auth
@api.route('/comments', methods=['GET'])
def comments():
    """ 
    returns comments from the database
    requires admin authorization

    QUERY PARAMS
    ------------
    baseURL: qualified baseURL from the config
    slug: the article slug in the url
    approved: bool
    active: bool

    TODO
    ----
    filter output based on query params
    """
    return jsonify([comment.to_dict() for comment in Comment.query.all()])

@requires_auth
@api.route('/comments/count', methods=['GET'])
def count():
    """
    returns the count of comments for a particular resource

    QUERY PARAMS
    ------------
    baseURL: qualified baseURL from the config
    slug: the article slug in the url
    approved: bool
    active: bool

    TODO
    ----
    filter output based on query params
    """
    return 'count'

@requires_auth
@api.route('/comments/<id>', methods=['GET'])
def get_comment(id):
    comment = Comment.query.get(id)
    if comment:
        return jsonify(comment.to_dict()), 200
    else:
        return jsonify({'msg':'Comment not found', 'error': True}), 404
        

@requires_auth
@api.route('/comments/<id>', methods=['PUT'])
def update_comment(id):
    comment = Comment.query.get(id)
    if comment:
        comment.from_dict(request.get_json() or {})
        db.session.commit()
        return jsonify({'msg':'Comment updated', 'error': False}), 200 
    else:
        return jsonify({'msg':'Comment not found', 'error': True}), 404

@requires_auth
@api.route('/comments/<id>', methods=['DELETE'])
def delete_comment(id):
    comment = Comment.query.get(id)
    if comment:
        db.session.delete(comment)
        db.session.commit()
        return jsonify({'msg':'Comment deleted', 'error': False}), 200 
    else:
        return jsonify({'msg':'Comment not found', 'error': True}), 404


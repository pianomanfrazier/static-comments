from flask import Blueprint, jsonify, request
import hashlib
from .authentication import requires_auth

api = Blueprint('api', __name__)

def validate_comment(comment):
    """
    TODO
    ----
    - check honeypot
    - check url against urls in config
    """
    pass

@api.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return jsonify({'msg': 'The static comment api version 1'})
    elif request.method == 'POST':
        """
        {
            comment: string,
            email: string,
            honeypot: string,
            url: string
        }
        """
        return jsonify({'msg': 'Comment submitted', 'error': False}), 201

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
    - bleach all input upon render 
    see https://github.com/miguelgrinberg/flack/blob/85af2b76d801b38d5728e2fa08cb1cdd713cabf9/flack/api/messages.py#L14
    and https://github.com/miguelgrinberg/flack/blob/85af2b76d801b38d5728e2fa08cb1cdd713cabf9/flack/models.py#L141
    """
    return jsonify({
        'email': hashlib.md5('jim@jim.com'.lower().encode('utf-8')).hexdigest(),
        'name': 'Jim Bob',
        'comment': 'Howdy, this is a great comment',
        'date': '2018-08-21_21:33:35'
    })

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
    """
    return 'count'

@requires_auth
@api.route('/comments/<id>', methods=['GET', 'PUT', 'DELETE'])
def comment(id=None):
    if request.method == 'GET':
        if id != '1':
            return id
        else:
            return jsonify({'msg':'Comment ID not found', 'error': True}), 404
    elif request.method == 'PUT':
        return jsonify({'msg':'Comment updated', 'error': False}), 200 
    elif request.method == 'DELETE':
        return jsonify({'msg':'Comment deleted', 'error': False}), 200 

from chatapi.models import User, Message, Text, Image, Video, serialize
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask import request, jsonify, make_response, Response
from datetime import timedelta
from chatapi import app, db, bcrypt, jwt


@app.route('/messages/', methods=['POST'])
@jwt_required()
def send_message():
    user = get_jwt_identity()
    sender = request.json.get('sender', '')
    recipient = request.json.get('recipient', '')
    content = request.json.get('content', '')
    message = Message(sender=sender, recipient=recipient, content_type=content['type'])
    db.session.add(message)
    db.session.flush()
    # db.session.refresh(message) #in case session.flush doesnt refresh the message.id
    if content['type'] == 'text':
        media = Text(id=message.id, text=content['text'])
    elif content['type'] == 'image':
        media = Image(id=message.id, url=content['url'], height=content['height'], width=content['width'])
    elif content['type'] == 'video':
        media = Video(id=message.id, url=content['url'], source=content['source'])
    db.session.add(media)
    db.session.commit()
    return jsonify({'id': message.id, 'timestamp': message.timestamp}), 200


@app.route('/messages/', methods=['GET'])
@jwt_required()
def get_message():
    user = get_jwt_identity()

    recipient = request.args.get('recipient', type=int)
    start = request.args.get('start', type=int)
    limit = request.args.get('limit', default=100, type=int)
    query = db.session.query(Message, Text, Image, Video)\
        .outerjoin(Text, Image, Video)\
        .filter(Message.id >= start, Message.recipient == recipient)\
        .limit(limit)\
        .all()
    return jsonify({"messages": [serialize(q) for q in query]})


@app.route('/')
def hello_chat():
    return 'Welcome to the chat'


@app.route('/check/', methods=['POST'])
def check():
    return jsonify({"health": "ok"}), 200


@app.route('/login/', methods=['POST'])
def login():
    auth = request.authorization
    user = User.query.filter_by(username=auth.username).first()
    if user and bcrypt.check_password_hash(user.password, auth.password):
        token = create_access_token(identity={'id': user.id}, expires_delta=timedelta(minutes=430))
        return jsonify({'id': user.id, 'token': token}), 200
    return jsonify({"error": "Wrong credentials", }), 403


@app.route('/users/', methods=['POST'])
def create_user():
    print('create_user')
    username = request.json.get('username', '')
    if User.query.filter_by(username=username).first():
        print('User exist')
        return jsonify({"error": "User already exists", }), 406

    password = request.json.get('password', '')
    hashed = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(username=username, password=hashed)
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id}), 200

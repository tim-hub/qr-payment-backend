import uuid
from flask import request, url_for
from app import app, db
from models import Card, Machine, Scan

def get_uuid():
    return uuid.uuid4()

@app.route('/')
def main():
    return {'message':'hi there, thanks to use our service.'}

@app.route('/issue_a_card')
def issue_a_card():
    try:
        card = Card(uuid=get_uuid())
        db.session.add(card)
        db.session.commit()
        return {
            'data': {
                "uuid": str(card.uuid),
                'balance': card.balance
            },
            'message': 'got a uuid for your card.'
        }
    except Exception as e:
        raise e


@app.route('/issue_qr')
def issue_a_device():
    try:
        machine = Machine(uuid=get_uuid())
        db.session.add(machine)
        db.session.commit()
        return {
            'data': {
                "uuid": str(machine.uuid)
            },
            'message': 'got a uuid for the machine.'
        }
    except Exception as e:
        raise e


@app.route('/scan_tag//<string:machine_id>/')
def scan_tag(machine_id):
    card_id = str(request.data.get('card_id', None))
    # get this tag on from db
    tag_on = False
    balance = 0
    if tag_on:
        # decrease the balance
        return {
            'message': 'tag on',
            'data':{
                'balance': balance,
                'card_id': card_id
            }
        }
    else:
        # get and display the balance
        return {
            'message': 'tag off',
            'data':{
                'balance': balance,
                'card_id': card_id
            }
        }

@app.route('/admin')
def admin():
    # query results
    cards = Card.query.all()
    machines = Machine.query.all()
    scans = Scan.query.all()
    return {
        'message': 'all data for admin only',
        'data': {
            'cards': cards,
            'machines': machines,
            'scans': scans
        }
    }
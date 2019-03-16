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
                "uuid": str(card.uuid)
            },
            'message': 'got a uuid for your card.'
        }
    except Exception as e:
        print(e)
        raise e


@app.route('/issue_qr')
def issue_a_device():
    return {
        'data':{
            "uuid": str(get_uuid())
        },
        'message': 'got a uuid for your qr_code/nfc tag.'
    }

@app.route('/scan_tag//<string:machine_id>/')
def scan_tag(machine_id):
    card_id = str(request.data.get('card_id', ''))
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
    return {}
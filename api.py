import uuid
from flask import request
from app import app, db
from models import Card, Machine, Scan, CardSchema, MachineSchema, ScanSchema

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


@app.route('/issue_a_machine')
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


@app.route('/scan/<string:machine_id>/')
def scan_tag(machine_id):
    try:
        card_id = str(request.args.get('card_id', None))
        card = Card.query.filter_by(uuid=card_id).all()[0]
        machine = Machine.query.filter_by(uuid=machine_id).all()[0]

        # get this tag on from db
        last_scan = Scan.query.filter_by(card_id=card.id).order_by(Scan.created.desc()).limit(1).all()
        if len(last_scan) <=0:
            tag_on = False
        else:
            print(last_scan)
            tag_on = last_scan[0].tag_on
        print(last_scan)

        if not tag_on:
            # decrease the balance
            scan = Scan(
                card_id=card.id,
                machine_id=machine.id,
                tag_on= True
            )
            db.session.add(scan)
            db.session.commit()

            return {
                'message': 'tag on',
                'data':{
                    'balance': card.balance,
                    'card_id': card_id
                }
            }
        else:
            # get and display the balance
            scan = Scan(
                card_id=card.id,
                machine_id=machine.id,
                tag_on=False,
                amount= 2,
            )
            card.balance -= 2
            db.session.add(card)
            db.session.add(scan)
            db.session.commit()
            return {
                'message': 'tag off',
                'data': {
                    'balance': card.balance,
                    'card_id': card_id
                }
            }
    except Exception as e:
        raise e


@app.route('/admin')
def admin():
    # query results
    cards = Card.query.all()
    machines = Machine.query.all()
    scans = Scan.query.all()
    return {
        'message': 'all data for admin only',
        'data': {
            'cards': CardSchema(many=True).dump(cards)[0],
            'machines': MachineSchema(many=True).dump(machines)[0],
            'scans': ScanSchema(many=True).dump(scans)[0]
        }
    }
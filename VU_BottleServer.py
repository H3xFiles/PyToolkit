from bottle import response, error, get, post, put, delete, request
import json
import sqlite3
import random
import os.path
import makeDatabase


def db_connect():
    conn = sqlite3.connect('inventory2.db')

    return conn


def allow_cors(func):
    """ this is a decorator which enable CORS for specified endpoint """

    def wrapper(*args, **kwargs):
        response.headers[
            'Access-Control-Allow-Origin'] = '*'  # * in case you want to be accessed via any website
        return func(*args, **kwargs)

    return wrapper


###############################################################################
# Routes
###############################################################################
@get('/')
def index():
    response.content_type = 'text/html'
    return '<h1>Welcome to the "mySERVER" v1.0</h1>'


@get('/database')
@allow_cors
def fetch_all_items():
    response.content_type = 'application/json'
    db = db_connect()
    items = db.cursor()
    items.execute('SELECT * FROM inventory ')
    all_items = items.fetchall()
    items.close()
    return json.dumps(all_items)


@post('/database/new')
def add_item():
    response.content_type = 'text/html'
    db = db_connect()
    items = db.cursor()
    name = request.params.get('name')
    type = request.params.get('category')
    place = request.params.get('location')
    date = request.params.get('date')
    quantity = request.params.get('amount')

    id = random.randint(1, 100000000000)
    items.execute('SELECT id FROM inventory WHERE id=?', (id,))
    old_id = items.fetchone()
    if id == old_id:
        while id == old_id:
            id = random.randint(1, 100000000000)
            return id
    else:
        items.execute("INSERT INTO inventory VALUES (?,?,?,?,?,?)", (id, name, type, place, date, quantity))
    db.commit()
    items.close()

    print "Adding item ..."
    print 'done.'
    return "<h2>Item added</h2>"


@put('/database/edit/<id:int>')
def update(id):
    response.content_type = 'text/html'
    name = request.params.get('name')
    type = request.params.get('type')
    place = request.params.get('place')
    date = request.params.get('date')
    quantity = request.params.get('quantity')
    db = db_connect()
    items = db.cursor()
    items.execute("""UPDATE inventory
                        SET name=?, category=?, location=?, date=?,
    		    amount=? WHERE id=?""",
                  (name, type, place, date, quantity, id))
    db.commit()
    items.close()
    print 'Items updated'
    return "<p>Items with id[%s] has been updated</p>" % id


@delete('/database/edit/<id:int>')
def delete_item(id):
    response.content_type = 'text/html'
    db = db_connect()
    items = db.cursor()
    items.execute('DELETE FROM inventory WHERE id=?', (id,))
    db.commit()
    items.close()
    print 'Item deleted'
    return "<h2>Items deleted</h2>"

    ###############################################################################
    # Error handling
    ###############################################################################


@error(403)
def mistake(e):
    return json.dumps({'Error': {'Message': e.status_line, 'Status': e.status_code}})


@error(401)
def mistake(e):
    return json.dumps({'Error': {'Message': e.status_line, 'Status': e.status_code}})


@error(403)
def mistake(e):
    return json.dumps({'Error': {'Message': e.status_line, 'Status': e.status_code}})


@error(404)
def error_404_handler(e):
    return json.dumps({'Error': {'Message': e.status_line, 'Status': e.status_code}})


@error(500)
def mistake(e):
    return json.dumps({'Error': {'Message': e.status_line, 'Status': e.status_code}})


if __name__ == "__main__":
    from bottle import run

    if not os.path.exists('/database2.db'):
        makeDatabase.create_new_database()

    run(host='localhost', port=8080, reloader=True, debug=True, autojson=True)

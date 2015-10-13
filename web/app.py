import bottle
import pymongo

@bottle.route('/')
def index():
    connection = pymongo.MongoClient('mongo', 27017)

    db = connection.test

    name = db.names

    item = name.find_one()

    return bottle.template('index', username = item["first"])

bottle.debug(True)
bottle.run(host='0.0.0.0', port=8080)

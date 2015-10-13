import bottle
import pymongo

@bottle.route('/')
def index():
    mythings = ['apple', 'orange', 'banana', 'peach']

    connection = pymongo.MongoClient('mongo', 27017)

    db = connection.test

    name = db.names

    item = name.find_one()

    return bottle.template('index', {'username' : item["first"], 'things': mythings})

@bottle.post('/favorite_fruit')
def favorite_fruit():
    fruit = bottle.request.forms.get("fruit")
    if (fruit == None or fruit == ""):
        fruit = "No Fruit Selected"

    return bottle.template('fruit_selection.tpl', {'fruit' : fruit})

bottle.debug(True)
bottle.run(host='0.0.0.0', port=8080)

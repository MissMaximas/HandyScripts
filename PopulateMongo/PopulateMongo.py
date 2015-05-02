__author__ = 'Chloe'

''' To run this script, just run 'python3 PopulateMongo.py' on the command line.
Make sure you have mongo installed and running, as well as pymongo.
Script was created on 02/04/2015 (DD/MM/YYYY)'''

from pymongo import MongoClient


class PopulateMongo:

    _connection_string = 'mongodb://localhost:27017/'

    def __init__(self, connection_string=None):
        if connection_string:
            self.client = MongoClient(connection_string)
        else:
            self.client = MongoClient(self._connection_string)
        self.db = self.client['ToyBox']
        self.collection = self.db['Pets']

    def populate_db(self):
        i = 0
        for i in range(0, 100):
            animal_name = 'Spot_{0}'.format(i)
            animal = {'name': animal_name,
                      'animal': 'dog',
                      'age': i}
            self.collection.insert(animal)
            i+=1

    def test_db(self):
        result = self.collection.find_one({'name': 'Spot_3'})
        print(result)
        print("The DB creation was a success! You have created the DB ToyBox with a collection of Pets.")


populate = PopulateMongo()
populate.populate_db()
populate.test_db()
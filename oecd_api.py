import requests
from pymongo import MongoClient


REST_EU_ROOT_URL = "http://restcountries.eu/rest/v1"
def REST_country_request(field='all', name=None, params=None):

    headers = {'User-Agent': 'Mozilla/5.0'}

    if not params:
        params = {}

    if field == 'all':
        return requests.get(REST_EU_ROOT_URL + '/all')

    url = '%s/%s/%s' % (REST_EU_ROOT_URL, field, name)
    print('Requesting URL:' + url)
    response = requests.get(url, params=params, headers=headers)

    if not response.status_code == 200:
        raise Exception('Request failed with status code' +
                        str(response.status_code))

    return response

def get_mongo_database(db_name, host='localhost',
                       port=27017, username=None,
                       password=None):
    '''get named db from mongoDB with/without authent'''
    if username and password:
        mongo_url = 'mongodb://%s:%s@%s/%s' % (username,
                                               password,
                                               host,
                                               db_name)
        conn = MongoClient(mongo_url)
    else:
        conn = MongoClient(host, port)

    return conn[db_name]


nobel_winners = [
    {'category': 'Physics',
     'name': 'Albert Einstein',
     'nationality': 'Swiss',
     'sex': 'male',
     'year': 1921},
    {'category': 'Physics',
     'name': 'Paul Dirac',
     'nationality': 'British',
     'sex': 'male',
     'year': 1933},
    {'category': 'Chemistry',
     'name': 'Marie Curie',
     'nationality': 'Polish',
     'sex': 'female',
     'year': 1911}
]


if '__name__' == '__main__':

    response = REST_country_request('currency', 'usd')
    response.json()

    client = MongoClient()
    db = client.nobel_prize
    coll = db.winners

    db_nobel = get_mongo_database('novel_prize')
    col = db_nobel['country_data']

    response = REST_country_request()

    col.insert(response.json())



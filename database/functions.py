import json
import os

DB_FILE = os.path.join(os.path.abspath('.'), 'database', 'marketplace_db.json') # verificati sa fie ok

def read_database(db_file=DB_FILE):
    print('Reading database...')
    with open(db_file) as f:
        data = json.load(f)

    return data


def write_database(data, db_file=DB_FILE):
    print('Writing database...')
    with open(db_file, 'w') as f:
        json.dump(data, f, indent=4)

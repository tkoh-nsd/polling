#%%

import firebase_admin
from firebase_admin import credentials, firestore

from project_utils import get_time_now

#%%

cred = credentials.Certificate("firebase_voting.json")
firebase_app = firebase_admin.initialize_app(cred)

# connect to firestore database
db = firestore.client()
# %%

# go to collection 'tables' then document 't01' and change the data
def reset_tables():
    singers = {
        f'singer{i}':{
            'guess': 0,
            'correct': False,
            'time': get_time_now()
        }
        for i in range(1,7)
    }
    doc_ref = db.collection("tables")
    for table in [f't{i:02d}' for i in range(1, 65)]:
        doc_ref.document(table).set(singers)

# %%

def vote(table_no, singer_no, guess_no):
    doc_ref = db.collection("tables").document(f't{table_no:02d}')
    answer = db.collection("answers").document(f'singer{singer_no}').get().to_dict().get('answer', 0)
    doc_ref.update({
        f'singer{singer_no}': {
            'guess': int(guess_no),
            'correct': int(guess_no) == answer,
            'time': get_time_now()
        }
    })

# %%


from config.mongo import mongo_db_connect

mongo_db = mongo_db_connect()

collection = mongo_db['scripts']
documents = collection.find(
    {
        'slides': {'$exists': True},
        'concepts_covered': {'$regex': 'new_.*'}
        #'id': {'$lt': 171}
    },
    {
        '_id': 0,
        'id': 1,
        'slides': 1
    }
)
if documents is None:
    query1 = None
else:
    query1 = [i for i in documents]

for i in query1:
    for j in i['slides']:
        if 'annotations' in j:
            for k in j['annotations']:
                if 'actions' in k:
                    if len(k['actions']):
                        val = k['actions'][0]
                        k['actions'] = [{
                            "action":val,
                            "action_description":""
                        }]
    print(i)

    documents1 = collection.update_one(
        {'id': i['id']},
        {'$set': {'slides': i['slides']}}
    )


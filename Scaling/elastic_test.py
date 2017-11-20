import pandas as pd
from elasticsearch import Elasticsearch
import time

def main():
    # (1) Load data
    # (2) Collect by user
    # (3) Create user index
    # (4) Search by "user-who-reviewed"
    dpath = 'samples/ratings_Amazon_Instant_Video.csv'
    columns=['user','item','rating','timestamp']
    df = pd.read_csv(dpath, header=None,names=columns)
    i = 0
    es = Elasticsearch()

    for user, dg in df[['user','item']].groupby('user'):
        doc = {'reviewed':dg['item'].tolist()}
        res = es.index(index="user-index", doc_type='reviewed', id=user, body=doc)
        if(i>1000):
            break
        i += 1

    query = {"query" : {
                "constant_score" : {
                    "filter" : {
                        "term" : {
                        "reviewed" : 'B00BLCHYKU'
                        }
                        }
                        }
                        }
                        }

    res = es.search(index="user-index", body=query)
    print("Got %d Hits:" % res['hits']['total'])
    for hit in res['hits']['hits']:
        print(hit["_source"])

if __name__ == '__main__':
    main()


    """
    es = Elasticsearch()

    doc = {
        'author': 'kimchy',
        'text': 'Elasticsearch: cool. bonsai cool.',
        'timestamp': datetime.now(),
    }
    res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
    print(res['created'])


    res = es.get(index="test-index", doc_type='tweet', id=1)
    print(res['_source'])

    es.indices.refresh(index="test-index")

    res = es.search(index="test-index", body={"query": {"match_all": {}}})
    print("Got %d Hits:" % res['hits']['total'])
    for hit in res['hits']['hits']:
        print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
    """

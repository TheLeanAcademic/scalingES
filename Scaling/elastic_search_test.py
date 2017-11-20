import pandas as pd
from elasticsearch import Elasticsearch

def main():
    es = Elasticsearch()
    query = {"query": { "term" : { 'reviewed' : 'B00BN4V2YA' } }}
    res = es.search(index="user-index", body=query)
    print("Got %d Hits:" % res['hits']['total'])
    for hit in res['hits']['hits']:
        print(hit["_source"])

if __name__ == '__main__':
    main()

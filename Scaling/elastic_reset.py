from elasticsearch import Elasticsearch

def main():
    es = Elasticsearch()
    es.indices.delete(index='user-index', ignore=[400, 404])

if __name__ == '__main__':
    main()

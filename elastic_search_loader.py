from elasticsearch import Elasticsearch, helpers
import csv

def load():
    # es configs
    es_host = 'localhost'
    es_port = 9200
    index_name = "job-seekers-000001"
    file_name = "Resume.csv"

    # connect to client
    es = Elasticsearch([{'host': es_host, 'port': es_port, "scheme": "http"}])

    # open csv file
    file_path = "/home/aliabusaleh/Downloads/{file_name}"
    with open(file_path.format(file_name="Resume.csv")) as f:
        reader = csv.DictReader(f)
        helpers.bulk(es, reader, index=index_name)

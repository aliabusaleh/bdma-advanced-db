import json
import os

import ijson

from elasticsearch import Elasticsearch, helpers
import csv

def load():
    # es configs
    es_host = 'localhost'
    es_port = 9200
    index_name = "job-posting-000001"
    file_path = "C:\\Users\\aligh\\Downloads\\original_dataset\\{file_name}"
    files_root = "C:\\Users\\aligh\\Downloads\\archive"
    file_name = "techmap-jobs-dump-2021-09.json"

    # connect to client
    es = Elasticsearch([{'host': es_host, 'port': es_port, "scheme": "http"}])

    with open(file_path.format(file_name=file_name),encoding="utf8") as f:
            for line in f:
                try:
                    j_content = json.loads(line)
                    del j_content['_id']
                    helpers.bulk(es, [j_content], index=index_name, ignore_status=True, raise_on_error=False)
                    print(x)
                    x = x+1
                except Exception as e:
                    print(f"Error {e}")
    # open csv file
    # with open(file_path.format(file_name=file_name)) as f:
    #     reader = csv.DictReader(f)
    #     helpers.bulk(es, reader, index=index_name)

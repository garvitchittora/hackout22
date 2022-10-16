from django.db import models
import requests

# query builder to call company's data api
class QueryBuilder:
    def __init__(self, table, attributes, query_type):
        self.url = "https://localhost:8001/api/v1/"
        self.table = table
        self.attributes = attributes
        self.type = query_type # get, post

    # function to call url
    def execute(self):
        if type == "get":
            final_url = self.url + self.table + "?"
            for key, value in self.attributes.items():
                final_url += key + "=" + value + "&"
            final_url = final_url[:-1]
            response = requests.get(final_url)
            return response.json()
        elif type == "post":
            final_url = self.url + self.table
            response = requests.post(final_url, self.attributes)
            return response.json()

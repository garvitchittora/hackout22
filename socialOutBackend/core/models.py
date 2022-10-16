from django.db import models
import requests
from .config import BASE_URL

# query builder to call company's data api
class QueryBuilder:
    def __init__(self, table, attributes, query_type):
        self.url = BASE_URL
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

class Analytics(models.Model):
    type = models.CharField(max_length = 50)
    count = models.IntegerField(default = 0)
    reference = models.CharField(max_length = 50)

    class Meta:
        db_table = "Analytics"
        verbose_name_plural = "Analytics"

    def __str__(self):
        return self.reference + " - " + self.type


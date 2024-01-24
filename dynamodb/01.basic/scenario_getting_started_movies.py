from decimal import Decimal
from io import BytesIO
import json
import logging
import os
from pprint import pprint
import requests
from zipfile import ZipFile
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
# from question import Question

logger = logging.getLogger(__name__)

class Movies:
    def __init__(self) -> None:
        pass

    def exists(self, table_name):
        pass

    def create_table(self, table_name):
        pass

    def list_tables(self):
        pass

    def write_batch(self, movies):
        pass

    def add_movies(self, title, year, plot, rating):
        pass

    def get_movie(self, title, year):
        pass

    def update_movie(self, title, year, rating, plot):
        pass

    def query_movies(self, year):
        pass
    
    def scan_movies(self, year_range):
        pass

    def delete_movie(self, title, year):
        pass


if __name__ == "__main__":
    pass

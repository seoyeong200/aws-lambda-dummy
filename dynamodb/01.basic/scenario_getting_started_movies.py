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
    def __init__(self, dyn_resource) -> None:
        self.dyn_resource = dyn_resource
        self.table=None

    def exists(self, table_name):
        pass

    def create_table(self, table_name):
        pass

    def list_tables(self):
        pass

    def write_batch(self, movies):
        """
        Table.batch_writer() 함수로 테이블에 items 를 put 하는 메소드
        - Inside the context manager, Table.batch_writer builds a list of requests.
        - context manager에 구현되어있는 매직메소드를 사용해서 put_item()을 했을 때
            DynamoDB로 batches of write requests를 보내고, 
            이 과정에서의 chunking, buffering, retrying은 자동으로 수행된다.
        """
        try:
            with self.table.batch_writer() as writer:
                for movie in movies:
                    writer.put_item(Item=movie)
        except ClientError as err:
            logger.error(
                "Couln't load data into table %s. Here's why: %s %s",
                self.table.name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

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

def run_scenario(table_name, movie_file_name, dyn_resources):
    logging.basicConfig(level=logging.INFO, 
                        format=f"%(levelname)s: %(message)s")
    
    movies = Movies(dyn_resources)

if __name__ == "__main__":
    pass

from src.cloud_io.mongo import MongoIO
from src.exception import CustomException
import sys

def fetch_product_names_from_cloud():
    try:
        mongo = MongoIO()
        collection_names = mongo.mongo_ins._mongo_operation__connect_database.list_collection_names()
        return [collection_name.replace('_', ' ')
                for collection_name in collection_names]

    except Exception as e:
        raise CustomException(e, sys)
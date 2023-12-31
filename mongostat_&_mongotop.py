# Populate the collections with this script

from concurrent.futures import ThreadPoolExecutor
from pymongo import MongoClient
import random

# Function to insert a document
def insert_document(client, i):
    db = client.sampleDatabase
    collection = db.LM_Number1 # Or LM_Number2 for mongotop
    document = {"_id": i, "value": random.randint(1, 1000)}
    collection.insert_one(document)

# Main script
def main():
    client = MongoClient('mongodb://localhost:27017/')

    # Using ThreadPoolExecutor to insert documents in parallel
    with ThreadPoolExecutor(max_workers=50) as executor:
        for i in range(50000):
            executor.submit(insert_document, client, i)

if __name__ == "__main__":
    main()

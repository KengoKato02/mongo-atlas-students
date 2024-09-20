from config import collection
from data_operations import create_dummy_data, run_queries

def main():
    # Careful here please, this is to clear exisiting data
    collection.delete_many({})

    create_dummy_data(collection)
    run_queries(collection)

if __name__ == "__main__":
    main()
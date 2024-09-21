from config import collection
from data_operations import create_dummy_data, run_queries

def main():
    # This is to clear exisiting data, before you start adding new shit
    collection.delete_many({})

    create_dummy_data(collection)
    run_queries()

if __name__ == "__main__":
    main()
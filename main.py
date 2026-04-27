import argparse
import json
from db import Database
from loader import Dataloader
from queries import Queries
from views import create_views
from exporter import Exporter
import os

os.makedirs("results", exist_ok=True)


# This is resetting the table in the database
def reset_tables(db):
    cursor = db.get_cursor()

    print("Table reset")

    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    cursor.execute("TRUNCATE TABLE students")
    cursor.execute("TRUNCATE TABLE rooms")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

    cursor.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--students", required=True)
    parser.add_argument("--rooms", required=True)
    parser.add_argument("--format", choices=["json", "xml"], default="json")

    args = parser.parse_args()

    db = Database()

    # RESET TABLES 
    reset_tables(db)

    # Load Data (rooms and students)
    loader = Dataloader(db)
    loader.load_rooms(args.rooms)
    loader.load_students(args.students)
    db.commit()
    print("Data Loaded")

    # Create views
    create_views()
    print("Views created")

    # Run Queries
    queries = Queries(db)
    results = queries.get_all_results()

    # Export JSON
    with open("results/output.json", "w") as f:
        json.dump(results, f, indent=4, default=float)
    print("✔ Results saved to results/output.json")

    # Export (JSON/XML)
    exporter = Exporter(db)
    exporter.export(args.format)

    db.close()


if __name__ == "__main__":
    main()
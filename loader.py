import json

class Dataloader:
    def __init__(self, db):
        self.db = db

    def load_rooms(self, path):
        cursor = self.db.get_cursor()

        with open(path) as f:
            rooms = json.load(f)

        data = [(r["id"], r["name"]) for r in rooms]

        cursor.executemany(
            "INSERT INTO rooms (id, name) VALUES (%s, %s)",
            data
        )

        cursor.close()

    def load_students(self, path):
        cursor = self.db.get_cursor()

        with open(path) as f:
            students = json.load(f)

        data = [
            (s["id"], s["name"], s["birthday"], s["room"], s["sex"])
            for s in students
        ]

        cursor.executemany(
            "INSERT INTO students (id, name, birthday, room, sex) VALUES (%s, %s, %s, %s, %s)",
            data
        )

        cursor.close()
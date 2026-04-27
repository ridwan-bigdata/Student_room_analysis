#This queries is reading from views
class Queries:
    def __init__(self, db):
        self.db=db

    def fetch(self, view):
        cursor=self.db.get_cursor()
        cursor.execute(f"Select * from {view}")
        
        columns= [col[0] for col in cursor.description]
        rows= cursor.fetchall()
        
        cursor.close()
        return [dict(zip(columns, row)) for row in rows]
    def get_all_results(self):
        return{
            "rooms_students_count": self.fetch("rooms_students_count"),
            "smallest_avg_age": self.fetch("smallest_avg_age"),
            "largest_age_diff": self.fetch("largest_age_diff"),
            "mixed_gender_rooms": self.fetch("mixed_gender_rooms"),
        }
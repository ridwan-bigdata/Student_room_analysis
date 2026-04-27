import json
import os

class Exporter:
    def __init__(self, db):
        self.db = db
    def fetch_data(self,query):
        cursor =self.db.get_cursor()
        cursor.execute(query)
        
        columns= [col[0] for col in cursor.description]
        rows=cursor.fetchall()
        
        cursor.close()
        return[dict(zip(columns, row)) for row in rows]
    
    def export(self, format="json"):
        queries = {
    "rooms_students_count": "SELECT * FROM rooms_students_count",
    "smallest_avg_age": "SELECT * FROM smallest_avg_age",
    "largest_age_diff": "SELECT * FROM largest_age_diff",
    "mixed_gender_rooms": "SELECT * FROM mixed_gender_rooms"
        }   
        
        results= {}
        for key, query in queries.items():
            results[key]=self.fetch_data(query)
        os.makedirs("results", exist_ok=True)
        file_path= f"results/output.{format}"

        if format == "json":
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(results, f, indent=4, default=float)
        elif format== "xml":
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("<results>\n")
                for key, items in results.items():
                    f.write(f"<{key}>\n")
                    for item in items:
                        f.write("   <item>\n")
                        for k, v in item.items():
                            f.write(f"<{k}>{v}</{k}>\n")
                        f.write("    </item>\n")
                    f.write(f"   </{key}>\n")
                f.write("</results>")
        print("Results saved to {file_path}")
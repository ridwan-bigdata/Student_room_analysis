from db import Database

def create_views():
    db = Database()
    cursor = db.get_cursor()

    views = [

        # 1. Rooms students count
        """
        CREATE OR REPLACE VIEW rooms_students_count AS
        SELECT r.name AS room,
               COUNT(s.id) AS student_count
        FROM rooms r
        LEFT JOIN students s ON r.id = s.room
        GROUP BY r.id;
        """,

        # 2. Smallest Average Age
        """
              CREATE OR REPLACE VIEW smallest_avg_age AS
       SELECT r.name AS room,
              AVG(YEAR(CURDATE()) - YEAR(s.birthday)) AS avg_age
       FROM rooms r
       LEFT JOIN students s ON r.id = s.room
       WHERE s.birthday IS NOT NULL
       GROUP BY r.id
       ORDER BY avg_age ASC
       LIMIT 5;
        """,

        # 3. Largest age difference
        """
       CREATE OR REPLACE VIEW largest_age_diff AS
       SELECT r.name AS room,
              MAX(YEAR(CURDATE()) - YEAR(s.birthday)) -
              MIN(YEAR(CURDATE()) - YEAR(s.birthday)) AS age_diff
       FROM rooms r
       LEFT JOIN students s ON r.id = s.room
       WHERE s.birthday IS NOT NULL
       GROUP BY r.id
       ORDER BY age_diff DESC
       LIMIT 5;
        """,

        # 4. Mixed gender rooms
        """
        CREATE OR REPLACE VIEW mixed_gender_rooms AS
        SELECT r.name AS room
        FROM rooms r
        JOIN students s ON r.id = s.room
        GROUP BY r.id
        HAVING COUNT(DISTINCT s.sex) > 1;
        """
    ]

    for query in views:
        cursor.execute(query)

    db.commit()
    cursor.close()
    db.close()

    print("Views created")
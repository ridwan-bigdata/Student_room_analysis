Select * from students_rooms.rooms;

# List of rooms and the number of students in each of them
Select r.name, count(s.id) AS student_count
FROM students_rooms.rooms r
LEFT JOIN students_rooms.students s
ON r.id = s.room
Group by r.id;

USE students_rooms;
# List of rooms and the number of students in each of them
Select r.name, count(s.id) AS student_count
FROM rooms r
LEFT JOIN students s
ON r.id = s.room
Group by r.id;

# 5 rooms with tyhe smallest average age of students
select r.name, 
AVG (timestampdiff(year, s.birthday,curdate())) AS avg_age
from rooms r 
Join students s
ON r.id = s.room
Group by r.id
order by avg_age ASC 
limit 5;

# 5 rooms with the largest difference in the age of students
select r.name, 
Max((timestampdiff(year, s.birthday,curdate()))) - 
Min( (timestampdiff(year, s.birthday,curdate())))  AS avg_diff
from rooms r 
Join students s
ON r.id = s.room
Group by r.id
order by avg_diff DESC 
limit 5;

# List of rooms where different-sex students live
Select r.name
From rooms r
Join students s
ON r.id = s.room
Group by r.id
Having count(distinct s.sex) > 1;


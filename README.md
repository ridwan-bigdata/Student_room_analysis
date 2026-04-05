# Project Title
Student Room Analysis. 

# Overview
This project processes student and room datasets stored in JSON files and loads the data into MYSQL relational database.
SQL queries are used to analyze the data and the results are exported in JSON format. Some of the results are
- the number of students per room
- age statistics
- mixed gender room allocations

# Architecture
The system follow the below data pipeline architecture.
1. Data Source
   * rooms.json
   * students.json
2. Data Ingestion
Python script reads JSON files and inserts the records into the database.
3. Database
   * MySQL Schema is students_rooms
   * Tables:
     * rooms
     * students
4. Processing
   * SQL queries performm data analysis to answer some key important questions
5. Output
   * The query results was exported to JSON format for each question.

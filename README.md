# Project Title
Student Room Analysis. 

# Overview
This project analyzes student-room allocation using MySQL and Python.
It implements a full data pipeline from JSON ingestion to structured output.

# Architecture
JSON Files --> loader.py (ETL - Load data)--> MySQL Database (students_rooms) --> views.py (SQL logic layer) --> queries.py (data retrieval) --> exporter.py (formatting + output) --> output.json

## Breakdown of what each part does.
1. Data Source
students.json & rooms.json

2. loader.py
* Reads JSON
* Inserts into MySQL
* Uses bulk insert (executemany)
* Handles reset of tables

3. MySQL (students_rooms)
* Stores structured data
* Enforces:
          Primary keys
          Foreign keys

4. views.py
   * Contains all SQL logic
   * Answers the 4 questions:
     - students per room
     - avg age
     - age difference
     - mixed gender

5. queries.py
 * Fetches data from views

6. exporter.py
* Converts results → JSON/XML
* Handles Decimal

7. main.py
Orchestrates everything: reset → load → create views → query → export

# Features
* JSON → MySQL data loading
* SQL views for analytics
* CLI-based execution
* JSON/XML export
* OOP-based architecture

# Queries Implemented
* Rooms and number of students
* 5 rooms with smallest average age
* 5 rooms with largest age difference
* Rooms with mixed gender

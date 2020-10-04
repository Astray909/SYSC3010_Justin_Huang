#!/usr/bin/env python3
import sqlite3
#connect to database file
dbconnect = sqlite3.connect("demo.db");
dbconnect.row_factory = sqlite3.Row;
cursor = dbconnect.cursor();

cursor.execute('''CREATE TABLE IF NOT EXISTS sensor (sensorID NUMERIC, type TEXT, zone TEXT);''');

cursor.execute('''INSERT INTO sensor values(1, "door", "kitchen")''');
cursor.execute('''INSERT INTO sensor values(2, "temperature", "kitchen")''');
cursor.execute('''INSERT INTO sensor values(3, "door", "garage")''');
cursor.execute('''INSERT INTO sensor values(4, "motion", "garage")''');
cursor.execute('''INSERT INTO sensor values(5, "temperature", "garage")''');

dbconnect.commit();

cursor.execute('SELECT * FROM sensor WHERE zone="garage"');
for row in cursor:
    print(row['sensorID'],row['type']);

cursor.execute('SELECT * FROM sensor WHERE zone="kitchen"');
for row in cursor:
    print(row['sensorID'],row['type']);

dbconnect.close();

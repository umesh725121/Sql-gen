# Sql-gen
SQL generator


# HR Dept Schema 
# Test data 

You can enter your requirement in natural language, ,POC will translate it into SQL and fetch the results .

for Example 

List all the employees of the department 

Here is the OUTPUT 

Action: sql_db_list_tables
Action Input: ""
Observation: countries, employees, departments, jobs, regions, locations, dependents
Thought:I see that there is an "employees" table in the database. I should query the schema of the "employees" table to see what columns are available.
Action: sql_db_schema
Action Input: "employees"
Observation: 
CREATE TABLE employees (
        employee_id SERIAL NOT NULL, 
        first_name VARCHAR(20), 
        last_name VARCHAR(25) NOT NULL, 
        email VARCHAR(100) NOT NULL, 
        phone_number VARCHAR(20), 
        hire_date DATE NOT NULL, 
        job_id INTEGER NOT NULL, 
        salary NUMERIC(8, 2) NOT NULL, 
        manager_id INTEGER, 
        department_id INTEGER, 
        CONSTRAINT employees_pkey PRIMARY KEY (employee_id), 
        CONSTRAINT employees_department_id_fkey FOREIGN KEY(department_id) REFERENCES departments (department_id) ON DELETE CASCADE ON UPDATE CASCADE, 
        CONSTRAINT employees_job_id_fkey FOREIGN KEY(job_id) REFERENCES jobs (job_id) ON DELETE CASCADE ON UPDATE CASCADE, 
        CONSTRAINT employees_manager_id_fkey FOREIGN KEY(manager_id) REFERENCES employees (employee_id) ON DELETE CASCADE ON UPDATE CASCADE
)

/*
3 rows from employees table:
employee_id     first_name      last_name       email   phone_number    hire_date       job_id  salary  manager_id      department_id
100     Steven  King    steven.king@sqltutorial.org     515.123.4567    1987-06-17      4       24000.00        None    9
101     Neena   Kochhar neena.kochhar@sqltutorial.org   515.123.4568    1989-09-21      5       17000.00        100     9
102     Lex     De Haan lex.de haan@sqltutorial.org     515.123.4569    1993-01-13      5       17000.00        100     9
*/
Thought:I can query the "employees" table to list all the employees working.
Action: sql_db_query
Action Input: "SELECT * FROM employees"
Observation: [(100, 'Steven', 'King', 'steven.king@sqltutorial.org', '515.123.4567', datetime.date(1987, 6, 17), 4, Decimal('24000.00'), None, 9), (101, 'Neena', 'Kochhar', 'neena.kochhar@sqltutorial.org', '515.123.4568', datetime.date(1989, 9, 21), 5, Decimal('17000.00'), 100, 9), (102, 'Lex', 'De Haan', 'lex.de haan@sqltutorial.org', '515.123.4569', datetime.date(1993, 1, 13), 5, Decimal('17000.00'), 100, 9), (103, 'Alexander', 'Hunold', 'alexander.hunold@sqltutorial.org', '590.423.4567', datetime.date(1990, 1, 3), 9, Decimal('9000.00'), 102, 6), (104, 'Bruce', 'Ernst', 'bruce.ernst@sqltutorial.org', '590.423.4568', datetime.date(1991, 5, 21), 9, Decimal('6000.00'), 103, 6), (105, 'David', 'Austin', 'david.austin@sqltutorial.org', '590.423.4569', datetime.date(1997, 6, 25), 9, Decimal('4800.00'), 103, 6), (106, 'Valli', 'Pataballa', 'valli.pataballa@sqltutorial.org', '590.423.4560', datetime.date(1998, 2, 5), 9, Decimal('4800.00'), 103, 6), (107, 'Diana', 'Lorentz', 'diana.lorentz@sqltutorial.org', '590.423.5567', datetime.date(1999, 2, 7), 9, Decimal('4200.00'), 103, 6), (108, 'Nancy', 'Greenberg', 'nancy.greenberg@sqltutorial.org', '515.124.4569', datetime.date(1994, 8, 17), 7, Decimal('12000.00'), 101, 10), (109, 'Daniel', 'Faviet', 'daniel.faviet@sqltutorial.org', '515.124.4169', datetime.date(1994, 8, 16), 6, Decimal('9000.00'), 108, 10), (110, 'John', 'Chen', 'john.chen@sqltutorial.org', '515.124.4269', datetime.date(1997, 9, 28), 6, Decimal('8200.00'), 108, 10), (111, 'Ismael', 'Sciarra', 'ismael.sciarra@sqltutorial.org', '515.124.4369', datetime.date(1997, 9, 30), 6, Decimal('7700.00'), 108, 10), (112, 'Jose Manuel', 'Urman', 'jose manuel.urman@sqltutorial.org', '515.124.4469', datetime.date(1998, 3, 7), 6, Decimal('7800.00'), 108, 10), (113, 'Luis', 'Popp', 'luis.popp@sqltutorial.org', '515.124.4567', datetime.date(1999, 12, 7), 6, Decimal('6900.00'), 108, 10), (114, 'Den', 'Raphaely', 'den.raphaely@sqltutorial.org', '515.127.4561', datetime.date(1994, 12, 7), 14, Decimal('11000.00'), 100, 3), (115, 'Alexander', 'Khoo', 'alexander.khoo@sqltutorial.org', '515.127.4562', datetime.date(1995, 5, 18), 13, Decimal('3100.00'), 114, 3), (116, 'Shelli', 'Baida', 'shelli.baida@sqltutorial.org', '515.127.4563', datetime.date(1997, 12, 24), 13, Decimal('2900.00'), 114, 3), (117, 'Sigal', 'Tobias', 'sigal.tobias@sqltutorial.org', '515.127.4564', datetime.date(1997, 7, 24), 13, Decimal('2800.00'), 114, 3), (118, 'Guy', 'Himuro', 'guy.himuro@sqltutorial.org', '515.127.4565', datetime.date(1998, 11, 15), 13, Decimal('2600.00'), 114, 3), (119, 'Karen', 'Colmenares', 'karen.colmenares@sqltutorial.org', '515.127.4566', datetime.date(1999, 8, 10), 13, Decimal('2500.00'), 114, 3), (120, 'Matthew', 'Weiss', 'matthew.weiss@sqltutorial.org', '650.123.1234', datetime.date(1996, 7, 18), 19, Decimal('8000.00'), 100, 5), (121, 'Adam', 'Fripp', 'adam.fripp@sqltutorial.org', '650.123.2234', datetime.date(1997, 4, 10), 19, Decimal('8200.00'), 100, 5), (122, 'Payam', 'Kaufling', 'payam.kaufling@sqltutorial.org', '650.123.3234', datetime.date(1995, 5, 1), 19, Decimal('7900.00'), 100, 5), (123, 'Shanta', 'Vollman', 'shanta.vollman@sqltutorial.org', '650.123.4234', datetime.date(1997, 10, 10), 19, Decimal('6500.00'), 100, 5), (126, 'Irene', 'Mikkilineni', 'irene.mikkilineni@sqltutorial.org', '650.124.1224', datetime.date(1998, 9, 28), 18, Decimal('2700.00'), 120, 5), (145, 'John', 'Russell', 'john.russell@sqltutorial.org', None, datetime.date(1996, 10, 1), 15, Decimal('14000.00'), 100, 8), (146, 'Karen', 'Partners', 'karen.partners@sqltutorial.org', None, datetime.date(1997, 1, 5), 15, Decimal('13500.00'), 100, 8), (176, 'Jonathon', 'Taylor', 'jonathon.taylor@sqltutorial.org', None, datetime.date(1998, 3, 24), 16, Decimal('8600.00'), 100, 8), (177, 'Jack', 'Livingston', 'jack.livingston@sqltutorial.org', None, datetime.date(1998, 4, 23), 16, Decimal('8400.00'), 100, 8), (178, 'Kimberely', 'Grant', 'kimberely.grant@sqltutorial.org', None, datetime.date(1999, 5, 24), 16, Decimal('7000.00'), 100, 8), (179, 'Charles', 'Johnson', 'charles.johnson@sqltutorial.org', None, datetime.date(2000, 1, 4), 16, Decimal('6200.00'), 100, 8), (192, 'Sarah', 'Bell', 'sarah.bell@sqltutorial.org', '650.501.1876', datetime.date(1996, 2, 4), 17, Decimal('4000.00'), 123, 5), (193, 'Britney', 'Everett', 'britney.everett@sqltutorial.org', '650.501.2876', datetime.date(1997, 3, 3), 17, Decimal('3900.00'), 123, 5), (200, 'Jennifer', 'Whalen', 'jennifer.whalen@sqltutorial.org', '515.123.4444', datetime.date(1987, 9, 17), 3, Decimal('4400.00'), 101, 1), (201, 'Michael', 'Hartstein', 'michael.hartstein@sqltutorial.org', '515.123.5555', datetime.date(1996, 2, 17), 10, Decimal('13000.00'), 100, 2), (202, 'Pat', 'Fay', 'pat.fay@sqltutorial.org', '603.123.6666', datetime.date(1997, 8, 17), 11, Decimal('6000.00'), 201, 2), (203, 'Susan', 'Mavris', 'susan.mavris@sqltutorial.org', '515.123.7777', datetime.date(1994, 6, 7), 8, Decimal('6500.00'), 101, 4), (204, 'Hermann', 'Baer', 'hermann.baer@sqltutorial.org', '515.123.8888', datetime.date(1994, 6, 7), 12, Decimal('10000.00'), 101, 7), (205, 'Shelley', 'Higgins', 'shelley.higgins@sqltutorial.org', '515.123.8080', datetime.date(1994, 6, 7), 2, Decimal('12000.00'), 101, 11), (206, 'William', 'Gietz', 'william.gietz@sqltutorial.org', '515.123.8181', datetime.date(1994, 6, 7), 1, Decimal('8300.00'), 205, 11)]
Thought:I have the results of the query. I can now return the list of all the employees working.
Final Answer: The list of all the employees working is [(100, 'Steven', 'King', 'steven.king@sqltutorial.org', '515.123.4567', datetime.date(1987, 6, 17), 4, Decimal('24000.00'), None, 9), (101, 'Neena', 'Kochhar', 'neena.kochhar@sqltutorial.org', '515.123.4568', datetime.date(1989, 9, 21), 5, Decimal('17000.00'), 100, 9), (102, 'Lex', 'De Haan', 'lex.de haan@sqltutorial.org', '515.123.4569', datetime.date(1993, 1, 13), 5, Decimal('17000.00'), 100, 9), (103, 'Alexander', 'Hunold', 'alexander.hunold@sqltutorial.org', '590.423.4567', datetime.date(1990, 1, 3), 9, Decimal('9000.00'), 102, 6), (104, 'Bruce', 'Ernst', 'bruce.ernst@sqltutorial.org', '590.423.4568', datetime.date(1991, 5, 21), 9, Decimal('6000.00'), 103, 6), (105, 'David', 'Austin', 'david.austin@sqltutorial.org', '590.423.4569', datetime.date(1997, 6, 25), 9, Decimal('4800.00'), 103, 6), (106, 'Valli', 'Pataballa', 'valli.pataballa@sqltutorial.org', '590.423.4560', datetime.date(1998, 2, 5), 9, Decimal('4800.00'), 103, 6), (107, 'Diana', 'Lorentz', 'diana.lorentz@sqltutorial.org', '590.423.5567', datetime.date(1999, 2, 7), 9, Decimal('4200.00'), 103, 6), (108, 'Nancy', 'Greenberg', 'nancy.greenberg@sqltutorial.org', '515.124.4569', datetime.date(1994, 8, 17), 7, Decimal('12000.00'), 101, 10), (109, 'Daniel', 'Faviet', 'daniel.faviet@sqltutorial.org', '515.124.4169', datetime.date(1994, 8, 16), 6, Decimal('9000.00'), 108, 10)].

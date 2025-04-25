import psycopg2
import os, sys

connection = psycopg2.connect(database="crm")
cursor = connection.cursor()


def clear():
    os.system('clear || cls')


# Companies
# create table companies (id serial, name varchar, number_of_employees int);

#  id | name | number_of_employees 
# ----+------+---------------------




# Employees
# create table employees (id serial, name varchar, employer varchar);

#  id | name | company_name 
# ----+------+---------------




# Create
def create():
    while True:
        selection = input('would you like to add a new 1. Company or 2. Employee? (press \'1\' or \'2\') ')
        print(f'You selected {selection}')
        
        if selection not in ['1', '2']:
            clear()
        elif selection == '1':        
            name = input('Please enter customer name:').capitalize()
            company_name = input('Please enter customer employer:').capitalize()
            cursor.execute(f'INSERT INTO employees (name, company_name) VALUES (%s, %s)', [ name, company_name ])
            cursor.execute(f'INSERT INTO companies (name) VALUES (%s)', [ company_name ])
            connection.commit()
            break
        else:
            name = input('Enter company name: ').capitalize()
            cursor.execute(f'INSERT INTO companies (name) VALUES (%s)', [ name ])
            connection.commit()
            break

# Read
# cursor.execute('SELECT * FROM employees')
# connection.commit()


# Update
# name = input('Update name')
# employer = input('Update employer')
# id = input('input customer id')
# cursor.execute('UPDATE employees SET name = %s, employer = %s WHERE id = %s', [name, employer, id])
# connection.commit()


# Delete
# id = input('input customer id')
# cursor.execute('DELETE FROM employees WHERE id = %s', [id])
# connection.commit()


create()

connection.close()
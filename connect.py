import psycopg2
import os, sys
import pandas



# Companies
#  id | name | number_of_employees 
# ----+------+---------------------


# Employees
#  id | name | company_name 
# ----+------+---------------




connection = psycopg2.connect(database="crm")
cursor = connection.cursor()


def clear():
    os.system('clear || cls')

def menu():
    while True:
        selection = input('\nPress \'e\' to exit to the menu.')
        
        if selection != 'e':
            print('Please select a valid option.\n')
        else:
            welcome()
            break




def welcome():
    clear()
    while True:
        selection = input('Please select an option:\n\n'  
                        '1. Add customer\n'
                        '2. View all customers\n'
                        '3. Update an existing customer\n'
                        '4. Delete an existing customer\n'
                        'q. Quit application\n\n'
                        'Enter the number of your choice: '
        )
        
        if selection not in ['1', '2', '3', '4', 'q']:
            clear()
            print('Please select a valid option.\n')
        
        elif selection == '1':
            print('Option 1')
            create()
            break
        
        elif selection == '2':
            read()
            menu()
            break
        
        elif selection == '3':
            update()
            break

        elif selection == '4':
            print('4')
            # break
        
        else:
            cursor.close()
            connection.close()
            print('Exiting application.')
            sys.exit
            break




# Create
def create():
    clear()
    while True:
        selection = input(
                        'What would you like to add?\n'
                        'Please select an option:\n\n'  
                        '1. Employee\n'
                        '2. Company\n'
                        'e. Exit to menu\n\n'
                        'Enter the number of your choice: '
        )
        
        if selection not in ['1', '2', 'e']:
            clear()
            print('Please select a valid option.\n')
            
        elif selection == '1':        
            name = input('\nPlease enter customer name: ').title()
            company_name = input(f'Name of company { name } is employed with: ').title()
            cursor.execute(f'INSERT INTO employees (name, company_name) VALUES (%s, %s)', [ name, company_name ])
            cursor.execute(f'INSERT INTO companies (name) VALUES (%s)', [ company_name ])
            connection.commit()
            clear()
            print(f'Successfully added { name } to the list of employees.\n')
            
        elif selection == '2':
            name = input('\nEnter company name: ').title()
            cursor.execute(f'INSERT INTO companies (name) VALUES (%s)', [ name ])
            connection.commit()
            print(f'Successfully added { name } to the list of companies.')
            
        else:
            welcome()
            break




# Read
def read():
    clear()
    cursor.execute('SELECT employees.name AS employee_name, employees.id AS employee_id, employees.company_name, companies.id AS company_id,COUNT(employees.id) OVER (PARTITION BY employees.company_name) AS number_of_employees FROM employees LEFT JOIN companies ON employees.company_name = companies.name;')
    connection.commit()
    
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    dataframe = pandas.DataFrame(rows, columns=columns)
    
    print(f'\n{dataframe}')




# Update
def update():
    read()
    print('\nWho would you like to update?')
    id = input('Input customer id: ')
    updated_name = input('Update customer name: ').title()
    updated_company_name = input('Update customer employer: ').title()
    cursor.execute('UPDATE employees SET name = %s, company_name = %s WHERE id = %s', [ updated_name, updated_company_name, id ])
    connection.commit()
    clear()
    print(f'Successfully updated { updated_name }\'s details.')




# Delete
# id = input('input customer id')
# cursor.execute('DELETE FROM employees WHERE id = %s', [id])
# connection.commit()




welcome()
connection.close()
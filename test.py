import psycopg2

conn = psycopg2.connect (
    host="localhost",
    database="postgres",
    user="postgres",
    password="2134",
    port="5432"
)

cursor = conn.cursor()

##create table

create_table_query = '''
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INTEGER,
        department VARCHAR(100)
    )
'''


cursor.execute(create_table_query)

conn.commit()

# Adjust the insert_employee function
def insert_employee(name, age, department):
    insert_query = '''
        INSERT INTO employees (name, age, department)
        VALUES (%s, %s, %s)
    '''
    cursor.execute(insert_query, (name, age, department))
    conn.commit()


##update 
def update_employee(id, new_age):
      update_query = '''
            UPDATE employees
            SET age = %s
            WHERE id =%s
      '''

      cursor.execute(update_query, (new_age, id))
      conn.commit()

      ##delete
def delete_employee(id):
    delete_query = '''
        DELETE FROM employees
        WHERE id = %s
    '''
    cursor.execute(delete_query, (id,))
    conn.commit()


##display

def display_employees():
      select_query = 'SELECT * FROM employees'
      cursor.execute(select_query)
      rows = cursor.fetchall()
      for row in rows:
           print(row)

      ##create the table of employee
        


##LOOPPP
while True:
      command = input("ENTER a command (.insert, .update, .delete, .display, or .exit): ")

      if command == ".insert":
            name = input("Enter the name of employee:")
            age = int(input("Enter the age of employee:"))
            department = input("Enter the department of the employee:")
            insert_employee(name, age, department)
            print("Employee inserted successfully!!")

      elif command == ".update":
                id = int(input("Enter the ID of the employee to update: "))
                new_age = int(input("Enter the new age for the employee: "))
                update_employee(id, new_age)
                print("Employee updated!")


      elif command == ".delete":
        id = int(input("Enter the ID of the employee to delete:"))
        delete_employee(id)
        print("Employee deleted!!")


      elif command == ".display":
        print("current employees:")
        select_query = 'SELECT * FROM employees'
        cursor.execute(select_query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)


      elif command == ".exit":
            break
      
      else:
            print("Invalid command")


            ##clossseee

      cursor.close()
      conn.close()  

      




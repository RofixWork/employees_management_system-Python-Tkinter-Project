import sqlite3 as sqlite
class Database:
    def __init__(self, db : str = 'test.db'):
        self.db : str = db
        self.connection = None

    def connect(self):
        try:
            if self.connection is None:
                self.connection = sqlite.connect(database=self.db)
                sql = '''
CREATE TABLE IF NOT EXISTS employees (
    id integer PRIMARY KEY,
    name text NOT NULL,
    age tinyint NOT NULL,
    job text NOT NULL,
    email text UNIQUE NOT NULL,
    gender text NOT NULL,
    mobile text UNIQUE NOT NULL,
    address text NOT NULL
)
'''               
                self.connection.execute(sql)
                print("Coonect to Database")
        except Exception as ex:
            print(f"Failed to connect to database: {ex}")
            self.connection = None

    def create(self, name, age, job, email, gender, mobile, address):
        try:
            with self.connection as connect:
                sql = '''
INSERT INTO employees(name, age, job, email, gender, mobile, address) VALUES (?, ?, ?, ?, ?, ?, ?)
'''
                connect.execute(sql, (name, age, job, email, gender, mobile, address))
                connect.commit()
        except Exception as ex:
            print("Failed to create employee", ex)

    def fetch(self):
        try:
            with self.connection as connect:
                sql = '''
SELECT * FROM employees
'''                 
                rows = connect.execute(sql)
                return rows.fetchall()
        except:
            print("Failed to fetch data")
            return

    def remove(self, id : int):
        try:
            with self.connection as connect:
                sql = 'delete from employees where id = ?'
                connect.execute(sql, (id,))
                connect.commit()
        except Exception as ex:
            print(f"Failed to remove employee with id {id}: {ex}")

    def update(self, id, name, age, job, email, gender, mobile, address):
        try:
            with self.connection as connect:
                sql = '''
UPDATE employees SET name = ?, age = ?, job = ?, email = ?, gender = ?, mobile = ?, address = ? WHERE id = ?
'''
                connect.execute(sql, (name, age, job, email, gender, mobile, address, id))
                connect.commit()
        except:
            print("Failed to update table")

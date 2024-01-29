from database.Database import Database
from model.Employee import Employee

class EmployeeController:
    def __init__(self):
        self.db = Database()

    def createEmployee(self, employee: Employee):
        result = self.getEmployeeByName(employee.last_name, employee.first_name)
        if(len(result) > 0):
            print('Employee already exists')
            return False
        
        self.db.connect()
        insert_query = """
            INSERT INTO employees (last_name, first_name, address, city, country, birthdate, department_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        employee_data = (employee.last_name, employee.first_name, employee.address, employee.city, employee.country, employee.birthdate, employee.department_id)
        self.db.execute_query(insert_query, employee_data)
        self.db.disconnect()
        return True

    def getEmployee(self, id):
        self.db.connect()
        select_query = """
            SELECT * FROM employees WHERE id=%s
        """
        results = self.db.fetch_all(select_query, (id))
        self.db.disconnect()
        return results

    def getEmployeeByName(self, last_name, first_name):
        self.db.connect()
        select_query = """
            SELECT * FROM employees WHERE last_name=%s AND first_name=%s
        """
        results = self.db.fetch_all(select_query, (last_name, first_name))
        self.db.disconnect()
        return results

    def getAllEmployees(self):
        self.db.connect()
        select_query = """
            SELECT * FROM employees
        """
        results = self.db.fetch_all(select_query)
        self.db.disconnect()
        return results
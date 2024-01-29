import os
from controller.EmployeeController import EmployeeController
from model.Employee import Employee

def main():
     # print(os.environ['PASSWORD'])
    employee1 = Employee('Muswashans', 'Employs', 'Aladeen St', 'Aladeen City', 'Wadeya', '1997-10-24', 1)
    employee2 = Employee('Washeroom', 'Ladiyes', 'Aladeen St', 'Aladeen City', 'Wadeya', '1997-10-24', 1)
    employee3 = Employee('Burgers', 'Allisons', 'Aladeen St', 'Aladeen City', 'Wadeya', '1997-10-24', 1)
    print(employee1)
    print(employee2)
    print(employee3)

    ec = EmployeeController()
    ec.createEmployee(employee1)
    ec.createEmployee(employee2)
    ec.createEmployee(employee3)

    employees_list = ec.getAllEmployees()
    for row in employees_list:
        print(row)

    # with open('data.json', 'r') as file:
    #     data = json.load(file)

    # print(data[0]['last_name'])

main()


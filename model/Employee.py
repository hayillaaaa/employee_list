class Employee:
    def __init__(self, last_name, first_name, address, city, country, birthdate, department_id):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.city = city
        self.country = country
        self.birthdate = birthdate
        self.department_id = department_id

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}, Department ID: {self.department_id}"
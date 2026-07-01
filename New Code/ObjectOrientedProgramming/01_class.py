# Class : Class is a blue print or a template.
# Eg: Form for an exam that contains name, age, electives, father's name etc...

# Object : Specific instance created from a template (class).
# Eg: Form which contains the data for John Doe

class Employee:
    company = "Google"
    def get_Salary(self):
        print(self)
        return 250000;

print("Creating a Emp 1...")
e1 = Employee()
print("E1 : ",e1.get_Salary())
print(e1)
print("Creating Emp 2...")
e2 = Employee()
print("E2 : ",e2.get_Salary())
print(e2)

"""
    this is simple program in python for oops implementation

    submitted by : suman kumar
    date : 1 january 2017
    time : 9 pm
"""

class Employee:
    
    emp_count = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count = Employee.emp_count + 1

    def count_emp(self):
        #print "total employee ", Employee.emp_count
        print "total employee %d " %Employee.emp_count # both line works   
    
    def emp_details(self):
        print "name ", self.name
        print "salary ", self.salary

emp1 = Employee("raju",10000)
emp2 = Employee("kaju",20000)
emp3 = Employee("maju",30000)

emp1.name = "sumti"
#del emp1.salary #delete salary attribute of emp1

print Employee.emp_count
emp1.count_emp()
emp2.count_emp()
#print emp1.name
emp1.emp_details()
emp2.emp_details()



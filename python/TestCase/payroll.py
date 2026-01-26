#object oriented programming

import unittest

class Employee:
    
    # variables
    company = "GRETB"
    taxRate = 0.2

    def __init__(self, empNo, empName, hoursWorked, rateOfPay):
        self.empNo = empNo
        self.empName = empName
        self.hoursWorked = hoursWorked
        self.rateOfPay = rateOfPay
        self.grossPay = 0
        self.nettPay = 0

    def welcomeMessage():
        print("Welcome to the Payrolls R Us made by" , Employee.company)
        print("The best payroll system on the web!")   

    def calcGross(self):
        self.grossPay = self.hoursWorked * self.rateOfPay

    def calcNettPay(self):
        self.nettPay = self.grossPay - (self.grossPay * self.taxRate)

    def printPaySlip(self):
         print("----- PAY SLIP -----")
         print("Employee Number:", self.empNo)
         print("Employee Name:", self.empName)
         print("Hours Worked:", self.hoursWorked)
         print("Rate of Pay:", self.rateOfPay)
         print("Gross Pay:", self.grossPay)
         print("Nett Pay:", self.nettPay)

    def exitMessage():
        print("Thank you for using the Payroll System ", Employee.company, " .exiting now...")

class Manager(Employee):
        def __init__(self, empNo, empName, hoursWorked, rateOfPay, bonus):
            super().__init__(empNo, empName, hoursWorked, rateOfPay)
            self.bonus = bonus

        def calcGross(self):
            super().calcGross()
            self.grossPay 

        def calcNettPay(self):
            super().calcNettPay()
            self.nettPay += self.bonus

        def printPaySlip(self):
            super().printPaySlip()
            print("Bonus:", self.bonus)

# main program
def main():
    Employee.welcomeMessage()

    employeeType = input("Are you an Employee or a Manager? ((E)mployee/(M)anager): ").strip().upper()
    empNo = input("Enter Employee Number: ")
    empName = input("Enter Employee Name: ")
    hoursWorked = float(input("Enter Hours Worked: "))
    rateOfPay = float(input("Enter Rate of Pay: "))

    if employeeType == "M":
        bonus = 100
        employee = Manager(empNo, empName, hoursWorked, rateOfPay, bonus)
    else:
        employee = Employee(empNo, empName, hoursWorked, rateOfPay)

    employee.calcGross()
    employee.calcNettPay()
    employee.printPaySlip()

    Employee.exitMessage()   
main()

class TestPayroll(unittest.TestCase):

    #test 1
    def test001(self):
        print("Test 1 : Employee name entered")
        emp = Employee("001", "Evan", 35, 15.0)
        self.assertNotEqual(emp.empName, "")

    #test 2
    def test002(self):
        print("Test 2 : Gross pay calculation")
        emp = Employee("002", "Alice", 40, 20.0)
        emp.calcGross()
        self.assertEqual(emp.grossPay, 800.0)  

    #test 3
    def test003(self):
        print("Test 3 : Nett pay calculation with tax")
        emp = Employee("003", "Bob", 50, 10.0)
        emp.calcGross()
        emp.calcNettPay()
        self.assertEqual(emp.nettPay, 400.0)

    #test 4
    def test004(self):
        manage = Manager("004", "Charlie", 45, 30.0, 200)
        manage.calcGross()
        manage.calcNettPay()
        print("Test 4 : Manager nett pay calculation with bonus")
        self.assertEqual(manage.nettPay, 1280.0)

    #test 5
    def test005(self):
        manage = Manager("005", "Diana", 60, 25.0, 300)
        self.assertIsInstance(manage, Manager)
        print("Test 5 : Manager object created when M is selected")

if __name__ == '__main__':
    unittest.main()
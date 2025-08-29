class Calculator:
    def _init_(self):
        self.num1 = 0
        self.num2 = 0
        self.operation = ''

    def get_input(self):
        try:
            self.num1 = float(input("Enter the first number: "))
            self.num2 = float(input("Enter the second number: "))
            self.operation = input("Choose an operation (+, -, *, /): ")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return False
        return True

    def calculate(self):
        if self.operation == '+':
            return self.num1 + self.num2
        elif self.operation == '-':
            return self.num1 - self.num2
        elif self.operation == '*':                                             
            return self.num1 * self.num2
        elif self.operation == '/':
            if self.num2 != 0:
                return self.num1 / self.num2
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation"

    def display_result(self, result):
        print("Result:", result)
calc = Calculator()
if calc.get_input():
    result = calc.calculate()
    calc.display_result(result)

class PAYECalculator:
    def __init__(self):
        self.paye_upper_bands = {
            30000: 0.00,
            300000: 0.07,
            600000: 0.11,
            1100000: 0.15,
            1600000: 0.19,
            3200000: 0.21,
        }

    def calculate_paye(self, gross_income):
        rate = self.get_income_paye_rate(gross_income)
        return rate * gross_income

    def get_income_paye_rate(self, gross_income):
        for income_level, rate in self.paye_upper_bands.items():
            if gross_income <= income_level:
                return rate

    def run_on_command_line(self):
        salary = float(input("Enter Gross Income: "))
        paye = self.calculate_paye(salary)
        print(f"PAYE of {salary:,} is {paye:,.2f}")


if __name__ == "__main__":
    paye_calculator = PAYECalculator()
    paye_calculator.run_on_command_line()
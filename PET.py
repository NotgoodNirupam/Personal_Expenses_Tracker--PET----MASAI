import json
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class PersonalExpenseTracker:
    def __init__(self, data_file="expenses.json"):
        self.data_file = data_file
        self.expenses = []
        self.load_expenses()
        self.necessities = ["food", "rent", "utilities", "transport"]
        self.luxuries = ["gadgets", "entertainment", "vacation"]
        self.luxury_alternatives = {
            "gadgets": "Consider refurbished gadgets.",
            "entertainment": "Try free or discounted events.",
            "vacation": "Opt for local or off-season trips."
        }

    def add_expense(self, amount, category, date=None):
        if not date:
            date = datetime.now().strftime('%Y-%m-%d')
        expense = {"amount": amount, "category": category, "date": date}
        self.expenses.append(expense)
        self.save_expenses()
        print(f"Added: {expense}")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return
        print("Your expenses:")
        for idx, expense in enumerate(self.expenses, start=1):
            print(f"{idx}. {expense['date']} - {expense['category']}: {expense['amount']:.2f}")

    def generate_monthly_report(self, month, year):
        monthly_expenses = [
            expense for expense in self.expenses
            if datetime.strptime(expense["date"], "%Y-%m-%d").month == month
            and datetime.strptime(expense["date"], "%Y-%m-%d").year == year
]

        if not monthly_expenses:
            return "No expenses found for the specified month."

        total = sum(expense["amount"] for expense in monthly_expenses)
        necessities = [
            expense for expense in monthly_expenses if expense["category"] in self.necessities
        ]
        luxuries = [
            expense for expense in monthly_expenses if expense["category"] in self.luxuries
        ]

        report = f"Monthly Expense Report ({month}/{year})\n"
        report += f"Total Expenses: Rs.{total:.2f}\n\nNecessities:\n"
        for item in necessities:
            report += f"- {item['date']} - {item['category']}: Rs.{item['amount']:.2f}\n"

        report += "\nLuxuries:\n"
        for item in luxuries:
            report += f"- {item['date']} - {item['category']}: Rs.{item['amount']:.2f}\n"

        report += "\nSuggested Alternatives for Luxuries:\n"
        for item in luxuries:
            suggestion = self.luxury_alternatives.get(item["category"], "No alternative available.")
            report += f"- {item['category']}: {suggestion}\n"

        return report

    def send_email_report(self, email, report):
        sender_email = "nirupammahato004@gmail.com"
        sender_password = "sacz mylk plef lpjt"

        try:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = email
            msg['Subject'] = "Monthly Expense Report"

            msg.attach(MIMEText(report, 'plain'))

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, email, msg.as_string())

            print("Email sent successfully!")
        except smtplib.SMTPAuthenticationError:
            print("Authentication error: Check your email and password.")
        except smtplib.SMTPException as e:
            print(f"SMTP error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def save_expenses(self):
        with open(self.data_file, "w") as f:
            json.dump(self.expenses, f, indent=4)

    def load_expenses(self):
        try:
            with open(self.data_file, "r") as f:
                self.expenses = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.expenses = []

def main():
    tracker = PersonalExpenseTracker()

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Generate Monthly Report")
        print("4. Send Monthly Report via Email")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
            tracker.add_expense(amount, category, date)
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year (e.g., 2023): "))
            report = tracker.generate_monthly_report(month, year)
            print(report)
        elif choice == "4":
            email = input("Enter recipient email: ")
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year (e.g., 2023): "))
            report = tracker.generate_monthly_report(month, year)
            tracker.send_email_report(email, report)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
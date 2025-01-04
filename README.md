# Personal_Expenses_Tracker--PET----MASAI
As my first project and to make it beginner friendly, I created a Personal Expenses Tracker. A Personal Expense Tracker is a tool designed to help individuals manage and monitor their financial spending. 


Personal Expenses Tracker
Overview
The Personal Expenses Tracker is a Python-based application designed to help users manage their daily expenses. It provides features to add, view, and analyse expenses, generate monthly reports, and send reports via email. This tool is ideal for individuals looking to gain better control over their finances.
________________________________________
Features
1.	Add Expenses:
o	Record expenses by amount, category, and date.
o	Categories include necessities (e.g., food, rent) and luxuries (e.g., gadgets, vacations).
2.	View Expenses:
o	Display a list of all recorded expenses with date, category, and amount.
3.	Generate Monthly Reports:
o	View total expenses for a specified month and year.
o	Categorize expenses into necessities and luxuries.
o	Provide alternative suggestions for luxury expenses to save money.
4.	Send Reports via Email:
o	Automatically email monthly reports to a specified recipient.
5.	Persistent Data Storage:
o	Stores all expenses in a JSON file for retrieval and analysis.
________________________________________
Installation
Prerequisites
•	Python 3.x
•	Internet connection (for email functionality)
Steps
1.	Clone or download the repository.
2.	Install required libraries:
pip install -r requirements.txt
(If a requirements.txt file is not provided, ensure you install the following manually: smtplib, json.)
3.	Run the script:
python personal_expenses_tracker.py
________________________________________
Usage
Main Menu
1.	Add Expense:
o	Enter the expense amount, category, and date (optional; defaults to today).
2.	View Expenses:
o	Lists all recorded expenses.
3.	Generate Monthly Report:
o	Specify a month and year to generate a detailed report.
4.	Send Monthly Report via Email:
o	Provide recipient's email address and the month/year for the report.
5.	Exit:
o	Quit the application.
________________________________________
Email Configuration
To use the email functionality:
1.	Update the script with your email credentials:
2.	sender_email = "your_email@example.com"
sender_password = "your_password"
3.	For Gmail Users:
o	Enable App Passwords:
	Go to Google Account Security.
	Enable 2-Step Verification.
	Generate an App Password and use it in place of your regular password.
4.	Verify SMTP settings:
o	Server: smtp.gmail.com
o	Port: 587
________________________________________
Data Storage
•	All expenses are saved in a JSON file (expenses.json).
•	Format example:
•	[
•	  {"amount": 50, "category": "food", "date": "2023-12-01"},
•	  {"amount": 150, "category": "gadgets", "date": "2023-12-05"}
]
________________________________________
Troubleshooting
1.	Email Not Working:
o	Verify email credentials and SMTP settings.
o	Use an App Password if using Gmail.
o	Ensure network or firewall isn't blocking SMTP traffic.
2.	Date Parsing Issues:
o	Ensure all dates follow the format "%Y-%m-%d".
3.	JSON File Corruption:
o	If expenses.json becomes unreadable, delete or fix it manually. The app will recreate the file.
________________________________________
Future Enhancements
1.	Add graphical visualizations for expense trends.
2.Support multiple user profiles.
3.Cloud-based storage for syncing across devices.
________________________________________
Contribution
Contributions are welcome! Please fork the repository and submit a pull request for review.
________________________________________
Contact
For queries or feedback, please email nirupammahato004@gmail.com


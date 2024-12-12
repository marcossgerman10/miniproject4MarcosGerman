# INF601 - Advanced Programming in Python  
## Marcos German  
## Mini Project 4  

# Habit Tracker  

A web application built using Django that allows users to track their habits, monitor their streaks, and gain insights into their progress.  

## Description  

This habit tracker application provides a user-friendly interface for creating, updating, and deleting habits. Users can also view their progress via dynamic insights and statistics, such as daily, weekly, and monthly streaks, and monitor their habits using a visually enhanced Bootstrap layout. A user authentication system ensures a personalized experience, allowing users to log in and manage their data securely.  

## Getting Started  

### Dependencies  

Ensure you have the following installed before proceeding:  

- **Python 3.10+**  
- **Django 4.2+**  
- Bootstrap (integrated via CDN)   

Install Python dependencies via pip:

```
pip install -r requirements.txt
```

### Installing
Clone the project from the GitHub repository:
```
git clone https://github.com/marcossgerman10/miniproject4MarcosGerman.git  
```
```
cd habit_tracker  
```
-Perform database migrations:
```
python manage.py makemigrations  
python manage.py migrate  
```

-Create a superuser for accessing the admin panel:
```
python manage.py createsuperuser  
```
-Start the development server:
```
python manage.py runserver  
```
### Executing Program
Access the application in your browser at:

http://127.0.0.1:8000/  

## Usage

Use the navigation bar to:

Add new habits.
View habit insights and streaks.
Edit or delete existing habits.
Logout.


## Authors
Marcos German

## Version History
1.0
Initial Release
Basic CRUD functionality for habits, user authentication, and insights page
Styled using Bootstrap

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

# DBS-HotelManagement
# Introduction

The Website application is built using Python for the backend logic and MySQL for the database management and the frontend is html css. Python libraries such as Flask and jinjar,used to develop the system. MySQL will be used for creating and managing the database for storing hotel-related data such as  admin login deatil ,room details, guest information, billing transactions, room services.
The system will provide a user-friendly interface for hotel staff to manage operations efficiently, reduce human errors, and improve guest experience. It will also generate reports and analytics to help hotel management make data-driven decisions for optimizing revenue and expenses.
Overall, the hotel management system based on Python and MySQL will automate and streamline hotel operations, resulting in improved performance, reduced costs, and enhanced guest satisfaction.

# Requirements

This Project requires the following tools:

+ Python
+ MySQL
+ Flask = 2.2.3
+ Flask-MySQLdb = 1.0.1
+ Jinja2 = 3.1.2
+ mysqlclient = 2.1.1

# Features
## Admin Specification

### Admin can do the following things: 
* Admin can login by their login details
![login](https://user-images.githubusercontent.com/127228884/232310021-5c8615d9-0530-49cf-8eca-0e9dd67a0b87.jpg)
## Dashboard Specifications
* This dahsborad will works when admin get logged in and later process the features according to customers requirements.
![dashboard](https://user-images.githubusercontent.com/127228884/232312986-f7dcdf4e-d2bd-46f5-8b12-754c76e82f2e.jpg)

## Room Booking
In this section hotel staff takes the detalis of the customer and select the room on customer permission and process the booking
![logobook](https://user-images.githubusercontent.com/127228884/232313500-69d77bca-8a60-4dea-a628-3e341493ac0e.jpg)
![book](https://user-images.githubusercontent.com/127228884/232313532-8b215ae7-21af-410d-9464-4db7de95d4ea.jpg)

+ Room services
+ guest count
+ Room information
+ Room facilities

# Steps to run the Project
## Follow these steps to run the project
```
$  Reach to the folder cmd 
$  venv/scripts/activate 
$  pip install -r requirements.txt 
$  set flask_app=app.py
$  flask run

```
### Step 2: Make Sure that you have a MySQL Server up and running either in your local computer or hosted remotely
By default, a flask application runs on port `5000` on `localhost`. So head over to http://localhost:5000 and start using!

# Screenshots

# Contributions
+ Aneela Hameed (10625393) (https://github.com/Aneela106)
+ Fahd Mansoor Khan (10637537) (https://github.com/fahdkhan98)
+ Archana Devaraj Gowda (10625916) (https://github.com/paapu12)

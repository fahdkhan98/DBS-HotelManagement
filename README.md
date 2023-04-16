# DBS-HotelManagement
# Introduction
We have designed a Hotel Management system using Python, Flask, HTML, CSS, and Java Script. It is a web-based application that is designed to manage the day-to-day operations of a hotel. This application helps the staff to manage their hotel operations more efficiently by providing them a user-friendly interface to handle tasks such as room information, room reservations, manage customer check-ins record, manage in house food billing and room facilities provided to the guest.

The system will provide a user-friendly interface for hotel staff to manage operations efficiently, reduce human errors, and improve guest experience. It will also generate reports and analytics to help hotel management make data-driven decisions for optimizing revenue and expenses.

# Technologies Implemented
+ Python : Python is a powerful programming language that is widely used for web development. Flask is a popular web framework in Python that simplifies web application development. HTML, CSS, and JS are the standard web technologies used to create the user interface of a web application.
+ HTML : HTML (Hypertext Markup Language) is a standard markup language used to create the structure and content of web pages. HTML defines the elements and attributes that are used to define the content of a web page, including headings, paragraphs, images, links, and more.
+ CSS : CSS (Cascading Style Sheets) is a style sheet language used to describe the presentation of HTML or XML documents. CSS allowed developers to apply styles to web pages, such as font styles, colors, layout, and more, to improve the appearance and user experience of the website.
+ Java Script : Java Script (JavaScript) is a high-level programming language used to create interactive and dynamic effects on web pages. It is commonly used to create client-side scripts that run on the user's web browser, such as form validation, animations, and more.
+ Flask : Flask is a micro web framework written in Python. It is used to build web applications quickly and easily, and provides tools and libraries for handling web requests, session management, database integration, and more. Flask is lightweight and easy to learn, making it a popular choice for building web applications.
In our Hotel Management System, Flask is used to create routes for different pages and functions of the application. For example, Flask can be used to create routes for the login page, reservation page, room availability page, and more. Flask also allows for the creation of dynamic web pages that can be updated in real-time based on user input or database changes.

We have developed a Hotel check-in management website which allows the hotel management add room availability, check-in the walk-in customer and assign  to check-in a walkin customer into a hotel depending on the availability of rooms  The Website application is built using Python for the backend logic and MySQL for the database management and the frontend is html css. Python libraries such as Flask and jinjar,used to develop the system. MySQL will be used for creating and managing the database for storing hotel-related data such as  admin login deatil ,room details, guest information, billing transactions, room services.
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
* In this section hotel staff takes the detalis of the customer and select the room on customer permission and process the booking
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

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

# Application Requirements to execute the code
+ Visual Studio Code
+ Python
+ MySQL
+ Flask = V 2.2.3
+ Flask-MySQLdb = V 1.0.1
+ Jinja2 = V 3.1.2
+ mysqlclient = V 2.1.1
+ Xampp = V 3.3.0

# Features
## Login Page (index.html)
This login page is used by Admins only to authenticate themselves to create a new booking and make changes to the existing bookings.

![image](https://user-images.githubusercontent.com/127228884/232329917-a001183c-5378-46c8-9cef-0c6b853b1b46.png)

## Check Info (checkinfo.html)
This page is used to view the details of the customer without logging in as admins only by entering the guest ID which will be generated for each checked-in customer. 

![Check info](https://user-images.githubusercontent.com/127228884/232332696-489c725b-7989-4fa2-a19d-78de272ede60.png)

## Dashboard (dashboard.html)
The dashboard page is accessible only by the admin post authenticating themselves from the login page. the Dashboard page consists options to reserve a room for a new customer, view the list checked-in guests, view the room details & facilities provided and order choose and order food for room service.

![dashboard](https://user-images.githubusercontent.com/127228884/232336039-7eb2142b-b980-48ee-9609-6d98d6af5c61.png)

## Create Booking (booking.html)
This page allows the admin to enter the details of the guest and choose the room required as per the customers need.

![Booking](https://user-images.githubusercontent.com/127228884/232335128-7ad4715e-2ea8-4805-8dd1-d6a97fb3a1ef.png)

## Guest Count (guestlist.html)
This page allows the hotel management to view the information of rooms utilised, details of the guests (checked-in & checked-out dates) and their Guest ID.

![image](https://user-images.githubusercontent.com/127228884/232336401-76b83f45-2bee-4cdd-81ac-e8318f578d24.png)

## Rooms Information (roomsinfo.html)
This page provides details of the rooms and the facilities provided in the same.

![rooms info](https://user-images.githubusercontent.com/127228884/232336457-68e584e0-4de3-432c-a0b3-6c188b8944b6.png)

# Steps to run the above code
## Execute the below steps in Visual Studio Code Terminal
+ Extract the contents of the .zip file into a folder
+ Navigate to the folder where the files exatracted from .zip are present using the cd function  
```
$ cd C:\folderpath
```
## Install and Activate Flask by typing the below commands in the Visual Studio Code Terminal
```
$ pip install flask
$ python -m venv venv 
$ venv/scripts/activate 
$ pip install -r requirements.txt 
$ set flask_app=app.py
$ flask run
```
### Step 2: Make Sure that you have a MySQL Server up and running either in your local computer or hosted remotely
By default, a flask application runs on port `5000` on `localhost`. So head over to http://localhost:5000 and start using!


# Contributions
+ Aneela Hameed (10625393) (https://github.com/Aneela106)
+ Fahd Mansoor Khan (10637537) (https://github.com/fahdkhan98)
+ Archana Devaraj Gowda (10625916) (https://github.com/paapu12)

# Overview
This project is my Stage 0 task for the **HNG13 Backend Track**.
It's a simple RESTFUL API built with **Python (Flask)** that returns my profile information and a random cat fact fetched from an external API.

___

## Endpoint
**GET** `/me`
Returns a JSON response with: 
- My user details (email, name, stack)
- A dynamic cat fact from the Cat Facts API
- Current UTC timestamp

Example response
````json
{
"status": "success",
"user": {
"email": "Thomasdreh@gmail.com",
"name": "Osakinle Oluwadare Thomas"
"stack": "Python/Flask"
},
"timestamp": "2025-10-16T12:34:56.7892",
"fact": "Cats sleep for 70% of their lives."

Tech Stack
Language: Python
Framework: Flask
External API: Cat Facts API
Hosting: Railway

Setup Instructions
1. Clone the repository
git clone https://github.com/Thomas-byt/hng13-backend-task.git
cd hng13-backend-task

2. Install dependencies
pip install -r requirements.txt

3 Run the app locally
python app.py
visit: http://127.0.0.1:5000/me

Live Demo
https://your-railway-app-url.up.railway.app/me

Contact
Name: Osakinle Oluwadare Thomas
Email: Thomasdreh@gmail.com
Stack: Python/Flask

What I learned
1. How to build a RESTful API endpoint
2. How to consume external APIs dynamically
How to return JSON responses and handle errors
How to deploy a live app using Railway

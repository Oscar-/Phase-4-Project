# Phase-4-Project

## A one sentence description of your app.
RhythmRadar is an interactive music review app that allows users to rate and comment on music while providing insights into the song's historical impact and popularity. 

## RhythmRadar Setup Guide

# Prerequisites

Ensure you have the following installed on your system:

- Node.js and npm: For managing JavaScript dependencies and running the React app.

- Python 3.8.x: Required for running the Flask backend.

- pipenv: For managing Python dependencies and virtual environments.

## Fork the Repository

Before you begin, you need to fork the repository to your own GitHub account. This will allow you to make changes and push them to your own fork.

1. Go to the RhythmRadar repository on GitHub.

2. Click the "Fork" button in the upper right corner of the page.

Once forked, clone your forked repository to your local machine:

# git clone git@github.com:Oscar-/Phase-4-Project.git
# cd Phase-4-Project

## Backend Setup (Flask)

1. # Set Up the Python Environment

Install dependencies and set up the virtual environment using pipenv:

# pipenv install

# pipenv shell
      
2. Set Up the Database

Initialize the database with the seed data:

python seed.py

3. # Run the Flask Server

Use honcho to start the server with the Procfile.dev configurations:

# honcho start -f Procfile.dev

The Flask server should now be running at http://127.0.0.1:5555.

## Frontend Setup (React)

1. Navigate to the Frontend Directory

From the root of the project, go to the React app directory:

# cd client

2. Install Dependencies

Install the required npm packages:

# npm install

3. Start the React Development Server

Start the React development server:

# npm start

The React app should now be running at http://localhost:3000.

## Proxy Configuration

The React app uses a proxy to forward API requests to the Flask backend, which is configured in package.json: 

# "proxy": "http://localhost:5555"

This setup helps avoid CORS issues by forwarding API requests made by the React frontend to the Flask backend server.

## Connecting Frontend and Backend

Ensure that the backend Flask server is running before starting the React app. The React app will make API requests to the Flask server to fetch and send data.

 - API Endpoints: Make sure the API endpoints used in your React app match those exposed by the Flask backend.

## Environment Configuration

You might need to set up environment variables for your Flask app. Create a .env file in the server directory and include any necessary configurations. An example .env file might look like this:

# FLASK_APP=app.py
# FLASK_ENV=development
# DATABASE_URL=sqlite:///yourdatabase.db

## Procfile.dev

Ensure you have a Procfile.dev in your root directory with the following content:

# web: PORT=3000 npm start --prefix client
# api: gunicorn -b 127.0.0.1:5555 --chdir ./server app:app

This configuration allows you to run both the frontend and backend servers concurrently.

## Troubleshooting

- Port Conflicts: Ensure that ports 3000 (React) and 5555 (Flask) are not being used by other applications.

- CORS Issues: If you encounter CORS issues, make sure the flask-cors package is properly configured in your Flask app.

## Additional Notes

- For Production: For production deployment, consider using Docker and a cloud provider or hosting service.

- Testing: Ensure you run tests for both the frontend and backend to verify that everything is functioning as expected.


## Our wireframe
![image](https://github.com/user-attachments/assets/a428fc1d-0286-4f13-9ffe-e5308592ade9)
![image](https://github.com/user-attachments/assets/aa73d6fa-4a76-4534-a7d6-f0d15a0d58ee)

## User Stories
![image](https://github.com/user-attachments/assets/8da3bd55-7258-468e-9498-200ab2280fbd)

## React Tree Diagram
<img width="1244" alt="Screenshot 2024-09-12 at 2 30 14 AM" src="https://github.com/user-attachments/assets/37dcb584-17c8-40fe-be5e-10f2742dd515">


## React Routes
<img width="717" alt="Screenshot 2024-09-09 at 9 48 41 AM" src="https://github.com/user-attachments/assets/20854ecf-d882-4bf2-b1a2-1b68a783e843">


## Our schema
![image](https://github.com/user-attachments/assets/ee764a59-7ffc-430a-b9f7-fd6c0bad93a0)

## A list of your API routes (includes HTTP Verb, Endpoint, Purpose)4
<img width="701" alt="Screenshot 2024-09-09 at 9 50 10 AM" src="https://github.com/user-attachments/assets/a5b964cb-2c23-43b3-9c35-6d942cd4014b">


## Three stretch goals
1. User Authentication 
2. Lyrics 
3. Mp3 - play button 

## Our Kanban Board
![image](https://github.com/user-attachments/assets/566e27ec-9ed9-42ca-bd20-23d5fd0c9ff5)

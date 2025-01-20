# Job Board

This is a simple Django job board app that lists the jobs fetched from a REST API.

## Setup Instructions

To run the project, run the following commands sequentially in terminal in root directory of this project:

1.  `docker build . -t jobboard`
2.  `docker run -d jobboard -p 8000:8000 jobboard`

If you don't have Docker installed on your system, the following instructions apply:

1. `pip install -r requirements.txt`
2. `cd jobboard; python manage.py runserver`

Navigate to **localhost:8000** to run the web app.

## Steps to make production ready

Although the exact steps would depend on the requirements for the web app, here are a few that I would necessarily implement to make this production ready:

1. Use a database to store jobs instead of flat file
2. Use `python-dotenv` to implement env variables
3. Implement AuthN and AuthZ
4. Implement API security
   - Setup CORS
   - Setup Rate Limiting
   - Add a reverse proxy
5. Implement a CI/CD pipeline in github or ADO
6. Setup test/staging/prod environments for the app
7. Add unit tests for each module
8. Add integration tests
9. Setup end-end tests via selenium/cypress
10. Add a Cache if the read/write ratio is heavy

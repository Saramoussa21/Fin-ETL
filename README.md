# FinETL

FinETL is an ETL (Extract, Transform, Load) application that extracts financial transaction data, processes it, and stores it for easy retrieval and analysis through a RESTful API. The project allows users to interact with financial data via an API, with JWT-based authentication to secure data access.

---

## Project Setup

### Prerequisites

- Python 3.8+
- PostgreSQL
- Docker (optional, if using Docker to run the project)

---

## Installation

### 1. Clone the Repository

```sh
git clone <repo-url>
cd FinETL

2. Create a Virtual Environment
sh
Copy code
python -m venv venv
source venv/bin/activate 

3. Install Dependencies
sh
Copy code
pip install -r requirements.txt
Database Setup
Create a PostgreSQL database and set up the credentials.
Update the .env file with your database credentials as follows:

makefile
Copy code
DATABASE_NAME=fintech
DATABASE_USER=fin_admin
DATABASE_PASSWORD=your_password
DATABASE_HOST=your_db_host
DATABASE_PORT=5432
Migrations
Run the following commands to set up the database schema:

sh
Copy code
python manage.py makemigrations
python manage.py migrate
Running the Project
1. Start the Django Development Server
To start the Django development server, run:

sh
Copy code
python manage.py runserver 0.0.0.0:8000
Then, open your web browser and navigate to:

sh
Copy code
http://<your-ip>:8000/
2. Create a Superuser for Admin Access
To access the Django admin panel, create a superuser:

sh
Copy code
python manage.py createsuperuser
After creating the superuser, open your browser and go to:

sh
Copy code
http://<your-ip>:8000/admin
Running the ETL Process
To execute the ETL process, run the following management command:

sh
Copy code
python manage.py etl
This command will initiate the ETL process that extracts, transforms, and loads data into your database.

API Usage
The project exposes a RESTful API for interacting with financial data.

Authentication
The API uses JWT (JSON Web Tokens) for authentication. You need to obtain a token before accessing the API.

Obtain Access Token
Send a POST request to the /api/token/ endpoint with your credentials to obtain a JWT token:

sh
Copy code
POST /api/token/
Refresh Token
To refresh your JWT token, send a POST request to the /api/token/refresh/ endpoint:

sh
Copy code
POST /api/token/refresh/
Available Endpoints
Retrieve Transactions for a Client
Send a GET request to the following endpoint:

sh
Copy code
GET /api/transactions/<client_id>/
Pass the JWT token in the Authorization header like this:

makefile
Copy code
Authorization: Bearer <your-access-token>
Running the Project with Docker
You can run the project using either a Dockerfile or Docker Compose.

Running with Dockerfile
1. Build the Docker Image
sh
Copy code
docker build -t django-fin-etl .
2. Run the Container
sh
Copy code
docker run -p 8000:8000 django-fin-etl
Access the application by opening your browser and navigating to:

sh
Copy code
http://<your-ip>:8000/
Running with Docker Compose
1. Create a docker-compose.yml File
If you haven't already, create a docker-compose.yml file to define the services.

2. Run Docker Compose
sh
Copy code
docker-compose up
This will build and start all services defined in the docker-compose.yml file.
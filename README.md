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
```

#### 2. Create a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  
```

#### 3. Install Dependencies

```sh
pip install -r requirements.txt
Database Setup
Create a PostgreSQL database and set up the credentials.
```

### Migrations
Run migrations to set up the database schema:

```sh
python manage.py makemigrations
python manage.py migrate
```

## Running the Project

#### 1. Start the Django Development Server
To start the Django development server, run:

```sh
python manage.py runserver 0.0.0.0:8000
```

Then, open your web browser and go to http://<your-ip>:8000/.

#### 2. Create a Superuser for Admin Access
To access the Django admin panel, create a superuser:

```sh
python manage.py createsuperuser
```

After creating the superuser, open your browser and go to:

```sh
http://<your-ip>:8000/admin
```

### Running the ETL Process
Run the following management command to execute the ETL process:

```sh
python manage.py etl
```

This command will initiate the ETL process that extracts, transforms, and loads data into your database.

### API Usage
The project exposes a RESTful API that can be used to interact with financial data.

#### Authentication
The API uses JWT (JSON Web Tokens) for authentication. You need to obtain a token before accessing the API.

#### Obtain Access Token
Send a POST request to the /api/token/ endpoint with your credentials to obtain a JWT token:

```sh
POST /api/token/
Refresh Token
```

#### Use this endpoint to refresh your token:

```sh
POST /api/token/refresh/
```

Available Endpoints
Retrieve Transactions for a Client
#### Send a GET request to the following endpoint:

```sh
GET /api/transactions/<client_id>/
```

#### You need to pass the JWT token in the Authorization header as:

```sh
Authorization: Bearer <your-access-token>
```

## Running the Project with Docker
There are two methods to run the project using Docker: Dockerfile and Docker Compose.

#### Running with Dockerfile

#### 1. Build the Docker Image

```sh
docker build -t django-fin-etl .
```

#### 2.Run the Container

```sh
docker run -p 8000:8000 django-fin-etl
```

### Access the application by opening your browser and navigating to:

```sh
http://<your-ip>:8000/
```

## Running with Docker Compose

#### 1. Create a docker-compose.yml File
If you haven't already, create a docker-compose.yml file to define the services.

#### 2. Run Docker Compose

```sh
docker-compose up
```

This will build and start all services defined in the docker-compose.yml file.

Troubleshooting
Common Issues
Unable to connect to the database: Ensure that the PostgreSQL server is running and the credentials in the .env file are correct.

Cannot access the application via the IP: Ensure that port 8000 is open on your firewall and network settings, and that ALLOWED_HOSTS in settings.py includes your IP address.

Error running Docker container: Ensure that no other container or service is using port 8000. Stop any existing container or modify the port number in the Docker command.

Page Not Found (404) when accessing the application: Make sure the URLs are correctly defined in the urls.py file and that you are navigating to a valid endpoint.

Additional Notes
Running Tests
To run tests for the project, you can use the following command:

```sh
python manage.py test
```

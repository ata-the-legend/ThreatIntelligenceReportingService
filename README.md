# Threat Intelligence Service

This project is a small threat intelligence service developed using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python. The service allows users to report and query suspicious IP addresses, and it stores the data in a PostgreSQL database. The API endpoints are protected with JWT (JSON Web Token) authentication to ensure secure access.

## Prerequisites

Before running this project, make sure you have the following prerequisites installed:

- Python 3.10 or higher
- PostgreSQL

## Getting Started

Follow the steps below to get the threat intelligence service up and running:

1. Clone the repository:

    ```
    git clone https://github.com/ata-the-legend/ThreatIntelligenceReportingService.git
    ```

2. Create a virtual environment (optional but recommended):
    ```
    cd threat-intelligence-service
    python3 -m venv venv
    source .venv/bin/activate
    ```
3. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Set up the PostgreSQL database:
   
- Create a new database in PostgreSQL.
    ```
    CREATE DATABASE ThreatIntel;
    ```

- Update the database configuration in `database.py` and `alembic.ini` file with your database details.
    ```
    postgresql://username:password@127.0.0.1:5432/ThreatIntel
    ```

5. Run database migrations to initialize the tables:
    ```
    alembic upgrade head
    ```
6. Generate a secret key for JWT authentication:

- In the terminal, run the following command:

    ```
    python -c "import secrets; print(secrets.token_urlsafe())"
    ```
    Copy the generated secret key.
7. Set the JWT secret key variable:

    Update SECRET_KEY variable in `config.py` file with your the secret key generated in the previous step.

8. Start the FastAPI server:
    ```
    python main.py
    ```

9. The service is now running locally. You can access the API documentation by visiting http://localhost:8000/docs in your web browser.

## API Development (FastAPI with JWT Authentication)

The FastAPI application has been developed with the following endpoints:

- `POST /report-ip`: Accepts an IP address and updates the SuspiciousIPs table. If the IP is already reported, it increments the `report_count` and updates `last_reported`.
- `GET /query-ip`: Takes an IP address and returns its details if present in the database.

These endpoints are protected with JWT authentication to ensure secure access.

## Authentication

To access the protected endpoints, you need to obtain a JWT token by sending a POST request to `/login` with valid credentials. The credentials include a username (which is email) and password. Upon successful authentication, the API will return a JWT token. Include this token in the `Authorization` header of subsequent requests as follows:

    Authorization: Bearer <token>
    
Replace `<token>` with the JWT token obtained during authentication.

## Contributing

Contributions to this project are welcome! If you find any issues or would like to add new features, feel free to open an issue or submit a pull request.

When contributing, please ensure that you follow the existing code style, write unit tests for new functionality, and update the documentation accordingly.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
# Threat Intelligence Service

This project is a small threat intelligence service developed using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python. The service allows users to report and query suspicious IP addresses, and it stores the data in a PostgreSQL database. The API endpoints are protected with JWT (JSON Web Token) authentication to ensure secure access.

## Prerequisites

Before running this project, make sure you have the following prerequisites installed:

- Python 3.10 or higher
- PostgreSQL

## Getting Started

#### Dockerized Version

Follow the steps below to get the threat intelligence service up and running:

1. Clone the repository:

    ```
    git clone https://github.com/ata-the-legend/ThreatIntelligenceReportingService.git
    ```
2. Change into the project directory:

   ```
   cd ThreatIntelligenceReportingService
3. Start the project with docker:

    ```
    docker compose up
4. The service is now running locally. You can access the API documentation by visiting http://localhost:8000/docs in your web browser.


#### Non-Dockerized Version

If you don't want to use Docker and prefer a non-dockerized setup, you can switch to the `non-dockerized` branch. The README file in the `non-dockerized` branch provides instructions for setting up the project without Docker.

To switch to the `non-dockerized` branch, run the following command:
```
git checkout non-dockerized
```
Once you're on the `non-dockerized` branch, follow the instructions in the README file to set up the project without Docker.

Please note that the non-dockerized version may have different requirements and instructions compared to the Dockerized version. Make sure to follow the appropriate instructions based on your preferred setup.

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
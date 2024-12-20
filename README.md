# Canva_calculator

This project is a FastAPI server with a calculator API. It supports basic arithmetic operations, with CORS enabled for all origins. The server can be run in development mode with auto-reloading.

## Features

- FastAPI server for handling API requests.
- Calculator routes for performing arithmetic operations (located in `apps.calculator.route`).
- CORS middleware to allow requests from any origin.
- Logging setup to track server activity.

## Setup and Installation

### Prerequisites

Make sure you have Python 3.7+ installed on your machine.

### Install dependencies

To install the necessary dependencies, create a virtual environment and install the packages via pip:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Requirements

The `requirements.txt` file should include the following (or similar versions):

```txt
fastapi
uvicorn
pydantic
```

## Configuration

The application requires the following environment variables to be set up:

- **SERVER_URL**: The base URL for the server (e.g., localhost).
- **PORT**: The port number for the server to run on (e.g., 8000).
- **ENV**: The environment type ("dev" for development, "prod" for production).

You can set them as environment variables or create a `.env` file in your project root. Here's an example `.env` file:

```ini
SERVER_URL=localhost
PORT=8000
ENV=dev
```


## Running the Server

To run the FastAPI server, execute the following command:

```bash
python main.py
```

## Accessing the API

Once the server is running, you can access it at:

Root endpoint: http://localhost:8000
This returns a simple status message, e.g., {"message": "Server is running"}.

Calculator endpoints: `http://localhost:8000/calculate`
The calculator API handles various arithmetic operations.

## Logging
The application uses Python's built-in logging module for logging. You can adjust the verbosity level (e.g., DEBUG, INFO, WARNING, or ERROR) by changing the log level in the code.

## CORS Middleware
CORS (Cross-Origin Resource Sharing) is enabled for all origins, which allows requests from any external domain.

### Example Request (GET method)
To test the server, you can hit the root endpoint with a GET request:
```bash
curl http://localhost:8000/
```
Response:

```json
{
  "message": "Server is running"
}
```

## Structure

├── apps
│   └── calculator
│       └── route.py  # Contains routes for calculator operations
├── constants.py  # Holds constant values like SERVER_URL, PORT, ENV
├── main.py  # Main application entry point
├── requirements.txt  # List of Python dependencies
└── .env  # Optional configuration file for environment variables

## License
This project is open-source and available under the MIT License.




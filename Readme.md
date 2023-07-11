# doordash Automation

Automate doordash tasks using the Multilogin software. This project consists of multiple components that work together to achieve automation.

## Components
1. Multilogin UI: User interface for managing browser profiles.
2. Multilogin Server: Server component for handling browser profile operations.
3. Backend Server: Custom server that interacts with the Multilogin API for doordash automation.
4. Python Scripts: Collection of Python scripts for various automation tasks.

## Prerequisites
Before using the automation system, make sure you have the following software installed on your system:

- Python 3.7: A programming language required for executing Python scripts.
- Node.js: A JavaScript runtime environment required for running the backend server and executing JavaScript-based automation scripts.
- MongoDB: A NoSQL database used for storing data required for the automation system.

Follow the installation instructions below for each prerequisite:

### Python 3.7
- Ubuntu:
  ```shell
  sudo apt update
  sudo apt install python3.7
  ```
- Windows/Mac: Download and install Python 3.7 from the official Python website (https://www.python.org).

### Node.js
- Ubuntu:
  ```shell
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
  source ~/.bashrc
  nvm install v16.13.1
  nvm alias default 16.13.1
  ```
- Windows/Mac: Download and install Node.js from the official Node.js website (https://nodejs.org).

### MongoDB
- Ubuntu: Follow the MongoDB installation guide for Ubuntu (https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu).
- Windows/Mac: Download and install MongoDB from the official MongoDB website (https://www.mongodb.com).

## Usage
Follow these steps to use the automation system:

1. Download and install Multilogin application:
    - Launch the Multilogin application and log in using your credentials.

2. Start the Multilogin Server:
    - For Linux:
        - Open a terminal.
        - Navigate to the Multilogin Server installation directory (`/opt/Multilogin/headless`).
        - Update the `app.properties` file in the `.multiloginapp.com` directory (`/home/%username%/.multiloginapp.com`).
            - Open the `app.properties` file in a text editor.
            - Add the following line, replacing `[PORT_NUMBER]` with the desired port number (10000 to 49151):
              ```shell
              multiloginapp.port=35000
              ```
            - Save the `app.properties` file.
        - Start the Multilogin Server by running the following command:
          ```shell
          ./headless.sh
          ```

3. Start the Backend Server:
    - Open a terminal/command prompt.
    - Navigate to the backend server directory.
    - Install dependencies by running the following command:
      ```shell
      npm install
      ```
    - Set up the environment variables in the `.env` file:
        - Ensure that the `MULTILOGIN_API` variable is set to the port number defined in the Multilogin Server's `app.properties` file (default: 35000).
        - Make sure the MongoDB port is set to 27017.
    - Start the server by running the following command:
      ```shell
      npm start
      ```

4. After the backend server is up, add proxies to the database so that the program can create new profiles with new proxies.
    - Use the following API endpoint (e.g., in POSTMAN) to add proxies:
        - Endpoint: POST `http://localhost:3001/proxy`
        - Payload:
          ```json
          {
            "host": "161.77.153.235",
            "port": "12323",
            "username": "14a23373005b8",
            "password": "1c6ff9bc33"
          }
          ```
          Replace the values with your proxy details. You can add as many proxies as you want using this endpoint.

5. Python Scripts:
    - Open a terminal/command prompt.
    - Navigate to the Python scripts directory.
    - Install dependencies by running the following command:
      ```shell
      pip install -r requirements.txt
      ```
    - Use the following Python scripts for automation tasks:
        - `main.py`: Execute various automation actions such as creating Multilogin profiles, doordash accounts, running warmup, crawling, profile photo upload, and media photo upload.
            - To run the script in a production environment, execute the following command:
              ```shell
              ENVIRONMENT=Prod python main.py
              ```
        - `warmup_scheduler.py`: Initiate the warmup process.
            - To run the script in a production environment, execute the following command:
              ```shell
              ENVIRONMENT=Prod python warmup_scheduler.py
              ```

Please refer to the documentation and code implementation for detailed instructions on each script.

## Additional Information
- Each profile requires a proxy. There should be an unused proxy available in the database to create a profile.
- All data is saved in the database, including doordash account details.
- If you want to remove a profile, please remove it from the database as well after removing it from the Multilogin GUI application.
- Once a proxy is used in profile creation, it will be marked as "is_used". If you want to reuse it, set "is_used" back to false in the database.

## Disclaimer
Use this automation system responsibly and comply with doordash's terms of service. Ensure that your actions are ethical and legal.

Feel free to customize the README file further to suit your needs.
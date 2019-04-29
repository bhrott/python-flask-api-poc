# Python Flask Api Poc

## Setup

After clone this project, follow these steps:

### Adding `.env` file

Create a file named `.env` in the root of the project with this content:

```
DB_CONNECTION=mongodb://localhost:27017/
JWT_SECRET=your-secret-hash-here
ENV_NAME=local
```

### Installing the dependencies

In the terminal, run:

```
pip install -r requirements.txt
```

### Running the database

This project uses mongodb as database. If you don't have mongodb installed in your machine, you can install or
use with the docker compose.

- Instaling local:
    - Follow this tutorial: https://docs.mongodb.com/manual/administration/install-community/
- Running from docker
    - Install docker using this tutorial: https://www.docker.com/products/docker-desktop
    - After install, run the docker and wait until is running.
    - Run the command `make run-db` in the root folder.
    
    
## Tech

- [Flask](http://flask.pocoo.org/) for http api handling.
- [Cerberus](http://docs.python-cerberus.org/en/stable/index.html) for schema validation.

# COMP-3005-Final-Project

This repo is a submission to a university project for the course COMP 3005 Database Management Systems at Carleton University

## Purpose

This project locally hosts a PostgreSQL server through a podman (preferred) or docker container.

The PostgreSQL server is initialized with a setup script by the podman container.

The project interacts with the PostgreSQL server using limited commands through a python application.

## Instructions

All commands are executed through the CLI using this repo's directory.

### Requirements

The following applications must be installed to run this project:
    - python3
    - podman
    - podman compose

### Python Setup

This project requires a python virtual environment with a pip package used to interact with PostgreSQL.

To automatically setup the python virtual environment, execute the following:
    - `./app/setup-python.sh`

### Database Setup

To launch the database, execute the following:
    - `./app/db-setup.sh`

### Running The App

Assuming the python setup command (above) has been ran, run the app with the following:
    - `./app/run-app.sh`

### Database Teardown

To stop the database, use the following CLI command:
    - `./app/db-teardown.sh`

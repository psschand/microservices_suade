# microservices
 
### Local Setup


### 1 Run with docker
    $ docker-compose build
    $ docker-compose up

### 2 Initial migration
    $ docker-compose exec reports python manage.py recreate_db


### 3 Populate data in databases
    $ docker-compose exec reports python manage.py populate_db


### Run Tests
    $ docker-compose exec reports python manage.py test


### Run flake8
    $ docker-compose run --rm reports flake8
   

### Services
Service name| Service endpoint|
-------|---|
swagger|http://localhost:8084/
reports|http://localhost:8081/v1/reports/
react UI|http://localhost:3000/

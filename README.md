## Backstage Test ##
###How to run ###

- Download and install python (>3.7). <br>
https://www.python.org/downloads/ <br>
Make sure to install `pip` (python package management tool) during installing python.
- Clone the project from its repository.
- In the project base folder run below command to install dependencies. <br>
`pip install -r requirements.txt`
- Migrate database
`python manage.py migrate`
- Run the server with the below command.
`python manage.py runserver` <br>
This should run the server on http://localhost:8000
- Test the endpoint with the below command.
curl --request GET 'http://localhost:8000/difference?number=10' <br>

Expected result.
```text
{
    "datetime": "2021-02-09 23:17:05",
    "value": 2640,
    "number": 10,
    "occurrences": 1
}
```

- Access http://localhost:8000 with browser. You will see the UI to query and see the result.
Type number in the input and click "query" button.
The result will be shown in the table.


### How it works ###

- This project uses sqlite3 for its database.
- When the request is received, it first checks the database if the "number" is already stored.
If then it adds 1 to the "occurrences" value of the "number" and return result.
If "number" is not stored in the database, which means the "number" has not requested yet, calculate the different value (between the sum of the squares of the first n natural numbers and the square of the sum of the same first n natural numbers) and store it in the database.

### Unit Test ###
`python manage.py test apps.service.tests.ServiceTestCase.test_service` <br>





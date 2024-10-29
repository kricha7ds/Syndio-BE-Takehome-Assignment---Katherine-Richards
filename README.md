# Syndio Backend App

Using the `employees.db` SQLite database in this repository with data that looks like the below:

```
sqlite> .open employees.db
sqlite> .schema employees
CREATE TABLE employees (id INTEGER PRIMARY KEY, protected_class TEXT, department TEXT, tenure INTEGER, performance INTEGER, compensation INTEGER);
sqlite> SELECT * FROM employees;
1|reference     | Engineering   | 21 | 1  | 177000
2|comparison    | Engineering   | 42 | 2  | 155725
3|reference     | Engineering   | 2  | 3  | 180000
4|comparison    | Engineering   | 34 | 4  | 220000
5|reference     | Engineering   | 9  | 5  | 130000
6|comparison    | Engineering   | 17 | 4  | 165000
...
```

Create an API with an endpoint `/pvalue` that:

- reads the employee data for employees belonging to a specified department from the `employees.db` SQLite database
- uses the employee data to run an OLS regression with independent variables `protected_class`, `tenure`, and `performance` and dependent variable `compensation` that includes all employees in the specified department
- returns the OLS model pvalue associated with `protected_class` rounded to 3 decimal places in a JSON response like the one below:

```
{"pvalue": 0.053}
```

You're welcome to use any libraries you'd like in your solution. While the provided dataset is clean, feel free to account for any edge cases you can think of (for example, how to deal with missing data).

If you're unfamiliar with OLS regressions, you may find [this resource](https://soc.utah.edu/sociology3112/regression.php) helpful.

## Requirements

- The API must take an environment variable `PORT` and respond to requests on that port.
- You provide basic setup instructions required to run the API.
- We can send an API request to your endpoint via `curl` (i.e. something similar to `curl localhost:$PORT/pvalue`) that returns the described response.

## Success

- We can run the API from your setup instructions
- The curl returns the described response
- The API is written in Python or Go

## Not Required

- Tests
- Logging, monitoring, or anything more than basic error handling

## Submission

- Respond to the email you received giving you this assessment with:
  - a zip file, or link to a git repo
  - instructions on how to setup and run the code (could be included w/ zip/git)
- We'll follow the setup instructions to test it on a local machine, then we'll get back to you.

## Notes

- Keep it simple.
- We expect this to take ~1-2 hours, please try and limit your effort to that window.
- If the API works, and returns what we requested, it's a success!
- We truly value your time and just want a basic benchmark and common piece of code to use in future interviews.
- If we bring you in for the next round of interviews we'll ask you some questions about your submission and also expand on it.

---

## Instructions

At the project root, do the following:

1. Create a virtual environment

```
python3 -m venv venv
```

2. Activate the virtual environment

```
source venv/bin/activate
```

3. Install app dependencies

```
pip install -r requirements.txt
```

4. Export environment variable with desired port

```
export FLASK_RUN_PORT=<desired_port>
```

5. Run the API

```
flask run
```

6. Make a request to the API on the desired port

```
curl --location 'http://localhost:5000/pvalue?department=engineering'
```

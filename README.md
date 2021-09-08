# Python + Flask API Boilerplate

Based on [Flask API Starter](https://github.com/cdagli/flask-api-starter)

# Requirements
Python 3.8+

```bash
pipenv install
pipenv run python src/server.py
curl localhost:8000/info
```

Included Helm Chart for CI/CD.
Default port is **8000** with hot reloading for DEV environment.

# Environment Variables
|Variable|Description|Default|
|---	|---	|---	|
|WORK_ENV| DEV, STAGE, TEST, PROD|None -> Defaults to DEV|

# Running Tests

```bash
pipenv run nose2
```
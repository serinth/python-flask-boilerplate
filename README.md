# Python + Flask API Boilerplate

Based on [Flask API Starter](https://github.com/cdagli/flask-api-starter)

# Requirements
Python 3.8+

```bash
pipenv install
pipenv run python src/server.py
curl localhost:8000/metrics/health
```

Included Helm Chart for CI/CD.
Default port is **8000** with hot reloading for DEV environment.

# Swagger Documentation
Swagger documentation is generated and provided by [flask-restx](https://flask-restx.readthedocs.io/)
https://localhost:8000/docs

# Environment Variables
|Variable|Description|Default|
|---	|---	|---	|
|WORK_ENV| DEV, STAGE, TEST, PROD|None -> Defaults to DEV|

# Running Tests

```bash
pipenv run nose2
```

## Building the Docker image

1. Generate a requirements.txt from the lock file:
```bash
pipenv lock -r > requirements.txt
```

2. Build the docker image
```bash
docker build -t mydomain.com/myimage:latest .
```

3. Running
```bash
docker run \
-e WORK_ENV="PROD" \
-p 8000:8000 \
mydomain.com/myimage:latest
```
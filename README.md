# Python + Flask API Boilerplate

Based on [Flask API Starter](https://github.com/cdagli/flask-api-starter)

```bash
pip install -r requirements.txt
python src/server.py
```

Included Helm Chart for CI/CD.
Default port is **8080** with hot reloading for DEV environment.

# Environment Variables
|Variable|Description|Default|
|---	|---	|---	|
|WORK_ENV| DEV, STAGE, TEST, PROD|None -> Defaults to DEV|

# Running Tests

```bash
pipenv run nosetests
```
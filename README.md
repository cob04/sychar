# Sychar

### A Bible Study application.


## Setting up 
1)  Create a Python virtual environment to separate the app's python dependencies from the host OS python dependencies.
    ref: [https://docs.python.org/3.10/library/venv.html](https://docs.python.org/3.10/library/venv.html)
    ```bash
    # at the root of the project run.
    python -m venv venv/sychar
    ```

2)  Activate the virtualenvironment
    ```bash
    source venv/sychar/bin/activate
    ```

3)  Install dependencies from PyPI
    ```bash
    pip install -r requirements.txt
    ```

## running tests
Make sure you have activated the projects virtualenvironment and all dependencies have been installed.
There are two methods:
1)  Generating test coverage reports
    ```bash
    coverage run -m pytest -v
    ```
    To see the coverage report
    ```bash
    coverage report -m
    ```

2)  No coverage report
    ```bash
    pytest -v
    ```

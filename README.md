# python_flask

## I. Requirements

```text
Windows or Windows server 2019
Python >= 3.7
Postgre SQL
```

### 1. Install python 3

-   Download the binaries: [python-3.8.10-amd64.exe](https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe)

-   Run the Executable installer, notes: check the 'Add Python 3.8 to PATH' check box to include the interpreter in the execution path.
-   Add Python to PATH environmental variables (manually):
    | Variable | Value | Notes |
    |----------------------|------------------------------------------------------------|--------------|
    | PATH | C:\Users\\[USER_PROFILE\]\AppData\Local\Programs\Python\Python38; C:\Users\\[USER_PROFILE\]\AppData\Local\Programs\Python\Python38\Scripts; | Path to python execution |

### 2. Install Oracle client and ODBC driver

-   Link to download:
    <https://www.enterprisedb.com/downloads/postgres-postgresql-downloads>

## II. Project structure

    .
    ├── common
    ├── controllers
    ├── static
    │   ├── images
    │   ├── css
    │   ├── js
    │   └── plugins
    ├── templates
    |   ├──screen1
    |   |  ├──index.html
    ├── .gitnore
    ├── app.py
    ├── README.md
    ├── requirements.txt        # Requirement packages
    ├── settings.py             # information of Database

## III. Extension for VS Code (for dev only)

-   Python Extension Pack: <https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack>
-   Pylint: <https://marketplace.visualstudio.com/items?itemName=ms-python.pylint>
-   Python snippets: <https://marketplace.visualstudio.com/items?itemName=frhtylcn.pythonsnippets>
-   Black Formatter: <https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter>
-   VS Code Counter: <https://marketplace.visualstudio.com/items?itemName=uctakeoff.vscode-counter>

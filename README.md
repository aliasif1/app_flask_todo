# Flaks Todo app

## Clone the repo 
```
git clone https://github.com/aliasif1/app_flask_todo.git
```

## Setup Virtual Environment 
```
virtualenv env 
source env/bin/activate
pip3 install flask flask-sqlalchemy
```

## setup the database 
```
python3
from app import db
db.create_all()
```

## start the server 
```
python3 app.py
```
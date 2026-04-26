# flask-backend-middle

# instruction

1. mkdir myproject
   cd myproject
   py -3 -m venv .venv

2. .venv\Scripts\activate

3. pip install -r requirements.txt

4. docker run --name flask-backend-middle -p 5432:5432 -e POSTGRES_PASSWORD=root -d postgres

5. CREATE DATABASE "flask-backend-middle-db";

6. flask db upgrade

7. flask --app main.py run

   flask --app main.py run --debug

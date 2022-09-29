#  Star Wars API

## Getting Started
1. ### Clone the repository
   ```
      git clone git@github.com:Philipotieno/star_wars_api.git
   ```
2. ### create a virtual environment
   ```
      python -m venv venv
   ```
3. ### Create a .env file and set variables as in the .env-example

4. ### Create postgres database
 ```
  $ psql postgres
  postgres=# CREATE USER your-user WITH PASSWORD 'your-password';
  postgres=# ALTER ROLE your-user SET client_encoding TO 'utf8';
  postgres=# ALTER ROLE your-user SET default_transaction_isolation TO 'read committed';
  postgres=# ALTER ROLE your-user SET timezone TO 'UTC';
  postgres=# CREATE DATABASE your-database-name;
  postgres=# GRANT ALL PRIVILEGES ON DATABASE your-database-name TO your-user;
  postgres=# \q
 ```
3. ### Install dependencies
   ```
      pip insatll -r requirements.txt
   ```
4. ### Activate the virtual environment
   ```
      source venv/bin/activate
   ```
5. ### Make Migrations
   ```
      python manage.py migrate
   ```
6. ### Run server
   ```
      python manage.py runserver
   ```
7. ### Test Using Postman
   ```http://127.0.0.1:8000/graphql/```
- Import the following Collection: [https://www.getpostman.com/collections/8e4608cd2283e03f96a2](https://www.getpostman.com/collections/8e4608cd2283e03f96a2)

## Screenshots

1. ### Create User
   ![Create User](https://github.com/Philipotieno/star_wars_api/blob/develop/images/create_user.png)

2. ### Authenticate User
   ![Authenticate User](https://github.com/Philipotieno/star_wars_api/blob/develop/images/auth_user.png)

   #### Authentication Header
      ```
         Authentication : JWT <token here>
      ```
3. ### List Users
   ![List Users](https://github.com/Philipotieno/star_wars_api/blob/develop/images/list_users.png)

4. ### Get All Star Wars People
   ![Get All People](https://github.com/Philipotieno/star_wars_api/blob/develop/images/get_all_people.png)
5. ### Search Person
   ![Search Person](https://github.com/Philipotieno/star_wars_api/blob/develop/images/search_person.png)
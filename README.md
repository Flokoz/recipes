
# Recipes

This project contains an API to add, edit, remove and list recipes and can also search the list of recipes.

## Requirements

- Python 3.9+ 
- Django 4.0 
- Django Rest 3.13 

## Installation
The documentation follows a Windows 10 environment based installation.

- After cloning the project, install the python requirements, using the command:

```
    pip install -r requirements.txt
```

### Run

To start the server, enter the folder containing the 'manage.py' file and use the following commands:

```
  python manage.py migrate
  python manage.py runserver
```

The first command will update the database and the second is responsible for initializing the server.

By default, the server uses localhost port 8000, which can be accessed through the addresses:

- http://127.0.0.1:8000/
- http://localhost:8000/


## API Reference

#### Create recipe

```http
  POST /recipes
```

| Parameter        | Type      | Description                             |
| :--------------- | :-------- | :-------------------------------------- |
| `chef`           | `string`  | **Required**. Chef name                 |
| `recipe_name`    | `string`  | **Required**. Recipe name               |
| `recipe`         | `string`  | **Required**. Recipe description        |
| `prepare_time`   | `integer` | **Required**. Recipe preparation time   |

#### Filters recipes by name and chef's name

```http
  GET /recipe-find
```

| Query Parameter      | Type           | Description                                              |                                              
| :------------------- | :--------------| :------------------------------------------------------- |
| `recipe_name`        | `string`       | **Optional**. Parameter to search recipes by name        |                                           
| `chef_name`          | `string`       | **Optional**. Parameter to search recipes by chef's name |                                           


## Running Tests

To run tests, run the following command inside the base folder

```bash
  pytest tests/ -v
```

  
## Authors

- [@Lucas Cota](https://github.com/Flokoz)


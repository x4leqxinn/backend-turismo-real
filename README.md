![Python](https://img.shields.io/badge/-Python-000000?style=flat&logo=python)
![JavaScript](https://img.shields.io/badge/-JavaScript-000000?style=flat&logo=javascript)
![HTML5](https://img.shields.io/badge/-HTML5-000000?style=flat&logo=html5)
![CSS3](https://img.shields.io/badge/-CSS-000000?style=flat&logo=css3)
![SQL](https://img.shields.io/badge/-SQL-000000?style=flat&logo=mysql)
![Git](https://img.shields.io/badge/-Git-000000?style=flat&logo=git)
![Github](https://img.shields.io/badge/-Github-000000?style=flat&logo=github) 
![Visual Studio Code](https://img.shields.io/badge/-VisualStudioCode-000000?style=flat&logo=.net)

***Backend Turismo Real*** es un proyecto creado utilizando Python 3.9.7 Trabajando en la validación, buenas prácticas y
mantenimiento de un backend pensado para integrar distintas plataformas.

( Portafolio de Título (10/08/2022) )

## Setup

- _Django_
- _Django restframework_
- _Oracle Database 19c_

## Run Locally

### Python

Create env
```
python3 -m venv venv
```

Install requirements
```
pip install -r requirements.txt
```

- Config your .env file

Drop and Create database
```
python manage.py system
```

Database migrations
```
python manage.py migrate --d turismo_real
```

Seeding Database
```
python manage.py seed
```

Server
```
python manage.py runserver
```


> Delete migrations
```bash
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
```
## Technologies
* Python 3.9
* HTML
* CSS
* Django
* Django RestFramework
* Oracle Database 19c

## Tools
* Visual Studio Code 
* Git 
* Github 

## Features

* Auth Token
* APIView
* Decorators 
* Serializers
* POST, PUT, PATCH, DELETE AND UPDATE Requests 
* Response Validations
* Models Crud
* ViewSets
* Generics Views
* Routers
* Sessions
* CORS Config
* Admin Site Config and Customization
* Send Emails

## Contributors
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/joacogithub2022"><img src="https://avatars.githubusercontent.com/u/113393198?v=4" width="100px;" alt=""/><br /><sub><b>Joaquin Reyes</b></sub></a><br /><a href="https://github.com/4lequinn/backend-turismo-real?author=joacogithub2022" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/lucasmenares"><img src="https://avatars.githubusercontent.com/u/47159689?v=4" width="100px;" alt=""/><br /><sub><b>Lucas Menares</b></sub></a><br /><a href="https://github.com/4lequinn/backend-turismo-real?author=lucasmenares" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/4lequinn"><img src="https://avatars.githubusercontent.com/u/66024934?v=4" width="100px;" alt=""/><br /><sub><b>Jorge Quintui</b></sub></a><br /><a href="https://github.com/4lequinn/backend-turismo-real?author=4lequinn" title="Code">💻</a></td>
  </tr>
</table>

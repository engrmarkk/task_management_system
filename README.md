# Task Management System API


<!-- Back to Top Navigation Anchor -->

<a name="readme-top"></a>


<!-- https://user-images.githubusercontent.com/100721103/200149633-373db975-c47f-43a7-9288-f6cbd16e0410.mp4 -->

<br><br>
<!-- Project Shields -->
<div align="center">

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Twitter][twitter-shield]][twitter-url]

[//]: # ([![Twitter][twitter-shield2]][twitter-url2])

</div>

<br />


---

<!-- Table of Contents -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-Scissor API">About the project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#features">Features</a></li>
      </ul>
     <!-- <li><a href="#demo">Demo</a></li> -->
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#project-structure">Project Structure</a></li>
         <li><a href="#endpoints">Endpoints</a></li>
      </ul>
    <!-- <li><a href="#shots">Shots</a></li> -->
    <li><a href="#contact">Contact</a></li>
  </ol>
  <p align="right"><a href="#readme-top">back to top</a></p>
</details>

---

## About The Project

The API is a simple and efficient task management service built with Flask. The platform enables users to manage their tasks seamlessly and reliably. With the API, organizing your tasks becomes effortless, ensuring a smooth experience for individuals.

### Features
- **Secure Authentication**: The API offers robust user authentication using JWT tokens, ensuring that your task data remains safe and accessible only to you.

- **Task Management**: Create, read, update, and delete tasks effortlessly with our user-friendly endpoints. Whether it's a personal to-do list or a project task, managing tasks is quick and hassle-free.

- **Data Persistence**: All task data is securely stored in a database, ensuring data integrity and reliability.

- **Input Validation**: Strong input validation ensures that the data you enter is accurate and secure, maintaining the integrity of your task management system.

<p align="right"><a href="#readme-top">back to top</a></p>




### Built With:

![Python][python]
![Flask][flask]
![Sqlite][sqlite]
![Postgres][Postgres]

[//]: # (<p align="right"><a href="#readme-top">back to top</a></p>)

[//]: # (---)

[//]: # (## Demo)

[//]: # ()
[//]: # (https://user-images.githubusercontent.com/100721103/225929529-95040462-f36d-4880-854c-c89b4bac6d33.mp4)

[//]: # ()
[//]: # (<br><p align="right"><a href="#readme-top">back to top</a></p>)

---
<!-- Lessons from the Project -->

[//]: # (## Exposure)

[//]: # ()
[//]: # (Creating this project got me more exposed to:)

[//]: # ()
[//]: # (- Debugging)

[//]: # (- Restful API)

[//]: # (- Thorough research)

[//]: # (- Database Management)

[//]: # (- Authentication)

[//]: # (- Authorization)

[//]: # (- Endpoint restriction)

[//]: # (- Testing with unittest)

[//]: # (- Swagger UI)

[//]: # (- API Documentation)

[//]: # (- Integration with React)

<p align="right"><a href="#readme-top">back to top</a></p>

[//]: # (---)

<!-- GETTING STARTED -->

## Usage

To get a local copy up and running, follow the steps below.

### Prerequisites

Python3: [Get Python](https://www.python.org/downloads/)

### Installation

1. Clone this repo
   ```sh
   git clone https://github.com/engrmarkk/task_management_system.git
   ```
2. Navigate into the directory
   ```sh
   cd task_management_system
   ```
3. Create a virtual environment
   ```sh
   python -m venv your_venv_name
   ```
4. Activate the virtual environment on powershell or cmd
   ```sh
   your_venv_name\Scripts\activate.bat
   ```
   On Bash ('Scripts' for windows, 'bin' for linux)
   ```sh
   source your_venv_name/Scripts/activate.csh
   ```
5. Install project dependencies
   ```sh
   pip install -r requirements.txt
   ```
6. Create .env file


7. Place your SECRET_KEY, JWT_SECRET_KEY, and DATABASE_URI (for postgresql, then a postgres link)
   ```sh
   DATABASE_URI=<your_postgresql_link>
   SECRET_KEY=<your_secret_key>
   JWT_SECRET_KEY=<your_jwt_secret_key>
   ```
8. Set your flask app
   ```sh
   set FLASK_APP=runserver.py
   ```
   on linux or macOS
   ```sh
   export FLASK_APP=runserver.py
   ```

9. Create database (using flask migrate)
   ```sh
   flask db init ( This will create a migration file)
   flask db migrate
   flask db upgrade (This  will create the db along with the tables)
   ```

10. Run App
   ```sh
    python runserver.py
   ```
11. Use the link generated on the terminal to access the endpoints
    ```sh
      http://127.0.0.1:5000
      ```

### Project structure

   ```sh
   
   ├── README.md
   ├── .gitignore
   ├── app_config
   |   ├── __init_.py
   |   ├── Your_sqlite_database
   ├── endpoints
   │   ├── __init__.py
   │   ├── auth.py
   |   |   ├──__init__.py
   │   └── users.py
   |   |  ├──__init__.py
   ├── models
   |   ├── __init_.py
   ├── app_config
   |   ├── __init_.py
   ├── sockets
   |   ├── __init_.py
   ├── utils
   |   ├── __init_.py
   ├── extensions
   |   ├── __init_.py
   ├── your_venv_name
   ├── .env
   ├── runserver.py
   └── requirements.txt
   ```  


### Endpoints
<br>
POST (Register) http://127.0.0.1:8000/api/v1/auth/register


REQUEST
```json
{
  "username": "string",
  "password": "password"
}
```

RESPONSE (Success)
```json
 {
    "message": "User created successfully"
}
```

RESPONSE (Error)
```json
 {
    "message": "Username already exist"
}
```


[//]: # (RESPONSE)

[//]: # (```json)

[//]: # ({)

[//]: # (    "id": 1,)

[//]: # (    "first_name": "string",)

[//]: # (    "password": "string",)

[//]: # (    "email": "string@string.com",)

[//]: # (    "last_name": "string")

[//]: # (})

[//]: # (```)
POST (Login) http://127.0.0.1:8000/api/v1/auth/login


REQUEST
```json
{
  "username": "string",
  "password": "string"
}
```
RESPONSE (Success)
```json
  {
    "access_token": "eyJhbGciOiJIUzIEyM..................."
  }
```
RESPONSE (Error)
```json
 {
    "message": "User does not exist"
}
```

To login with your key,

```sh
Provide the access token on postman auth (Bearer Token)
```
`

GET (Get tasks) http://127.0.0.1:8000/api/v1/user/get_tasks <br/>
@jwt_required


RESPONSE
```json
  {
    "tasks": [
        {
            "completed": true,
            "date_created": "19-May-2024 22:20:15",
            "id": "0abbf4f4131240dc85888bbc1bd4dc3e",
            "task_content": "Write code, Buy foodtuffs, Gym, and Sleep",
            "title": "Welcome Task2"
        },
        {
            "completed": false,
            "date_created": "19-May-2024 22:18:31",
            "id": "66d9c4c3f2bd4b2db2fd9cae4df61161",
            "task_content": "This is a welcome task",
            "title": "Welcome Task"
        }
    ]
}
```

GET (Get one Task) http://127.0.0.1:8000/api/v1/user/get_one_task/d8ae7e5dea934f3d9f02c2c3f49f2c72 <br/>
@jwt_required


RESPONSE
```json
  {
    "message": "Task found",
    "task": {
        "completed": false,
        "date_created": "19-May-2024 22:21:06",
        "id": "d8ae7e5dea934f3d9f02c2c3f49f2c72",
        "task_content": "Write code, Buy foodtuffs, Gym, and Sleep",
        "title": "Today Todo"
    }
}
```

RESPONSE (Error)
```json
 {
    "message": "No task found"
}
```

POST (Create Task) http://127.0.0.1:8000/api/v1/user/create_task <br>
@jwt_required

REQUEST
```json
{
    "title": "My List3",
    "content": "Write code, Go out"
}
```

RESPONSE
```json
 {
    "message": "Task created successfully"
}
```

PATCH (Update Task) http://127.0.0.1:8000/api/v1/user/update_task/0abbf4f4131240dc85888bbc1bd4dc3e <br>
@jwt_required

REQUEST
```json
{
    "content": "Write code, Buy foodtuffs, Gym, and Sleep",
    "completed": true
}
```

RESPONSE (Success)
```json
 {
    "message": "Task updated successfully"
}
```
RESPONSE (Error)
```json
 {
    "message": "No task found"
}
```

PATCH (Update Task) http://127.0.0.1:8000/api/v1/user/delete_task/d8ae7e5dea934f3d9f02c2c3f49f2c72 <br>
@jwt_required

RESPONSE (Success)
```json
 {
    "message": "Task deleted successfully"
}
```
RESPONSE (Error)
```json
 {
    "message": "No task found"
}
```

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Sample Screenshot -->

<!-- ## Shots -->

<!-- <br /> -->
<!-- <p>Light Mode</p> -->

<!-- [![My Blog Project Screenshot][Quiz_Api-screenshot]](https://github.com/engrmarkk/Quiz_Api/blob/main/static/images/screen-light.png) -->

<!-- <br/> -->
<!-- <p>Dark Mode</p> -->

<!-- [![My Blog Project Screenshot][Quiz_Api-screenshot2]](https://github.com/engrmarkk/Quiz_Api/blob/main/static/images/screen-dark.png) -->

[//]: # (<br/>)

[//]: # (<p align="right"><a href="#readme-top">back to top</a></p>)


<!-- Contact -->

## Contact

Adeniyi Olanrewaju - [@iamengrmark](https://twitter.com/iamengrmark) - adeniyiboladale@yahoo.com <br>

[//]: # (Gabriel Kalango - [@GabrielKalango]&#40;https://twitter.com/GabrielKalango&#41; - kallythegreat11@gmail.com)

Project Link: [Task Management System API](https://github.com/engrmarkk/task_management_system) <br>

Live Link (BASE URL): https://task-management-system-cy45.onrender.com/api/v1/

Postman Documentation: [Postman DOC](https://documenter.getpostman.com/view/30792613/2sA3QmDa7z)
<p align="right"><a href="#readme-top">back to top</a></p>

---


<!-- Markdown Links & Images -->

[contributors-shield]: https://img.shields.io/github/contributors/engrmarkk/task_management_system.svg?style=for-the-badge
[contributors-url]: https://github.com/engrmarkk/task_management_system/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/engrmarkk/task_management_system.svg?style=for-the-badge
[forks-url]: https://github.com/engrmarkk/task_management_system/network/members
[stars-shield]: https://img.shields.io/github/stars/engrmarkk/task_management_system.svg?style=for-the-badge
[stars-url]: https://github.com/engrmarkk/task_management_system/stargazers
[issues-shield]: https://img.shields.io/github/issues/engrmarkk/task_management_system.svg?style=for-the-badge
[issues-url]: https://github.com/engrmarkk/task_management_systemissues
[license-shield]: https://img.shields.io/github/license/engrmarkk/task_management_system.svg?style=for-the-badge
[license-url]: https://github.com/engrmarkk/task_management_system/blob/main/LICENSE.txt
[twitter-shield]: https://img.shields.io/badge/-@iamengrmark-1ca0f1?style=for-the-badge&logo=twitter&logoColor=white&link=https://twitter.com/iamengrmark
[twitter-shield2]: https://img.shields.io/badge/-@GabrielKalango-1ca0f1?style=for-the-badge&logo=twitter&logoColor=white&link=https://twitter.com/GabrielKalango
[twitter-url]: https://twitter.com/iamengrmark
[postgres]: https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white
[twitter-url2]: https://twitter.com/GabrielKalango
[Quiz_Api-screenshot]: static/images/screen-light.png
[Quiz_Api-screenshot2]: static/images/screen-dark.png
[python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[flask]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[django]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[djangorest]: https://img.shields.io/badge/django_rest_framework-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[jinja]: https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black
[html5]: https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white
[css3]: https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white
[sqlite]: https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white
[javascript]: https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E
[bootstrap]: https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white
[Postgres]: https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white

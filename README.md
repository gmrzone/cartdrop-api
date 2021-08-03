<div align="center">
  <h1>Cartdrop E-commerce</h1>
</div>

<div align="center">
  <h2>A high performanence Ecommerce created using Django, DRF, Postgresql, Redis on backend and Nextjs, Typescript and tailwind on frontend</h2>
</div>
<br/>

<div align="center">
  <h3>Currently the project is in very early stage of development. Here are some of the pages design screenshot from figma</h3>
</div>

<div align="center">
  <h3>Link to frontend repository https://github.com/gmrzone/cartdrop</h3>
</div>

![Desktop - 1 (1)](https://user-images.githubusercontent.com/65633542/128006696-d9e0371a-b24d-4a3c-a821-51ad0336e5b2.png)
 
<hr>

![Desktop-Product-detail (1)](https://user-images.githubusercontent.com/65633542/128006621-d3f01ab3-9086-41ef-8a98-b042a1f8ab22.png)

<hr>

![Desktop - login (1)](https://user-images.githubusercontent.com/65633542/127986291-0d429eb8-8aa8-47f0-a7c6-afc71de2d444.png)



# How to run it?

1. Clone the repository:
```
$ git clone https://github.com/gmrzone/cartdrop-api.git
```

2. Go to the cloned directory:
```
$ cd cartdrop-api
```

3. create a virtual environment and activate it:
```
$ virtualenv venv && source venv/bin/activate
```

4. Install dependencies:
```
$ pip install -r requirements/local.txt
```

5. Set envirinment variables for Project (Linux)
```
$ export DJANGO_SETTINGS_MODULE=config.settings.local
```

6. Runserver:
```
$ python manage.py runserver
```

## Run using Docker and docker Compose

1. Clone the repository:
```
$ git clone https://github.com/gmrzone/cartdrop-api.git
```

2. Go to the cloned directory:
```
$ cd cartdrop-api
```

3. Build the application:
```
$ docker-compose build
```
4. Start database:
```
$ docker-compose up -d db
```

5. Migrate database and add data to database:
```
$ docker-compose run --rm django /bin/sh scripts/start_script.dev.sh
```

6. Run the application:
```
$ docker-compose up
```

The application should now be available on http://127.0.0.1:8000/





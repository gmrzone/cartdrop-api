<div align="center">
  <h1>Cartdrop E-commerce</h1>
</div>

<div align="center">
  <h2>A high performanence Ecommerce created using Django, DRF, Postgresql, Redis</h2>
</div>
<br/>

<div align="center">
  <h3>Currently the project is in very early stage of development. Here are some of the pages design screenshot from figma</h3>
</div>

![Desktop - 1 (1) (1)](https://user-images.githubusercontent.com/65633542/127990069-c83408dd-9810-4817-86b8-e8faa92f3274.png)

<hr>

![Desktop-Product-detail (1) (1)](https://user-images.githubusercontent.com/65633542/127990218-c1603ded-4cd8-4468-b4f4-4244eb36cfe3.png)


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





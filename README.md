<div align="center">
  <h1>Cartdrop E-commerce</h1>
</div>

<div align="center">
  <h2>A high performanence Ecommerce created using Django, DRF, Postgresql, Redis</h2>
</div>
<br/>

<div align="center">
  <h3>Currently the project is in very early stage of development. Here are some of the screenshot of design from figma</h3>
</div>

![Desktop - 1_cropped (1)](https://user-images.githubusercontent.com/65633542/127782631-6cb4f93f-146e-416f-866d-3f08f1aa0076.png)

<hr>

![Desktop-Product-detail_cropped (1)](https://user-images.githubusercontent.com/65633542/127782666-58b5db34-9621-409c-8c67-0c9c7cd692b2.png)

![Desktop - login (1) (1)](https://user-images.githubusercontent.com/65633542/127782646-d38a2e0b-1e70-4848-a83f-4a3658f4e19e.png)

# How to run it?

## Run using Docker and docker Compose

1. Clone the repository:
```
$ git clone https://github.com/gmrzone/cartdrop-api.git
```

2. Go to the cloned directory:
```
$ cd cartdrop-api

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





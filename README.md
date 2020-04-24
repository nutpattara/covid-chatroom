# Covid Chat

This project is for Parallel and Distributed Systems 2110315 class,
Chulalongkorn University

Covid chat is a simple chat room website using django-channels with load balancer from nginx

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install

```bash
pip install -r requirement.txt
```

## Setting up

```python
python manage.py makemigrations
python manage.py migrate
```

## Run the server

```python
docker run -p 6379:6379 -d redis:5
python manage.py runserver 8000
```

## p.s.
This project is for educational purpose only. It might have problems on run-time, feel free to edit and reuse a you please.

## License
[MIT](https://choosealicense.com/licenses/mit/)
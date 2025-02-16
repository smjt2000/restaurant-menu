### use gunicorn as logger:
```
gunicorn --bind 0.0.0.0:8000 -c gunicorn.config.py coffee_shop.wsgi
```

### use logger app as logger:
copy "logger" app to your project.

add `logger` to `INSTALLED_APPS`.

add `logger.middleware.LoggerMiddleWare` to `MIDDLEWARE`.

### urls
`/`: Menu

`/chat/call/?table_name=...`: Menu with "call waiter" button

`/chat/call/?table_name=admin`: List of waiter calls

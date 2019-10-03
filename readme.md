Project is created with:

* Python              3.7.0
* Django              2.2.5
* Django Rest Framework 3.10.3


## Run Worker

```
python worker.py
```
ctrl + c to stop

## Start Server:

```
python manage.py runserver 8080
```

## Run Unit Tests:

```
python manage.py test
```

## Curl Tests:

* Get:

```
curl -s 127.0.0.1:8080/api/fetcher/1/
```

* List:

```
curl -s 127.0.0.1:8080/api/fetcher/
```

* Create:

```bash
curl -si 127.0.0.1:8080/api/fetcher/ -X POST -d "url=https://httpbin.org/range/15&interval=60"
```

* Update:

```
curl -si 127.0.0.1:8080/api/fetcher/2/ -X PUT -d "url=https://httpbin.org/range/15&interval=666"
```


* Delete:

```
curl -s 127.0.0.1:8080/api/fetcher/1/ -X DELETE
```

* History:

```
curl -s 127.0.0.1:8080/api/fetcher/1/history/
```

## To Do

Tests for worker.py and endpoint mocks.
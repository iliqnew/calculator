# calculator

cd .\calculator_project\
python .\manage.py runserver

Test the API

**with curl**
- curl -X POST http://127.0.0.1:8000/api/calculate/ -d '{"operation": "add", "a": 10.2, "b": 5.8}' -H "Content-Type: application/json"
- curl -X POST http://127.0.0.1:8000/api/calculate/ -d '{"operation": "subtract", "a": 10, "b": 5.8}' -H "Content-Type: application/json"
- curl -X POST http://127.0.0.1:8000/api/calculate/ -d '{"operation": "multiply", "a": 10.2, "b": 5.8}' -H "Content-Type: application/json"
- curl -X POST http://127.0.0.1:8000/api/calculate/ -d '{"operation": "divide", "a": 10.2, "b": 5.8}' -H "Content-Type: application/json"

**via postman**

url:
- http://127.0.0.1:8000/api/calculate/

bodies (one per request):
- {
    "operation": "add",
    "a": 10.2,
    "b": 5.8
}

- {
    "operation": "subtract",
    "a": 10,
    "b": 5.8
}

- {
    "operation": "multiply",
    "a": 10.2,
    "b": 5.8
}

- {
    "operation": "divide",
    "a": 10.2,
    "b": 5.8
}
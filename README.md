# calculator
```
cd .\calculator_project\
python .\manage.py runserver
```

Test the API

**with curl**
- `curl -X POST http://127.0.0.1:8000/api/calculate/ -d '{"expression": "3!"}' -H "Content-Type: application/json"`
- `curl -X POST http://127.0.0.1:8000/api/calculate/ -d '{"expression": "3 + 5 * (2 - 8)^3!"}' -H "Content-Type: application/json"`

**via postman**

url:
- `http://127.0.0.1:8000/api/calculate/`

bodies (one per request):
- `{"expression": "3!"}`
- `{"expression": "3 + 5 * (2 - 8)^3!"}`
 
# calculator

**Setup the calculator project**
```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

cd .\calculator_project\

python .\manage.py makemigrations
python .\manage.py migrate
python .\manage.py runserver
```

Test the API

**with curl**
- `curl -X POST http://127.0.0.1:8000/api/calculate/ -d '{"expression": "3!"}' -H "Content-Type: application/json"`
- `curl -X POST http://127.0.0.1:8000/api/calculate/ -d '{"expression": "3 + 5 * (2 - 8)^2!"}' -H "Content-Type: application/json"`
- `curl -X POST http://127.0.0.1:8000/api/calculate/ -d '{"expression": "3 + 5 * (2 - 8)^2! + 10%125"}' -H "Content-Type: application/json"`
- `curl -X POST http://127.0.0.1:8000/api/calculate/ -d '{"expression": "3 + 5 * (2 - 8)^2! + 10%125 - (-5.34)^2 * (- 7)!"}' -H "Content-Type: application/json"`

**via postman**

url:
- `http://127.0.0.1:8000/api/calculate/`

bodies (one per request):
- `{"expression": "3!"}`
- `{"expression": "3 + 5 * (2 - 8)^3!"}`
- `{"expression": "3 + 5 * (2 - 8)^3! + 10%125"}`
- `{"expression": "3 + 5 * (2 - 8)^3! + 10%125 - (-5.34)^2"}`
## Starting
Start fastapi server:
```
drag and drop from '.venv/Scripts/activate.ps1' to terminal
```

dev
```bash
uvicorn app.main:app --reload
```
prod
```bash
uvicorn app.main:app --host 0.0.0.0 --port 80
```

## API Documentation

- **/docs**: [Swagger UI for API documentation](http://127.0.0.1:8000/docs).
- **/redoc**: [ReDoc UI for API documentation](http://127.0.0.1:8000/redoc).
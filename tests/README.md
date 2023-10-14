### **How to Run Tests:**

Clone the repository and navigate to the `/tests` directory:
```
git clone https://github.com/temirovazat/cinemax-admin-panel.git
```
```
cd cinemax-admin-panel/tests/
```

Create a `.env` file and add test settings:
```
nano .env
```
```
# PostgreSQL
POSTGRES_DB=cinemax_database
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
```

Deploy and run tests within containers:
```
docker-compose up --build --exit-code-from tests
```
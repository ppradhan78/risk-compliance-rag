1.  python -m venv .venv
2.  .venv\Scripts\Activate.ps1

3.  pip install -r requirements.txt

uvicorn app.main:app --reload --port 8000


Make sure qdrant is running and accessible at the specified host and port in your application configuration. You can start Qdrant using Docker with the following command:
```bash
docker run -p 6333:6333 qdrant/qdrant

or bat file

@echo off

cd /d D:\SoftwareInstalled\qdrant

echo Starting Qdrant...
echo Qdrant URL: http://localhost:6333
echo.

qdrant.exe

pause
```
Fast API application will be available at
http://localhost:8000/docs#


http://localhost:6333/

http://localhost:6333/collections

http://localhost:6333/collections/risk_compliance
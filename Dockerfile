FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

RUN pip install --upgrade pip
RUN pip --no-cache-dir install -r requirements.txt

COPY ./main.py /lib/



CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]

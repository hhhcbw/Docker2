FROM python:3.7.9-slim
WORKDIR /ubuntu/flaskapp_vision
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .
CMD ["gunicorn", "-c", "./gunicorn.config.py", "app:app"]

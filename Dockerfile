# 使用官方 Python 映像作為基礎映像
FROM python:3.9

# 設置環境變量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 安裝依賴
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# 複製整個 Django 專案到容器中的 /app 資料夾
COPY . /app

# 指定工作目錄
WORKDIR /app

# 執行 Django 命令來收集靜態文件等
RUN python manage.py collectstatic --noinput

# 運行 Django 應用
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

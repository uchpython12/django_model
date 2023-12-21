# 使用官方 Python 映像作為基礎映像
FROM python:3.9

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 创建并设置工作目录
WORKDIR /app

# 将整个 Django 项目复制到容器中的 /app 目录
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r /app/requirements.txt

# 告诉 Docker 运行服务的命令
CMD ["python", "/app/myproject/manage.py", "runserver", "0.0.0.0:8000"]

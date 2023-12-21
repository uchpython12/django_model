# Django Docker 化專案

這是一個使用 Docker 包裝並支持 MySQL 的 Django 專案。

## 需求

- Docker
- Docker Compose

## 安裝

1. 克隆存儲庫：

    ```bash
    git clone https://github.com/uchpython12/django_model.git
    cd django_model
    ```

2. 構建 Docker 容器：

    ```bash
    docker-compose build
    ```

3. 運行 Docker 容器：

    ```bash
    docker-compose up
    ```

4. 在瀏覽器中訪問 Django 應用程序：

    ```
    http://localhost:8000
    ```

## 配置

### MySQL 數據庫

MySQL 數據庫的配置可以在 `docker-compose.yml` 文件中找到。根據你的需求調整環境變量，例如 `MYSQL_DATABASE`、`MYSQL_USER`、`MYSQL_PASSWORD` 和 `MYSQL_ROOT_PASSWORD`。

### Django 設置

要配置 Django 使用 MySQL，請在 Django 專案目錄中的 `settings.py` 文件中更新。修改 `DATABASES` 部分以使用 MySQL 數據庫引擎，並提供必要的連接詳情。

## 專案結構

- `/app` - Django 專案文件
- `Dockerfile` - Django 應用程序的 Docker 配置
- `docker-compose.yml` - 服務的 Docker Compose 配置（Django 應用程序和 MySQL）

## 用法

- 通過修改 `/app` 目錄中的文件來開發你的 Django 應用程序。
- 在 Docker 容器內使用 Django 管理命令，例如 `docker-compose exec web python manage.py <命令>`。
- 根據你的需求自定義 Django 專案。

## 遷移資料庫

在啟動 Django 專案時，需要進行資料庫遷移以確保模型與資料庫結構同步。以下是必要的步驟：
### 进入容器： 
```bash
docker-compose exec web bash
```
在容器内，运行以下命令来创建迁移文件：
###建立遷移文件

在開發或更新模型後，需要建立遷移檔案來描述資料庫的變更。
運行以下命令：

````bash
python 管理.py makemigrations
````

###應用遷移文件
應用遷移檔案將實際更新資料庫結構以與模型保持一致。以下運行命令：
````bash
python 管理.py 遷移
````

## 貢獻

歡迎通過派生存儲庫並創建拉取請求來為此項目作出貢獻。

## 許可證

[MIT 許可證](LICENSE)

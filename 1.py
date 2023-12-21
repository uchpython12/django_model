import os

# 要列出內容的目錄路徑
directory_path = '/python/django_model'

# 列出目錄中的所有內容
directory_contents = os.listdir(directory_path)

# 遍歷目錄內容並打印
for item in directory_contents:
    print(item)

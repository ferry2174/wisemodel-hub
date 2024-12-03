# wisemodel-hub
    这是wisemodel开源社区仓库上传和下载工具，用于上传下载数据集、模型、代码等。

## 登录
    在登录前需要先注册账号，注册地址为：[https://wisemodel.cn/home](https://wisemodel.cn/home)

## 上传
### 上传单个文件
```python
from wisemodel_hub import upload_file

file_path = "/local/file/path"
repo_id = "your_repo_id"
branch = "main"                 # your branch name
commit_message = "your message" # commit message
chunk_size = 1024 * 1024        # 设置文件块大小，例如1 MB
retries=3                       # 失败重试次数
timeout=10                      # 超时时间，如果不设置则一直等待
upload_file(file_path, repo_id, branch=branch, commit_message=commit_message, chunk_size=chunk_size, retries=retries, timeout=timeout)
``` 

### 上传目录
```python
from wisemodel_hub import push_to_hub

dir_path = "/local/dir/path"
repo_id = "your_repo_id"
regex_pattern = "*"             # 匹配上传文件名的正则表达式，例如"*.py"
branch = "main"                 # your branch name
commit_message = "your message" # commit message
chunk_size = 1024 * 1024        # 设置文件块大小，例如1 MB
retries=3                       # 失败重试次数
timeout=10                      # 超时时间，如果不设置则一直等待
push_to_hub(dir_path, repo_id, regex_pattern=regex_pattern, branch=branch, commit_message=commit_message, chunk_size=chunk_size, retries=3, timeout=10)
``` 

## 下载
### 下载单个文件
```python

``` 
### 下载单个大文件
```python

``` 
### 下载目录
``` python
```
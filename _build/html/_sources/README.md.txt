# wisemodel-hub
    这是wisemodel开源社区仓库上传和下载工具，用于上传下载数据集、模型、代码等。

## 安装
```shell
pip install --index-url https://test.pypi.org/simple/ wisemodel_hub
```

## 登录
    在登录前需要先注册账号，注册地址为：[https://wisemodel.cn/home](https://wisemodel.cn/home)

### 自动登录
    在执行需要登录才能执行的函数时，会自动判断是否需要登录，使用用户名和密码进行登录。<br/>
    当使用notebook时，登录后重新执行原流程即可。<br/>
    当使用命令行时，登录后会自动执行原流程代码。<br/>

### notebook登录
```python
from wisemodel_hub import notebook_login

notebook_login("your_username", "your_password")
```

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
from wisemodel_hub import file_download

repo_id = "renqibing/SafeMTData"    # specified repo id
file_name = ".gitattributes"        # specified file name
local_dir = "/local/download/dir"   # specified local download directory
revision = "your_revision"          # specified revision

file_download(repo_id, file_name, local_dir=local_dir, revision="main")  
``` 
### 下载单个大文件
```python
from wisemodel_hub import lfs_file_download

repo_id = "renqibing/SafeMTData"    # specified repo id
file_name = ".gitattributes"        # specified file name
local_dir = "/local/download/dir"   # specified local download directory
revision = "your_revision"          # specified revision
num_parts = 8                       # 并行下载线程数

file_download(repo_id, file_name, local_dir=local_dir, revision="main", num_parts=num_parts)

``` 
### 下载目录
``` python
from wisemodel_hub import snapshot_download

repo_id = "renqibing/SafeMTData"    # specified repo id
local_dir = "/local/download/dir"   # specified local download directory
revision = "your_revision"          # specified revision
regex_pattern = "*"                 # 匹配下载文件名的正则表达式，例如"*.py"
num_parts = 8                       # 并行下载线程数

file_download(repo_id, local_dir=local_dir, revision="main", regex_pattern=regex_pattern, num_parts=num_parts)
```
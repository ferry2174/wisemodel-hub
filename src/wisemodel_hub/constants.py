import os


WM_ENDPOINT = "https://download.wisemodel.cn"
WM_GITLAB_ENDPOINT = "https://wisemodel.cn"
REVISION = "main"
CACHE_PATH = os.path.join(os.path.expanduser("~"), ".cache", "wisemodel")
RETRY_TIMES = 3
HEADERS = {}
HEADERS["Accept"] = (
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
)
HEADERS["User-Agent"] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)
HEADERS["Cookie"] = (
    "_ga=GA1.1.1928334475.1726100366; _ga_R1FN4KJKJH=GS1.1.1726100366.1.0.1726100372.0.0.0; ajs_anonymous_id=ec015c9c-f1e5-43a5-ae39-fb6910b8a9e9"
)
TEN_MB = 10 * 1024 * 1024
SLEEP_TIME = 5

WM_URL_CHECK = "https://www.wisemodel.cn/gateway/fileupload/api/v1/check"
WM_URL_UPLOAD = "https://www.wisemodel.cn/gateway/fileupload/api/v1/upload"
WM_URL_MERGE = "https://www.wisemodel.cn/gateway/fileupload/api/v1/merge"
WM_URL_ADDFILES = "https://www.wisemodel.cn/gateway/fileupload/api/v1/addfiles"

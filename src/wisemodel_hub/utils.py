import hashlib
import os

import gitlab
import requests

from .constants import CACHE_PATH, HEADERS, TEN_MB, WM_ENDPOINT, WM_GITLAB_ENDPOINT


# Get file names from GitLab repo based on repo id
def get_file_names(repo_id):
    gl = gitlab.Gitlab(WM_GITLAB_ENDPOINT)
    project = gl.projects.get(repo_id)
    files = project.repository_tree()
    return [file["name"] for file in files if file["type"] == "blob"]


def get_remote_file_size(repo_id, file_name, revision="main"):
    return get_remote_file_size_with_url(WM_ENDPOINT + f"/file-proxy/{repo_id}/-/raw/{revision}/{file_name}")


def get_remote_file_size_with_url(url):
    res = requests.get(url, stream=True, headers=HEADERS)
    res.raise_for_status()
    total_size = int(res.headers.get("Content-Length", 0))
    res.close()
    return total_size


def is_file_downloaded(repo_id, file_name, revision):
    cache_path = os.path.join(CACHE_PATH, repo_id.replace("/", "_"), file_name)
    if not os.path.exists(cache_path):
        return False
    local_size = os.path.getsize(cache_path)

    remote_size = get_remote_file_size(repo_id, file_name, revision)

    return remote_size == local_size


def is_greater_than_10mb(repo_id, file_name, revision="main"):
    return get_remote_file_size(repo_id, file_name, revision) > TEN_MB


def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


if __name__ == "__main__":
    repo_id = "01.AI/Yi-34B-Chat-4bits"
    file_names = get_file_names(repo_id)
    for file_name in file_names:
        print(file_name)

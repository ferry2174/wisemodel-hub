import os

import requests
from tqdm import tqdm

from ..constants import WM_URL_ADDFILES, WM_URL_CHECK, WM_URL_MERGE, WM_URL_UPLOAD
from ..utils import calculate_md5


TEMP_AUTH = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MzI4NzE0OTUsInVzZXJfaWQiOjg3MzYsInVzZXJuYW1lIjoiZGFkYmVhciIsImlzcyI6InN6In0.jP29N2wr_6xeDujWNYJ-gUlWbGFI0IsIE1OLAJDpv6I"


def upload_file(
    file_path, repo_id, token, project_id, branch, commit_message, chunk_size=5 * 1024 * 1024, retries=3, timeout=None
):
    file_name = os.path.basename(file_path)
    file_md5 = calculate_md5(file_path)

    # Step 1: Check the file chunk status
    check_data = {"fileName": file_name, "fileMd5": file_md5, "dir": "", "project_id": project_id}
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(WM_URL_CHECK, data=check_data, headers=headers)
    check_response = response.json()

    if check_response["code"] != 0:
        print(f"文件检查失败: {check_response['message']}")
        return

    existing_chunks = check_response["data"]["chunks"]
    if "resultCode" in check_response["data"] and check_response["data"]["resultCode"] == -1:
        existing_chunks = []

    # Step 2: Upload file chunks
    file_size = os.path.getsize(file_path)
    num_chunks = (file_size + chunk_size - 1) // chunk_size  # 计算块的数量

    with open(file_path, "rb") as f, tqdm(total=file_size, unit="B", unit_scale=True, desc=file_name) as pbar:
        for i in range(num_chunks):
            if str(i) in existing_chunks:
                f.seek(chunk_size, os.SEEK_CUR)
                pbar.update(chunk_size)  # 跳过已存在的块，并更新进度条
                continue

            chunk_data = f.read(chunk_size)
            upload_data = {"md5": file_md5, "dir": "", "project_id": project_id, "chunk": i}
            files = {"file": (file_name, chunk_data)}

            for _ in range(retries):
                try:
                    response = requests.post(
                        WM_URL_UPLOAD, data=upload_data, files=files, timeout=timeout, headers=headers
                    )
                    upload_response = response.json()
                    if upload_response["code"] == 0:
                        pbar.update(len(chunk_data))
                        break
                except requests.exceptions.RequestException as e:
                    print(f"Retry {i} due to {str(e)}")

    # Step 3: Check again the file chunk status after uploading all chunks
    response = requests.post(WM_URL_CHECK, data=check_data, headers=headers)
    check_response = response.json()

    if (
        check_response["code"] != 0
        or "resultCode" in check_response["data"]
        and check_response["data"]["resultCode"] != num_chunks
    ):
        print(f"文件检查失败或文件块数量不匹配: {check_response['message']}")
        return
    print("所有文件块已成功上传并验证")

    # Step 4: Merge file chunks
    merge_data = {"fileName": file_name, "fileMd5": file_md5, "dir": "", "project_id": project_id}
    response = requests.post(WM_URL_MERGE, data=merge_data, headers=headers)
    merge_response = response.json()

    if merge_response["code"] != 0:
        print(f"文件合并失败: {merge_response['message']}")
        return

    merged_file_path = merge_response["data"]["filepath"]
    print(f"文件合并成功: {merged_file_path}")

    # Step 5: Add merged file to repository
    addfiles_data = {
        "id": project_id,
        "branch": branch,
        "files": [merged_file_path],
        "commit": commit_message,
        "wangpan_url": "",
    }
    response = requests.post(WM_URL_ADDFILES, json=addfiles_data, headers=headers)
    addfiles_response = response.json()

    if addfiles_response["code"] != 0:
        print(f"添加文件到仓库失败: {addfiles_response['message']}")
        return

    print(f"{file_name},文件上传并添加到仓库成功")

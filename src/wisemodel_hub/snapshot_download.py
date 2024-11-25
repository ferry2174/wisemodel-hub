from .constants import RETRY_TIMES
from .download_with_resume import GitFileDownload
from .parallel_download_with_resume import LFSDownload
from .utils import get_file_names


# download model files from Wisemodel by providing repo_id in format like 'rwkv4fun/Rwkv-6-world'
def snapshot_download(repo_id, revision="main"):
    file_names = get_file_names(repo_id)
    for file_name in file_names:
        try_times = 0
        while try_times < RETRY_TIMES + 1:
            try:
                try_times += 1
                print(f"Downloading {file_name}...")
                # raise Exception("Test exception")  # 用于测试的异常
                if file_name.endswith(".bin") or file_name.endswith(".safetensors"):
                    lfs_file_download(repo_id, file_name, revision=revision)
                else:
                    file_download(repo_id, file_name, revision=revision)
            except Exception as e:
                print(f"Failed to download {file_name}: {e}")
                if try_times < RETRY_TIMES + 1:
                    print(f"Retrying {try_times}...")
                else:
                    print(f"Failed to download {file_name} after {try_times-1} retries.")


def lfs_file_download(repo_id, file_name, revision="main", num_parts=8):
    downloader = LFSDownload(repo_id, file_name, revision=revision, num_parts=num_parts)
    downloader.download()


def file_download(repo_id, file_name, revision="main", local_dir=None):
    downloader = GitFileDownload(repo_id)
    downloader.download_file(file_name, revision=revision, local_dir=local_dir)


if __name__ == "__main__":
    repo_id = "CUHK-DVLab/Mini-Gemini-2B"
    snapshot_download(repo_id)

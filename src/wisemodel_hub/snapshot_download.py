from .constants import RETRY_TIMES
from .download_with_resume import GitFileDownload
from .parallel_download_with_resume import LFSDownload
from .utils import filter_files_with_regex, get_file_names, is_file_downloaded, is_greater_than_10mb


def snapshot_download(repo_id, local_dir=None, revision="main", regex_pattern=None, num_parts=4):
    file_names = get_file_names(repo_id)
    file_names = filter_files_with_regex(file_names, regex_pattern)
    for file_name in file_names:
        try_times = 0
        while try_times < RETRY_TIMES + 1:
            if is_file_downloaded(repo_id, file_name, revision):
                print(f"{file_name} already exists in cache.")
                break
            try:
                try_times += 1
                print(f"Downloading {file_name}...")
                if is_greater_than_10mb(repo_id, file_name, revision):
                    lfs_file_download(repo_id, file_name, local_dir=local_dir, revision=revision, num_parts=num_parts)
                else:
                    file_download(repo_id, file_name, local_dir=local_dir, revision=revision)
                break
            except Exception as e:
                print(f"Failed to download {file_name}: {e}")
                if try_times < RETRY_TIMES + 1:
                    print(f"Retrying {try_times}...")
                else:
                    print(f"Failed to download {file_name} after {try_times-1} retries.")


def lfs_file_download(repo_id, file_name, local_dir=None, revision="main", num_parts=8):
    downloader = LFSDownload(repo_id, file_name, local_idr=local_dir, revision=revision, num_parts=num_parts)
    downloader.download()


def file_download(repo_id, file_name, local_dir=None, revision="main"):
    downloader = GitFileDownload(repo_id)
    downloader.download_file(file_name, revision=revision, local_dir=local_dir)

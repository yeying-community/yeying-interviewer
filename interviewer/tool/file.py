import logging
import os


def read(file_path):
    if not os.path.exists(file_path):
        logging.info(f'There is no such file={file_path}')
        return None
    with open(file_path, 'rb') as f:
        content = f.read()
    return content


def ensure_parent_dirs_exist(file_path):
    # 提取文件路径的父目录
    parent_dir = os.path.dirname(file_path)

    # 创建父目录及所有必要的子目录
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)
    return file_path

import shutil
import os


def copy_file(src, dest, overwrite=False):
    """
    复制单个文件到目标路径，可以选择是否覆盖。

    :param src: 源文件路径
    :param dest: 目标文件路径
    :param overwrite: 是否覆盖已有文件，默认不覆盖
    """
    if os.path.exists(dest) and not overwrite:
        print(f"File {dest} already exists and will not be overwritten.")
    else:
        shutil.copy2(src, dest)
        print(f"File {src} copied to {dest}.")


def copy_folder(src, dest, overwrite=False):
    """
    复制文件夹内容到目标文件夹，可以选择是否覆盖。

    :param src: 源文件夹路径
    :param dest: 目标文件夹路径
    :param overwrite: 是否覆盖已有文件，默认不覆盖
    """

    def custom_copy_function(src, dest):
        copy_file(src, dest, overwrite)

    shutil.copytree(src, dest, dirs_exist_ok=True, copy_function=custom_copy_function)


if __name__ == "__main__":
    copy_file(
        "/Users/zhangwenjie/coding/myboran/file1.txt",
        "/Users/zhangwenjie/coding/myboran/file2.txt",
        overwrite=True,
    )
    copy_folder(
        "/Users/zhangwenjie/coding/myboran/file",
        "/Users/zhangwenjie/coding/myboran/file2",
        overwrite=True,
    )

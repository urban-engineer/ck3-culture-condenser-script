import pathlib
import shutil

from utils import log


def clear_backup_folder(backup_folder_path: pathlib.Path):
    """
    Clear a backup folder if it exists.

    :param backup_folder_path: path to folder containing files backed up from a previous execution
    :return: None
    """
    if backup_folder_path.exists() and backup_folder_path.is_dir():
        for file in [x for x in backup_folder_path.iterdir() if x.is_file()]:
            file.unlink()


def backup_files(content_folder: pathlib.Path, backup_folder: pathlib.Path, dry_run: bool = False):
    """
    Copies files before performing operations on them.

    :param content_folder: path containing files to be modified
    :param backup_folder: path to where backup files should be stored
    :param dry_run: flag to not perform operations, just print out as if it was.
    :return: None
    """
    log.debug("Backing up original files to [{}]".format(backup_folder))
    if not dry_run:
        backup_folder.mkdir(exist_ok=True, parents=True)
        for file in [x for x in content_folder.iterdir() if x.is_file()]:
            shutil.copy2(file, backup_folder.joinpath(file.name))

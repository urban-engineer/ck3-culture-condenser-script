import argparse
import pathlib
import typing

from utils import common
from utils import log


def set_custom_icons(file: pathlib.Path, start: int, end: int) -> typing.List[str]:
    log.info("Scanning [{}]".format(file.name))

    lines = file.read_text(encoding="utf-8").splitlines(keepends=False)
    new_lines = []
    icon_string = " ".join(["custom{}".format(x) for x in range(start, end + 1)])

    # empty file check - empty files are to dummy out base CK3 religions
    if len(lines) > 1:
        in_custom_faith_icons = False
        for line in lines:
            if in_custom_faith_icons:
                if "}" in line:
                    in_custom_faith_icons = False
                else:
                    new_lines.append("\t\t{}".format(icon_string))
                    continue

            if "custom_faith_icons" in line:
                in_custom_faith_icons = True

            new_lines.append(line)

    return new_lines


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("religion_path", help="Path to folder containing religions to be converted")
    parser.add_argument("start_number", type=int, help="First number for custom religion icons")
    parser.add_argument("end_number", type=int, help="Last number for custom religion icons")
    parser.add_argument("--dry_run", action="store_true", help="Does not move or delete files, just parse")
    parser.add_argument("--wipe", action="store_true", help="Does not backup original files")
    args = parser.parse_args()

    religion_folder = pathlib.Path(args.religion_path).resolve().absolute()
    log.info("Parsing religion icons in [{}]".format(religion_folder))

    backup_folder = religion_folder.parent.joinpath("{}.bak".format(religion_folder.name))
    if args.wipe:
        common.clear_backup_folder(backup_folder)
    else:
        common.backup_files(religion_folder, backup_folder, args.dry_run)

    for religion in sorted([x for x in religion_folder.iterdir() if x.is_file() and x.name.endswith("txt")]):
        new_contents = set_custom_icons(religion, args.start_number, args.end_number)
        if not args.dry_run:
            religion.write_text("\n".join(new_contents), encoding="utf-8")

    log.info("Conversion complete")

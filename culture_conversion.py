import argparse
import pathlib
import typing

from utils import common
from utils import log


def parse_file(file: pathlib.Path) -> typing.List[str]:
    log.info("Scanning [{}]".format(file.name))
    lines = file.read_text(encoding="utf-8").splitlines(keepends=False)
    fixed_contents = []

    in_group = False
    in_building = False
    in_clothing = False
    in_unit = False

    for line in lines:
        # Flag handling - if we hit the end of a block and we're "in" a block, flag false and move to next line
        if any([in_group, in_building, in_clothing, in_unit]) and line.strip() == "}":
            in_group = False
            in_building = False
            in_clothing = False
            in_unit = False

        # Checking for which block we're in
        if "=" in line:
            if "coa_gfx" in line or "group_gfx" in line:
                in_group = True
            elif "building_gfx" in line:
                in_building = True
            elif "clothing_gfx" in line:
                in_clothing = True
            elif "unit_gfx" in line:
                in_unit = True

        # Now we check if we're in a scope we care about but the value is something we want to ignore
        if in_group and not ("coa_gfx" in line or "group_gfx" in line):
            continue
        if in_building and "building_gfx" not in line:
            continue
        if in_clothing and "clothing_gfx" not in line:
            continue
        if in_unit and "unit_gfx" not in line:
            continue

        # Finally, we add the verified good line to the final output
        # The only way to get here is to not be in a scope of concern
        # (e.g. the curly bracket at the end of a scope, anywhere in a scope we don't care about, etc.)
        fixed_contents.append(line)

    log.debug("Removed [{}] excess lines from [{}]".format(len(lines) - len(fixed_contents), file.name))

    return fixed_contents


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("culture_path", help="Path to folder containing cultures to be converted")
    parser.add_argument("--dry_run", action="store_true", help="Does not move or delete files, just parses")
    parser.add_argument("--wipe", action="store_true", help="Does not backup original culture files, just deletes")
    args = parser.parse_args()

    culture_folder = pathlib.Path(args.culture_path)
    log.debug("Parsing culture files in [{}]".format(culture_folder))

    backup_folder = culture_folder.parent.joinpath("{}.bak".format(culture_folder.name))
    if args.wipe:
        common.clear_backup_folder(backup_folder)
    else:
        common.backup_files(culture_folder, backup_folder, args.dry_run)

    for culture in sorted([x for x in culture_folder.iterdir() if x.is_file()]):
        new_contents = parse_file(culture)
        if not args.dry_run:
            culture.write_text("\n".join(new_contents), encoding="utf-8")

    log.debug("Conversion complete")

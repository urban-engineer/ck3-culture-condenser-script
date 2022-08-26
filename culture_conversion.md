# CK3 Modding Scripts

## Summary

Script to remove extra entries in culture files.

## Explanation

The following is allowed by the CK3 modding system:

```
building_gfx = {
    canadian_clothing_gfx
    maritimer_coa_gfx
    north_atlantic_coa_gfx
    western_building_gfx
    northern_clothing_gfx
    northern_unit_gfx
}
```

However, in this example, lines not containing `building_gfx` are not relevant and should be removed to make the file more readable/editable.  So this script will remove them as necessary.

The above snippet, but without 'extra' entries:

```
building_gfx = {
    western_building_gfx
}
```

This applies to `building_gfx`, `clothing_gfx`, `coa_gfx`, `group_gfx`, and `unit_gfx` scopes (and not any other scope).

Do note that `coa_gfx` and `group_gfx` are special since they represent the same scope/values.  So the script takes care to interact with them as if they are the same.

For example, the following snippet:

```
coa_gfx = {
    margariteno_coa_gfx
    costero_group_gfx
    mediterranean_building_gfx
    western_clothing_gfx
    indian_clothing_gfx
    western_unit_gfx
}
```

Will condense down to:

```
coa_gfx = {
    margariteno_coa_gfx
    costero_group_gfx
}
```

(Note `costero_group_gfx` was included, despite not containing `coa_gfx`)

## Installation

1. Install [Python](https://www.python.org/downloads/) (version 3.9 or greater)
2. Download the files from this repository.
 
For safety's sake, don't download these files to the same location as the files to be converted

## Execution

1. Open a command prompt/terminal instance/Powershell session in the folder containing `culture_conversion.py`.
2. Execute `python culture_conversion.py <path to cultures folder>`

Optionally, you may include the `--dry_run` flag to not actually move/convert files.  You may also include the `--wipe` option which will not backup the original culture files and just edit them in place.  e.g.:

* `python culture_conversion.py <path to cultures folder> --dry_run`
* `python culture_conversion.py <path to cultures folder> --wipe`
* `python culture_conversion.py <path to cultures folder> --dry_run --wipe`

A word of warning: this was only tested on Windows.  This should work on Linux or Mac, but Windows users should _probably_ wrap the path to the cultures folder in double quotes, to be safe.  e.g.:

* `python culture_conversion.py "C:\Users\username\Modding\CK3\my-cool-mod\cultures"`

## Expected output

Something like:

```
[   DEBUG]  [culture_conversion.py/<module>:71] - Parsing culture files in [C:\path\to\cultures]
[   DEBUG]  [culture_conversion.py/<module>:75] - Original culture files will be backed up to [C:\path\to\cultures\bak]
[    INFO]  [culture_conversion.py/parse_file:15] - Scanning [<culture_file_1>]
[   DEBUG]  [culture_conversion.py/parse_file:58] - Removed [18] excess lines from [<culture_file_1>]
[    INFO]  [culture_conversion.py/parse_file:15] - Scanning [<culture_file_2>]
[   DEBUG]  [culture_conversion.py/parse_file:58] - Removed [5] excess lines from [<culture_file_2>]
[    INFO]  [culture_conversion.py/parse_file:15] - Scanning [<culture_file_3>]
[   DEBUG]  [culture_conversion.py/parse_file:58] - Removed [99] excess lines from [<culture_file_3>]
[    INFO]  [culture_conversion.py/parse_file:15] - Scanning [<culture_file_4>]
[   DEBUG]  [culture_conversion.py/parse_file:58] - Removed [0] excess lines from [<culture_file_4>]
<further output truncated>
[   DEBUG]  [culture_conversion.py/<module>:91] - Conversion complete
```

## Bug Reporting

Feel free to leave an issue in this repo, I'll try to fix things if needed.  No promises.  Honestly if you just want to fork this and improve it as you see fit, feel free, no skin off my back.

## Final notes

The `cultures` folder exists as test data to be used, with three files already converted and three unconverted.  Those would be `000_abajeno.txt`, `000_abenaki.txt`, `000_acadien.txt` and `000_maracaju.txt`, `000_margariteno.txt`, and `000_maritimer.txt` respectively.  As bugs are fixed/features added, those files (and more) will be used for testing.  Hey, self, that's a good todo: some automated testing baybee

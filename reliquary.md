# CK3 Modding Scripts

## Summary

Script to quickly add custom icon religious icon entries to religion files.  Or write out a template for empty files.

## Explanation

The following is allowed by the CK3 modding system:

```
custom_faith_icons = {
    custom1 custom2 custom3 custom4 custom5 custom6 custom7 custom8 custom9 custom10 <truncated>
}
```

This is fine, but writing this out for each religion is tedious and error-prone.  This script will automatically write the `customX` string to religion files given the appropriate bounds.

If it finds an empty file, this script will instead write a basic 'template' instead.  It's modeled after `000_nanakpanthi.txt` (provided by a modder), and is designed to be the bare-minimum necessary for a religion to be defined.  Do note that I personally do not mod CK3, so I have no idea if I'm lying to you, intentionally or not.

## Execution

1. Open a command prompt/terminal instance/Powershell session in the folder containing `reliquary.py`.
2. Execute `python reliquary.py <path to religions folder> <start number> <end number>`

Optionally, you may include the `--dry_run` flag to not actually move/convert files.  You may also include the `--wipe` option which will not backup the original culture files and just edit them in place.  e.g.:

* `python reliquary.py /path/to/mod/religions 1 100 --dry_run`
* `python reliquary.py /path/to/mod/religions 1 100 --wipe`
* `python reliquary.py /path/to/mod/religions 1 100 --dry_run --wipe`

A word of warning: this was only tested on Windows.  This should work on Linux or Mac, but Windows users should _probably_ wrap the path to the religions folder in double quotes, to be safe.  e.g.:

* `python reliquary.py "C:\Users\username\Modding\CK3\my-cool-mod\religions" 1 100`

## Expected output

Something like:

```
[    INFO]  [reliquary.py/<module>:282] - Parsing religion icons in [C:\Users\username\Modding\CK3\my-cool-mod\religions]
[    INFO]  [reliquary.py/set_custom_icons:245] - Scanning [000_americanist.txt]
[    INFO]  [reliquary.py/set_custom_icons:245] - Scanning [000_astronomer.txt]
[    INFO]  [reliquary.py/set_custom_icons:245] - Scanning [000_nanakpanthi.txt]
[    INFO]  [reliquary.py/set_custom_icons:245] - Scanning [000_universal.txt]
[    INFO]  [reliquary.py/set_custom_icons:245] - Scanning [00_tributist.txt]
[    INFO]  [reliquary.py/set_custom_icons:245] - Scanning [00_waaqism.txt]
[    INFO]  [reliquary.py/set_custom_icons:245] - Scanning [00_west_african.txt]
[    INFO]  [reliquary.py/set_custom_icons:245] - Scanning [00_west_african_bori.txt]
[    INFO]  [reliquary.py/<module>:295] - Conversion complete
```

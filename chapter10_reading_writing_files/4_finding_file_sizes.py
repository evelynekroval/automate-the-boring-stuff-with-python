from pathlib import Path
import time

calc_file = Path('C:/Windows/System32/calc.exe')

calc_file.stat()
# Outputs: 
# os.stat_result(st_mode=33279, st_ino=562949956525418, st_dev=3739257218,
# st_nlink=2, st_uid=0, st_gid=0, st_size=27648, st_atime=1678984560,
# st_mtime=1575709787, st_ctime=1575709787)

# You can access the various attributes of stat_results objects as normal.

BASIC_INFO = f"""
The size (in bytes) of the Calculator app in Windows is: {calc_file.stat().st_size}. 

You can divide it by 1024, by 1024 ** 2, or by 1024 ** 3 to get the size in:
- {calc_file.stat().st_size / 1024} KB, 
- {calc_file.stat().st_size / 1024 ** 2} MB, or
- {calc_file.stat().st_size / 1024 ** 3} GB, respectively.

The `st_mtime` is the "last modified" timestamp. 

This timestamp is in Unix epoch time, which is the number of seconds since January 1, 1970. 

The `time` module can turn that into human-readable form: {time.asctime(time.localtime(calc_file.stat().st_mtime))}.

Others include:
- `st_birthtime` - the “creation” timestamp: {time.asctime(time.localtime(calc_file.stat().st_birthtime))}
On Windows, this identifies when the file was created. 
On macOS and Linux, this identifies the last time the file’s metadata (such as its name) was changed.

- `st_atime` - the “last accessed” timestamp, when the file was last read: {time.asctime(time.localtime(calc_file.stat().st_atime))}

Keep in mind that the modified, creation, and access timestamps can be changed manually, and are not guaranteed to be accurate."""


print(BASIC_INFO)
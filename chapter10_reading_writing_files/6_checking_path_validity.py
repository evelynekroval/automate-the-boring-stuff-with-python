

# Non-existent paths obviously give errors
# So you can use certain boolean methods to verify existence and type of path

from pathlib import Path

win_dir = Path('C:/Windows')

not_exists_dir = Path('C:/This/Folder/Does/Not/Exist')
calc_file_path = Path('C:/Windows/System32/calc.exe')

PATH_VALIDITY_DEMO = f"""
You can see that the Windows directory exists: {win_dir.exists()}.

Is it a directory? {win_dir.is_dir()}.

Does the random path I created exist? {not_exists_dir.exists()}.

Is the calculator a file? {calc_file_path.is_file()}. Surely not a directory? {calc_file_path.is_dir()}"""

print(PATH_VALIDITY_DEMO)

# You can determine whether there is a DVD or flash drive currently attached to the computer 
# by checking for it with the exists() method. 
# For instance, if I wanted to check for a flash drive with the volume named D:\ 
# on my Windows computer, I could do that with the following:

d_drive = Path('D:/')
print(d_drive.exists())
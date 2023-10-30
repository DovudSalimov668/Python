import pathlib

path = pathlib.Path("C:\Python 1\day13\day13.py")
print(path)
home = pathlib.Path.home()
cwd = pathlib.Path.cwd()
print(home)
print(cwd)
course_dir = cwd /"day13" / "day13.py"
print(course_dir)
path1 = pathlib.Path
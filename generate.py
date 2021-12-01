import os
import shutil

for i in range(1,26):
    filename = f"day_{i:02}.py"
    if not os.path.exists(filename):
        shutil.copy("template.py", filename)
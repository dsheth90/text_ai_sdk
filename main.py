import os
import glob

print([os.path.splitext(os.path.basename(path))[0] for path in glob.glob('src/*.py')])
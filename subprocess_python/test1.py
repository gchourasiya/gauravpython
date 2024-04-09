import os
import subprocess
from glob import glob

out = subprocess.run(['hostname'],capture_output=True,text=True)
print(out)

out1 = glob('*.subprocess.*')
print(out1)
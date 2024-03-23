# Çakıyı güncelleme paketi

import os
from requests import get as g

build = g("https://raw.githubusercontent.com/yaso09/vld/main/build.sh")

vld = g("https://raw.githubusercontent.com/yaso09/vld/main/vld.py")

f = open("vld.py", "w")

f.write(vld)

f.close()

os.system(build)

os.remove("vld.py")



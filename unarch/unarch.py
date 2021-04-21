import patoolib
import os

for num in range(1, 3800):
    if os.path.exists(str(num) + '.rar'):
        os.mkdir(str(num))
        patoolib.extract_archive(str(num) + '.rar', outdir=str(num))

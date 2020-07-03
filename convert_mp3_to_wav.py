from pathlib import Path
import subprocess
import os
#os.system(f"cd Desktop/MusicClassification/acm_mirum_tempo")
os.system("./forPython.sh")
i=Path("C:/Users/Ansh/Desktop/MusicClassification/acm_mirum_tempo")
o=Path("C:/Users/Ansh/Desktop/MusicClassification/Tempo Dataset")
for file in i.rglob('*'):
    inp=str(file).replace('\\','/')
    out=str(i/file.name)[:-8]+'wav'
    out=out.replace('\\','/')
    command=f"ffmpeg -i {inp} -vn -acodec pcm_s16le -ac 1 -ar 22500 -f wav {out}"
    print(command)
    os.system(command)
    #break

import os
#dir=''
for p,ds,fs in os.walk(dir):
    print('#### directory of following srcs/alts is '+p)
    for f in fs:
        if f.endswith(('jpg','jpeg' or 'png')):
            print('src="'+f+'" '+'alt="'+os.path.splitext(f)[0].replace('-',' ')+'"')

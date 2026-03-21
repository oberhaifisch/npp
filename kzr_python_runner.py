r"""
$(FULL_CURRENT_PATH) – Full path of the active file, e.g. E:\My Web\main\welcome.html
$(CURRENT_DIRECTORY) – Directory of the active file, e.g. E:\My Web\main
$(FILE_NAME) – File name with extension of the active file, e.g. welcome.html
$(NAME_PART) – File name without extension, e.g. welcome
$(EXT_PART) – Extension only, e.g. html
$(CURRENT_WORD) – The word currently selected (or under caret)
$(CURRENT_LINE) – Line number of caret (1-based)
$(CURRENT_COLUMN) – Column number of caret (1-based)
$(NPP_DIRECTORY) – Folder where Notepad++ is installed, e.g. C:\Program Files\Notepad++
$(SYS.VARNAME) – Access to a Windows environment variable, e.g. $(SYS.PATH) for %PATH%
$(CURRENT_LINESTR) contents of the current line as a string
"""



import sys
import os
import subprocess
import glob
# print("runner run")
# print('sys.argv\n', ' '.join(sys.argv[1:]), sep='\n')

CELLS_DIVIDER = '# %%'

COMMAND_GROUP = ' '.join(sys.argv[1:])
COMMAND_GROUP = COMMAND_GROUP.split("<")
COMMAND_GROUP = dict([_.split(">") for _ in COMMAND_GROUP])

for key in COMMAND_GROUP:
    COMMAND_GROUP[key] = COMMAND_GROUP[key].strip('"')

# print(*COMMAND_GROUP.items(), sep='\n')

# 'CURRENT_DIRECTORY': '"', 
# 'FULL_CURRENT_PATH': 'new 4', 
# 'NPP_DIRECTORY': 'D:\\HyperV\\npp', 
# 'COMMAND': '-i', 
# 'PYTHON_PATH': 'D:\\HyperV\\WPy64-3880\\python-3.8.8.amd64\\python'

# 'CURRENT_DIRECTORY': 'P:"', 
# 'FULL_CURRENT_PATH': 'P:\\shit.py', 
# 'NPP_DIRECTORY': 'D:\\HyperV\\npp', 
# 'COMMAND': '-i', 
# 'PYTHON_PATH': 'D:\\HyperV\\WPy64-3880\\python-3.8.8.amd64\\python'

# 'CURRENT_DIRECTORY': 'D:\\Рабочие файлы и программы', 
# 'FULL_CURRENT_PATH': 'D:\\Рабочие файлы и программы\\функции.py',
# 'NPP_DIRECTORY': 'D:\\HyperV\\npp', 
# 'COMMAND': '-i', 
# 'PYTHON_PATH': 'D:\\HyperV\\WPy64-3880\\python-3.8.8.amd64\\python'


try:
    CURRENT_DIRECTORY   = COMMAND_GROUP["CURRENT_DIRECTORY"]
    FULL_CURRENT_PATH   = COMMAND_GROUP["FULL_CURRENT_PATH"]
    NPP_DIRECTORY       = COMMAND_GROUP["NPP_DIRECTORY"]
    COMMANDS            = COMMAND_GROUP["COMMANDS"]
    PYTHON_PATH         = COMMAND_GROUP["PYTHON_PATH"]
except:
    input("runner: shit happened")



cmd = ''
if COMMANDS: cmd = COMMANDS.split(",")[0]
    
if not os.path.exists(FULL_CURRENT_PATH):
    CURRENT_DIRECTORY = os.path.join(NPP_DIRECTORY, 'backup')
    tplt = CURRENT_DIRECTORY + '\\' + FULL_CURRENT_PATH + '@*'
    filenames = glob.glob(tplt)
    
    # if not filenames:
        # print(*((_, eval(_)) for _ in dir()), sep='\n')
        ## lena = len(max(dir(), key=len))
        # [print(_.ljust(len(max(globals(), key=len))+1)+'-', eval(_)) for _ in dir()]
        # subprocess.run((PYTHON_PATH, ))
    # else:
    if filenames:
        latest_filename = max(filenames, key=os.path.getctime)
        FULL_CURRENT_PATH = latest_filename
    else:
        print(f"py_runner says: file <{FULL_CURRENT_PATH}> is not found")
        FULL_CURRENT_PATH = CURRENT_DIRECTORY
        # if not os.path.exists(FULL_CURRENT_PATH):
            # from datetime import datetime
            # timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
            # with open(os.path.join(CURRENT_DIRECTORY, FULL_CURRENT_PATH), 'w') as f:
                # pass

        # input("press anykey")
        # exit()

# if 'latest_filename' not in dir():
    # latest_filename = FULL_CURRENT_PATH

def get_python_version():
    global PYTHON_PATH
    with open(FULL_CURRENT_PATH, mode='r', encoding='utf-8') as f:
        line = f.readline()
        if line and line[0] == '#' and line[1] != '#' and 'python' in line:
            PYTHON_PATH = line[1:].strip()

def get_cell_code(curr_line_num, from_start=0):
    with open(FULL_CURRENT_PATH, mode='r', encoding='utf-8') as f:
        lines = f.read().split('\n')

        start = 0
        end = len(lines)
        
        if not from_start:
            print(curr_line_num)
            if lines[curr_line_num].startswith(CELLS_DIVIDER):
                start = curr_line_num
            else:
                for i in range(curr_line_num - 1, -1, -1):
                    if lines[i].startswith(CELLS_DIVIDER):
                        start = i
                        # print('start=', start)
                        break
                        
        
        if lines[curr_line_num].startswith(CELLS_DIVIDER):
            curr_line_num += 1
        for i in range(curr_line_num, len(lines)):
            if lines[i].startswith(CELLS_DIVIDER):
                end = i
                # print('end=', end)
                break
        # print('start=', start, 'end=', end)
        # print('-'*50)
        # print(*lines[start:end], sep='')
        # print('-'*50)
        
    return '\n'.join(lines[start:end])

        
# print(f'{cmd=}')
# print(f'{FULL_CURRENT_PATH=}')
os.chdir(CURRENT_DIRECTORY)
# print("CWD=",os.getcwd())

# print(cmd)

if 0:
    pass
elif cmd == '-i':
    get_python_version()
    subprocess.run((PYTHON_PATH, "-i", FULL_CURRENT_PATH))
elif cmd == '-pylab':
    print('pylab')
    get_python_version()
    os.chdir(CURRENT_DIRECTORY)
    # subprocess.run((PYTHON_PATH, "-m jupyter lab"), shell=True, cwd=CURRENT_DIRECTORY)
    subprocess.run((PYTHON_PATH, "-m", "jupyterlab"))


elif cmd.startswith('-cell'):
    #-cell 42
    curr_line_num = int(cmd.split()[-1])
    get_python_version()
    subprocess.run((PYTHON_PATH, "-i", "-c", get_cell_code(curr_line_num)))
elif cmd == '-gcd':
    subprocess.run((f'explorer.exe /select,"{FULL_CURRENT_PATH}"'))

else:
    get_python_version()
    subprocess.run((PYTHON_PATH, FULL_CURRENT_PATH))
        
# input()
# [print(_, eval(_)) for _ in dir()]









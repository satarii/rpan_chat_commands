import ctypes, sys, os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    os.system('cmd /c "python -m pip install -r %s\\requirements.txt"' % os.getcwd())
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


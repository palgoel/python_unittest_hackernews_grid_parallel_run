from subprocess import Popen


processes = []

for counter in range(2):
    chrome_cmd = 'set BROWSER=chrome && python test.py' #"set" is used in windows and "export" is used for linux n unix
    firefox_cmd = 'set BROWSER=firefox && python test.py'
    processes.append(Popen(chrome_cmd, shell=True))
    processes.append(Popen(firefox_cmd, shell=True))

for counter in range(2):
    processes[counter].wait()
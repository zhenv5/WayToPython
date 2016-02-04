### subprocess module in python

The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. It intends to replace several older modules and functions such as: os.system, os.spawn, os.popen, popen2 and commands. 

[python document: subprocess - subprocess management](https://docs.python.org/2/library/subprocess.html#module-subprocess).

### Running via the shell

```Python
import subprocess
ls_output = subprocess.call('ls -al',shell=True)
ls_output = subprocess.check_call(['ls','-al'])
ls_output = subprocess.check_output('ls -al',shell=True)
ls_output = subprocess.check_output(['ls','-al'])
```
Above are basic usages.

```
ls_output = subprocess.check_output(['ls','-al'])
ls_output = subprocess.check_call(['ls','-al'])
```

The first item in list is the executable and rest are its command line arguments. 

Both **call** and **check_call** can return the return code after running the command. The difference is check_call raises a CalledProcessError if the return code is non-zero.

```Python
ls_output = subprocess.call('ls -al',shell=True)
ls_output = subprocess.check_output('ls -al',shell=True)
ls_output = subprocess.check_output(['ls','-al']])
```

**check_ouput** can run command with arguments and return its output as a byte string. 

With _shell_ setting to _True_, we can pass the commands as a _string_ not a _list_. The program actually gets executed is the OS default shell, _/bin/sh_ on linux and _cmd.exe_ on windows. This can be changed with the _executable_ argument.

### ref

[The ever useful and neat subprocess module](http://sharats.me/the-ever-useful-and-neat-subprocess-module.html)
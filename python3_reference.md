## 24/10/2018 
This is the rework of my old notes in python, I am using the excuse of having an interview to actually go over these notes and improve them with some more knowledge I aquired during my previous internship.
So, the first thing I am changing the file type to an md file, so I can make it preattier  to read. 

A very important git of mine connected with developing in python is the [gitHelpPage](https://github.com/H3xHunter/GitH3xProtocol/blob/master/gitCommands.md)

### Basic Operators
```Python
#Sum
print(2 + 1)

#Subtraction
print(3 - 2)

#Multiplication
print(2 * 2)

#Power
print(2 ** 2)

#Divisions
print(4 / 2.0)
print(int(4 / 2))
print(type(str(4/2)))

#Modulus
print(5 % 2)
print(5 % 1)
```

### Assignment Operators
```Python
#equal
=

#increment
+=

#decrement
-=

#multiply
*=

#divide
(=)

#exponent
**=
```

### Variables
```Python
#int
integer_var = 12
print(type(integer_var))

#float
float_var = 2.5
print(type(float_var))

#string
string_var = 'I am a string' "I am a string"
print(type(string_var))

#boolean
a = 2
b = 3
print(type(a==b))
print(a==b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a!=b)
print(a>b and b==b)
print(a>b or b==b)
```

### Take user input
```Bash
python my_awesome_script par1 par2 par3
```
```Python
my_cool_variable1 = argv[1] 
my_cool_variable2 = argv[2] 
my_cool_variable3 = argv[3] 
```

### Data Type Conversion
```Python
#int(x) Cast an int value
#str(x) Cast a string value
#eval(str) Evaluate the string and return an object
#tuple(s) Convert a read-only touples
#list(s) Convert it to a list
#set(s) Convert it to a set
#dict(d) Creates a dictionary. d must be a sequence of (key,value) tuples.
```

### Print method
```Python
x = "I am a string"
print(x)

age  = 29
sex = "god"
country = "Earth"
name = "Hex"

print("My name is {} and I am {} years old. I am a {} from {}".format(name,age,sex,country))
print("My name is {name} and I am {age} years old. I am a {sex} from {country}".format(name=name,age=age,sex=sex,country=country))

#string are an array of characters 
string = "I am another string"
string[5]
string[1:5]
string[5:]
string[:5]
```

### String formatting: basic methods
```Python
website = "http://www.MINdwareLaB.org"
print(website.upper())
print(website.lower())
print(website.split("."))
print(website.split("//"))
print(website.split("www"))
print(website.split(".")[1])
print(website.split(".")[2])
```

### String formatting: string escape
```Python
#\\	Backslash (\)
print("\\")

#\'	Single quote (')
print("\'")

#\"	Double quote (")
print("\"mindwarelab\"")

#\b	ASCII Backspace (BS)
print("Mindwarelab\b")

#\n	ASCII Linefeed (LF)
print("Mindware\nlab")

#\t	ASCII Horizontal Tab (TAB)
print("\tmindwarelab")
```
### Flow manipulation
```Python
if var1 >= var:
    #do something here
elif var1 <= var2:
    #do something else here
elif var1 == var2:
    #do something else here
else:
    #do something even different here
```

### List, Touples, Dictionaries, Sets
 - Use a dictionary when you have a set of unique keys that map to values.
 - Use a list if you have an ordered collection of items.
 - Use a set to store an unordered set of items.
 - Use a touple to store an unordered set of read-only items

```Python
list1 = [] #this is a list
touples1 = () #this is a touple
disctionaries = {} #this is a dictionary
```

### List
```Python
#Similar to the arrays, but it can contain mixed data type
list1 = ["USA", 99, "guns"]
list2 = [44,77,87.7,55]

#len 
print(len(list1))

#type
print(type(list1))

#max
print(max(list2))

#min
print(min(list2))

#sort
list2.sort()
print(list2)

#Adding items to a list
list1.append("chocolate")
print(list1)

#removing items from a list
print("removed: "+ str(list1.pop(1)))
print(list1)

#check an item inside a list
print("x" in ["x",88,"Torino"])

#two-value list
my_list = []
my_list.append([key,value])
```

### Dictionaries
In dictionaries you cannot have double entries as key like in the lists. There is not append and you can only update a dictionary
```Python
dictionary1 = {"key1":"Ferrari","key2":"Mercedes"}
dictionary2 = {"key1":[14,77,54],"key2":"Mercedes"}
dictionary3 = {"key1":{"numbers":[55,43,99]},"key2":"Mercedes"}

#Accessing values inside a nested dictionary
print(dictionary3["key1"]["numbers"][2])

#some extra things you can do with the dictionaries
print(dictionary1.keys())
print(dictionary1.items())
print(dictionary1.values())

#Adding or updating the dictionary:
mydict = {}
mydict.update({key:value})

#Loop through a dictionary:
for key, value in My_dic
print('{}{}'.format(key,value))
```

### Touples
```Python
#touples are read-only 
tup1 = ("moon", "venus", 2017, 2009)
print(tup1)

#Operation on list of touples
num = [(0,1),(1,1),(0,0)]
for a,b in num: print(a)
```

### Set
```Python
set1 = {1,2,6,7,5,5}
set1.add(9)
set1
```

### Repeated actions
```Python
age_set=[33,56,78,92,11]
for numbers in age_set:
    print("Someone has {} years old".format(numbers))
    print("Increment the age of {} + 1 -> ".format(numbers)+ str(numbers+1)) 

for numbers in list(range(1,10)):
    print(numbers)
    
print(list(range(5)))
    
a = 1
while a < 10:
    print("a is {}".format(a))
    a = a + 1
```

### Appending items to a list with a for loop
```Python
my_list = []
for numbers in range(10):
    my_list.append(numbers **2)
print(my_list)

#List Comprehensions
print([numbers **2 for numbers in range(10)])
print([numbers **2 for numbers in range(10) if numbers % 2 == 0])
```

### functions
```Python
def welcome(name = "{error: name not assigned}"):
    global age
    age = 34
    surname = "Black"
    print("hello {}".format(name))

welcome("MindwareLab")
welcome()

def power(numbers, power):
    return numbers **power

output = power(10,2)
power(7,37)

print(output)

print(age)
print(surname)
```

### Maps and lambda
```Python
from functools import reduce
list_of_number = [1,2,3,4,5,6,7,8,9,10]

#maps a function
def power2(num):
    return num **2
print(list(map(power2,list_of_number)))

#labda functions 
print(list(map(lambda n: n**2, list_of_number)))
print(list(map(lambda n: n**2, range(11))))

#Filters
print(list(filter(lambda x: x<=5, list_of_number)))
print(list(filter(lambda x: x%2 == 0, list_of_number)))
print(list(filter(lambda x: x%2 == 1, list_of_number)))

#Reduce
print(reduce((lambda x, y: x*y), [1,2,3,4,5,6,7,8,9,10]))
print(reduce((lambda x, y: x*y), list_of_number))
```

### Classes
```Python
class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+last+"@mindwarelab.com"
        
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def increse_salary(self):
        self.pay =  int(self.pay + 10)

#Creating Instance Objects
employee1 = Employee("Frak","Lasagna", 10)

#Accessing Attributes
print(employee1.email.lower())
print(employee1.fullname())
print("Salary before the increase in the salary is equal to {}".format(employee1.pay))

#increase the salary
employee1.increse_salary()
print("Salary after the increase in the salary is equal to {}".format(employee1.pay))

#hiding variable
class Missle_luncher:
    __timer = 0 # private variable not callable from outside the class
    def counter(self):
        self.__timer =+1
        print("{} hours before the next strike.".format(self.__timer))

missle1 = Missle_luncher()
missle1.counter()
#print(missle1.__timer) #AttributeError: 'Missle_luncher' object has no attribute '__timer'
```
       
### import libraries and Code introspection
```Python
import pandas
import numpy

#pandas?
#numpy?
#dir(pandas) #functionality
#pandas.DataFrame?
```

### Time handling
```Python
import time
import calendar

localtime = time.asctime( time.localtime(time.time()) )
print ("What time is it? {}".format(localtime))
cal = calendar.month(2017, 4)
print(cal)
```

### Handling errors
```Python
try: #try this code
    pass #some code goes here
except: #if happen this well-know possible exception, please do this
    pass #some code goes here
except: #if happen this well-know possible exception, please do this
    pass #some code goes here
else: #if happens something else that we are not aware of
    pass #some code goes here
finally: #this code will be always execute no matter what
    pass #some code goes here
```

### Regex 
Main module [re](https://docs.python.org/3.3/library/re.html)
- [RegexOne](https://regexone.com/)
- [RegexVisualizer](https://jex.im/regulex/#!flags=&re=%5E(a%7Cb)*%3F%24)

An example taken from the re help page.
```Python

import collections
import re

Token = collections.namedtuple('Token', ['typ', 'value', 'line', 'column'])

def tokenize(s):
    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    token_specification = [
        ('NUMBER',  r'\d+(\.\d*)?'), # Integer or decimal number
        ('ASSIGN',  r':='),          # Assignment operator
        ('END',     r';'),           # Statement terminator
        ('ID',      r'[A-Za-z]+'),   # Identifiers
        ('OP',      r'[+*\/\-]'),    # Arithmetic operators
        ('NEWLINE', r'\n'),          # Line endings
        ('SKIP',    r'[ \t]'),       # Skip over spaces and tabs
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    get_token = re.compile(tok_regex).match
    line = 1
    pos = line_start = 0
    mo = get_token(s)
    while mo is not None:
        typ = mo.lastgroup
        if typ == 'NEWLINE':
            line_start = pos
            line += 1
        elif typ != 'SKIP':
            val = mo.group(typ)
            if typ == 'ID' and val in keywords:
                typ = val
            yield Token(typ, val, line, mo.start()-line_start)
        pos = mo.end()
        mo = get_token(s, pos)
    if pos != len(s):
        raise RuntimeError('Unexpected character %r on line %d' %(s[pos], line))

statements =
    IF quantity THEN
        total := total + price * quantity;
        tax := price * 0.05;
    ENDIF;

for token in tokenize(statements):
    print(token)


```


### Multithreaded Programming
```Python
import _thread
import time

def bomb(name, timer):
    
    while timer > 0:
        #print("{} timer is ticking, {} seconds left\n".format(name, timer))
        timer -=1
        time.sleep(1)
    return print("{} Kabooom!!!\n".format(name))

try:
    _thread.start_new_thread(bomb, ("bomb1",10,))
    _thread.start_new_thread(bomb, ("bomb2",8,))
    _thread.start_new_thread(bomb, ("bomb3",6,))
    _thread.start_new_thread(bomb, ("bomb4",4,))
    _thread.start_new_thread(bomb, ("bomb5",2,))
    _thread.start_new_thread(bomb, ("bomb6",8,))
except:
    print("My God, it is full of stars!")
```

### make an executable
How to install it:
```cmd
python -m pip install cx_Freeze --upgrade
```
Then run ... 
You don't need to create the folder.
```Bash
python setup.py <new_project_name_folder> 
```
[cx_Freeze is a set of scripts and modules for freezing Python scripts into executables](ps://anthony-tuininga.github.io/cx_Freeze/)
```Python
import shutil, os
from cx_Freeze import setup, Executable

packages = [
    'multiprocessing',
    'idna',
    'win32timezone',
]

include_files = [ 
    'your_config_file.xml',
    'your_sexy_icon.ico',
    'sub_folders_you_want_to_include/',
]

exclude = [
    'something', 
]

include = [
]

name_of_the_executable = (Executable("name_of_the_executable.py",
                       targetName="name_of_the_executable.exe",
                       icon="your_sexy_icon.ico", 
                  ))
                                    
setup(
    name="name_of_the_executable",
    version="0.1",
    author="h3x",
    description="Making an executable",
    options={
        'build_exe': {
            'packages': packages,
            'include_files': include_files,
            'includes': include,
            'excludes': exclude,
            'build_exe': 'build',
            'include_msvcr': True,
            'optimize': 2
        }
    },
    executables=[name_of_the_executable]
)
```

### Base64
```Python
import base64

def __file_to_base64(filepath):
	with open(filepath, "rb") as f:
		return base64.b64encode(f.read())
```

### Exceptions handling

#### Basic

```Python
 try:
     print(1 / 0)
except Exception as error:
    raise RuntimeError("Something bad happened") from error
```

#### Rise an exception manually handling it.
```Python
class error_handling(error):
    pass
 
 #somewhere in your code
 if not <this>:
        raise error_handling("Error: something you were trying to do is  not correct.")
```

#### Traceback
```Python
except Exception as e:
    et, ei, tb = sys.exc_info()
    raise ei.with_traceback(tb)
```

#### Loggingg
```Python
import logging
LOG_FILENAME = '/tmp/logging_example.out'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

try:
    do_something_in_app_that_breaks_easily()
except AppError as error:
    logger.error(error)
    raise                 
```

### Generate temporary files and directories
```Python
import tempfile
import shutil

tmpdir = tempfile.mkdtemp()
print("temporary directory at " + tmpdir)

shutil.rmtree(tmpdir)
```

[example](https://programtalk.com/vs2/python/10241/PlagueScanner/avast-agent.py/)

```Python
import tempfile
import subprocess

def scan_file(sample):
    sample_data = sample.read()
    with tempfile.TemporaryDirectory() as td:
        sample_file = os.path.join(td, 'sample')
        fp = open(sample_file, 'wb')
        fp.write(sample_data)
        fp.close()
        command = os.path.join('C:\\', 'Program Files', 'AVAST Software', 'Avast', 'ashCmd.exe')
        scanner = subprocess.Popen([command, '/_', sample_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        stdout, stderr = scanner.communicate()
    return stdout
```

### Working with config files (configparser)
#### [Basic config parser](https://docs.python.org/3/library/configparser.html)

```xml
[DEFAULT]
ServerAliveInterval = 45
Compression = yes
CompressionLevel = 9
ForwardX11 = yes

[bitbucket.org]
User = hg

[topsecret.server.com]
Port = 50022
ForwardX11 = no
```

```Python
import configparser
config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45',
                      'Compression': 'yes',
                      'CompressionLevel': '9'}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'     # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
   config.write(configfile)
 
```

Let's test the config keys inside the config file
```Bash
>>> config = configparser.ConfigParser()

>>> config.sections()
[]

>>> config.read('example.ini')
['example.ini']

>>> config.sections()
['bitbucket.org', 'topsecret.server.com']

>>> 'bitbucket.org' in config
True

>>> 'bytebong.com' in config
False

>>> config['bitbucket.org']['User']
'hg'

>>> config['DEFAULT']['Compression']
'yes'

>>> topsecret = config['topsecret.server.com']

>>> topsecret['ForwardX11']
'no'

>>> topsecret['Port']
'50022'

>>> for key in config['bitbucket.org']:  
...     print(key)
user
compressionlevel
serveraliveinterval
compression
forwardx11

>>> config['bitbucket.org']['ForwardX11']
'yes'
```




#### xml parsing
```xml
<Config>
	<FacebookConfig>
		<api>http://facebook.com/app/api/</api>
		<app_name></app_name>
		<user></user>	
	</FacebookConfig> 
	<Errors>
		<Error name="INVALID_TOKEN" value="TThe provided Facebook token is invalid" />
	</Errors>
	<Messages>
		<Message name="FBTOKEN_SOTRED" value="The provided Facebook token has been successfully stored" />
	</Messages>
</Config>
```

```Python
import os
import xml.etree.ElementTree as CP

class ConfigParserException(Exception):
    pass
    
def __init__(self, filepath, templates_dir):
        self.filepath = filepath
        try:
            xml_config = CP.parse(filepath)
            root = xml_config.getroot()
	except IOError as ie:
            raise ConfigParserException("The config file '{}' cannot be found.".format(filepath))
        except AttributeError as ae:
            raise ConfigParserException("Missing parameters in config file.")
        except CP.ParseError as pe:
            raise ConfigParserException("Error parsing config file)
	for templatefile in os.listdir(self.templates_dir):
            if templatefile.endswith(".xml"): 
                try:
                    xml_config = CP.parse(os.path.join(self.templates_dir,templatefile))
                    xml_template = xml_config.getroot()
                    if xml_template.tag != "template":
                        raise ConfigParserException("Error parsing template file)
                    template_name = xml_template.get('name')
                    template = {}
                    template['description'] = xml_template.get('description')
                    template['attributes'] = {}
                    template['actions'] = []
                    for xml_attribute in xml_template.findall('attribute'):
                        attribute_name = xml_attribute.get('name')
                        attribute = {}
                        attribute['type'] = xml_attribute.get('type')
                        template['attributes'][attribute_name] = attribute
```

### Control Keyboard and Mouse

```Python
import time
import threading
from pynput.mouse import Button, Controller
import pynput.keyboard as kb
import random

delay = 30
button = Button.left
start_stop_key = kb.KeyCode(char='s')
exit_key = kb.KeyCode(char='e')

def action(self):
    arrow_keys = [kb.Key.up,kb.Key.down,kb.Key.right,kb.Key.left]
    return random.choice(arrow_keys)

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                self.action1 = action(self)
                print("{}".format(str(self.action1)))
                keyboard.press(self.action1)
                time.sleep(0.5)
                keyboard.release(self.action1)
                time.sleep(0.5)
                keyboard.press(kb.Key.enter) 
                keyboard.release(kb.Key.enter)
                time.sleep(0.5)
                mouse.click(self.button)
                time.sleep(0.5)
                keyboard.press(kb.Key.enter)
                keyboard.release(kb.Key.enter)
                time.sleep(self.delay)
            time.sleep(0.1)

mouse = Controller()
keyboard = kb.Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            print("Autobot is paused ...")
            click_thread.stop_clicking()
        else:
            print("Autobot is running ...")
            click_thread.start_clicking()
    elif key == exit_key:
        print("Autobot closed.")
        click_thread.exit()
        listener.stop()


with kb.Listener(on_press=on_press) as listener:
    listener.join()
```

### executing external programs in python 
exec() function is used for the dynamic execution of Python program which can either be a string or object code. If it is a string, the string is parsed as a suite of Python statements which is then executed unless a syntax error occurs and if it is an object code, it is simply executed. We must be careful that the return statements may not be used outside of function definitions not even within the context of code passed to the exec() function. It doesn;t returnn any value, hence returns None.
Syntax:

exec(object[, globals[, locals]])

It can take three parameters:
    - object: As already said this can be a string or object code
    - globals: This can be a dictionary and the parameter is optional
    - locals: This can be a mapping object and is also optional
    
Example 1   
```Python
prog = 'print("The sum of 5 and 10 is", (5+10))'
exec(prog) 
```
Example 2
```Python
def execfile(status, filepath, globals=None, locals=None):
    if not status:
        if globals is None:
            globals = {}
        globals.update({
            "__file__": filepath,
            "__name__": "__main",
        })
        with open(filepath, 'rb') as file:
            exec(compile(file.read(), FILENAME, 'exec'), globals, locals)
            return True
    else:
return True```

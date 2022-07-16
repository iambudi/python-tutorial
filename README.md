# Python Tutorial 
This tutorial repo would be my journey of learning Python. I will add or update the repo as i learn more.

## 1. Requirement
* Download [Python version >= 3.10](https://www.python.org/ftp/python/3.10.0/python-3.10.0-macos11.pkg) for osx or install using brew.
It will install python in folder `/Library/Frameworks/Python.framework/Versions/3.10/bin` or `/opt/homebrew/Cellar/python@3.10`

* Check if `python3` and `pip3` can be called anywhere.
***pip3** is a package manager for python*
> If python 3 would be default python version, put it as shell alias for easier call. Below python or pip i write refer to alias version 3.
```bash
alias "python=/opt/homebrew/opt/python@3.10/bin/python3"
alias "pip=/opt/homebrew/opt/python@3.10/bin/pip3"
```

* Install requirement packages used in this tutorial
  `pip install aiohttp more-itertools pytz`

  **[TODO]** put it inside `requirement.txt`
* Optional to enable python linting
`pip install -U pylint` 

## 2. Running Tutorial
If you use VSCode, just open a python file and press play button on top right of vscode editor to run file in terminal.

> Make sure to install Microsoft Python VSCode Extension first.

To run manually on terminal: `python src/basic/file.py`

## 3. Basic of Python
`src/basic`
|   No | Name                                                      | Description                                                                   |
| ---: | --------------------------------------------------------- | ----------------------------------------------------------------------------- |
|    1 | [Variables](src/basic/vars.py)                            | Introduction to python comment, variable, print to console and var assignment |
|    2 | [Type](src/basic/type.py)                                 | How to use and create python data type                                        |
|    3 | [Function](src/basic/function.py)                         | Define and call function                                                      |
|    4 | [Exception Handling](src/basic/exception_handling.py)     | [TODO] How to handle error or exception                                       |
|    5 | [Class](src/basic/class.py)                               | OOP                                                                           |
|    6 | [Abstract Class](src/basic/class_abstract.py)             | OOP - Contract interface                                                      |
|    7 | [Generic Class](src/basic/class_generic.py)               | Using generic data type in class                                              |
|    8 | [Decorator](src/basic/decorator.py)                       | Extend function using Meta programming                                        |
|    9 | [Data Class](src/basic/data_class.py)                     | Enhance class with special decorator                                          |
|   10 | [Comprehension](src/basic/comprehension.py)               | Creating list based on based on existing list. For one liner lover :)         |
|   11 | [Functional Programming](src/basic/func_programming.py)               | Lambda, Closure, Map, Filter, Reduce         |
|   12 | [Date Time](src/basic/date_time.py)                       | Date and Time manipulation and formatting                                     |
|   13 | [Database](src/basic/db.py)                               | How to read and write from database                                           |
|   14 | [Iterator](src/basic/iterator.py)                         | Traversing oject values                                                       |
|   15 | [Generator](src/basic/generator.py)                       | Iterator in Lazy version                                                      |
|   16 | [Asynchronous](src/basic/async_await.py)                  | Write concurrent code using asyncio                                           |
|   17 | [Async Http Request](src/basic/async_await.py)            | Write asynchronous http request                                               |
|   18 | [Serialization JSON](src/basic/serialization_json.py)     | Handle json data                                                              |
|   19 | [Serialization Pickle](src/basic/serialization_pickle.py) | Serializing and de-serializing Python object structures                       |
|   20 | [Multi Threading](src/basic/multi_threading.py)           | Pararrel processing using Multi Threading (MT) and Multi Process (MP)         |
|   21 | [Regex](src/basic/regex.py)                               | Regular Expression                                                            |

## 4. Unit Test
How to write [unit testing](src/testing/test_add.py) in python

## 5. Leet Code
Practice solving leet code using python
|   No | Name                                                    | Description                                                                       |
| ---: | ------------------------------------------------------- | --------------------------------------------------------------------------------- |
|    1 | [Two Sum Problem](src/leet/two_sum.py)                          | Sum of two int element in a list match to the target int |
|    2 | [Consecutive Chars](src/leet/consecutive_chars.py)      | Count consecutive repeated chars from a string and return in a List of Dictionary |
|    3 | [First Duplicate Number](src/leet/first_duplicate_number.py) | Find value of duplicate number found in a list with shortest occurrance index |
|    4 | [First Unique Char](src/leet/first_unique_char.py)      | Find first unique char in a string (non repeating char) |
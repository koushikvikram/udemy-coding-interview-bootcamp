# [Getting Started With Testing in Python](https://realpython.com/python-testing/#more-advanced-testing-scenarios)

Contents
--------------------------------------------------------
Testing Your Code
- Automated vs Manual Testing
- Unit Tests vs Integration Tests
- Choosing a Test Runner

Writing Your First Test
- Where to write the test
- How to structure a simple test
- How to write assertions
- Side effects

Executing Your First Test
- Executing Test Runners
- Running Your Tests From Visual Studio Code

-----------------------------------------------------------

## Testing Your Code

### Automated vs Manual Testing

**Exploratory Testing** - A form of **manual testing**. Done without a plan. You just explore the application. 

- Make a list of all the features your application has 
- the different types of input it can accept
- the expected results 

Now, every time you make a change to your code, you need to go through every single item on that list and check it.

**Automated Testing** - Execution of your test plan by a **script** instead of a human.

Test plan usually refers to
- the parts of your application you want to test
- the order in which you want to test them
- the expected responses

Python already comes with a set of tools and libraries to help you create automated tests for your application. 

## Unit Tests vs Integration Tests

**Integration Testing** - Testing multiple components.  
Eg. Testing the lights on a car - You would turn on the lights (known as the **test step**) and go outside the car or ask a friend to check that the lights are on (known as the **test assertion**).

Components - parts of your application - classes, functions, modules, etc.

> A major challenge with integration testing is that when an integration test doesn't give the right result, it's hard to diagnose the issue without being able to isolate which part of the system is failing.

If the lights didn’t turn on, then maybe the bulbs are broken. Is the battery dead? What about the alternator? Is the car’s computer failing?

**Unit Testing** - A smaller test. One that checks that a single component operates in the right way. A unit test helps you to isolate what is broken in your application and fix it faster.

To write a unit test for the built-in function ```sum()```, you would check the output of ```sum()``` against a known output.

```python
>>> assert sum([1, 2, 3]) == 6, "Should be 6"
```

If the result from sum() is incorrect, this will fail with an AssertionError and the message "Should be 6".

```python
>>> assert sum([1, 1, 1]) == 6, "Should be 6"

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: Should be 6
```

Instead of testing on the REPL, you’ll want to put this into a new Python file called ```test_sum.py``` and execute it again:

```python
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")
```

Now you have written 
- a test case
- an assertion
- an entry point (the command line). 

You can now execute this at the command line:

```bash
$ python test_sum.py

Everything passed
```

In Python, ```sum()``` accepts any **iterable** as its first argument. You tested with a list. Now test with a tuple as well. Create a new file called ```test_sum_2.py``` with the following code:

```python
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")
```

Upon execution, we get

```bash
$ python test_sum_2.py

Traceback (most recent call last):
  File "test_sum_2.py", line 9, in <module>
    test_sum_tuple()
  File "test_sum_2.py", line 5, in test_sum_tuple
    assert sum((1, 2, 2)) == 6, "Should be 6"
AssertionError: Should be 6
```

Here you can see how a mistake in your code gives an error on the console with some information on where the error was and what the expected result was.

> Writing tests in this way is okay for a simple check, but what if more than one fails? This is where **test runners** come in. 

The test runner is a special application designed for running tests, checking the output, and giving you tools for debugging and diagnosing tests and applications.

### Choosing a test runner

There are many test runners available for Python. 
> The one built into the Python standard library is called ```unittest```. 

In this tutorial, you will be using ```unittest``` test cases and the ```unittest``` test runner. The principles of ```unittest``` are easily portable to other frameworks. The three most popular test runners are:
- ```unittest```
- ```nose``` or ```nose2```
- ```pytest```

Choosing the best test runner for your requirements and level of experience is important.

#### unittest

```unittest``` contains both a testing framework and a test runner. ```unittest``` has some important requirements for writing and executing tests.

```unittest``` requires that:
- You put your tests into classes as methods
- You use a series of special assertion methods in the ```unittest.TestCase``` class instead of the built-in ```assert``` statement

To convert the earlier example to a unittest test case, you would have to:

1. Import ```unittest``` from the standard library
2. Create a class called ```TestSum``` that inherits from the ```TestCase``` class
3. Convert the test functions into methods by adding self as the first argument
4. Change the assertions to use the ```self.assertEqual()``` method on the ```TestCase``` class
5. Change the command-line entry point to call ```unittest.main()```

Follow those steps by creating a new file ```test_sum_unittest.py``` with the following code:

```python
import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
```

If you execute this at the command line, you’ll see one success (indicated with .) and one failure (indicated with F):

```bash
$ python test_sum_unittest.py
.F
======================================================================
FAIL: test_sum_tuple (__main__.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_sum_unittest.py", line 9, in test_sum_tuple
    self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
AssertionError: Should be 6

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
```

#### nose2

You may find that over time, as you write hundreds or even thousands of tests for your application, it becomes increasingly hard to understand and use the output from unittest.

```nose2``` is compatible with any tests written using the unittest framework and can be used as a drop-in replacement for the ```unittest``` test runner.

To get started with ```nose2```, install ```nose2``` from PyPI and execute it on the command line. ```nose2``` will try to discover all test scripts named ```test*.py``` and test cases inheriting from ```unittest.TestCase``` in your current directory:

```bash
$ pip install nose2
$ python -m nose2
.F
======================================================================
FAIL: test_sum_tuple (__main__.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_sum_unittest.py", line 9, in test_sum_tuple
    self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
AssertionError: Should be 6

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
```

```nose2``` offers many command-line flags for filtering the tests that you execute.

#### pytest

```pytest``` supports execution of ```unittest``` test cases. 

> The real advantage of ```pytest``` comes by writing ```pytest``` test cases. ```pytest``` test cases are a series of functions in a Python file starting with the name ```test_```.

pytest has some other great features:
- Support for the built-in assert statement instead of using special ```self.assert*()``` methods
- Support for filtering for test cases
- Ability to rerun from the last failing test
- An ecosystem of hundreds of plugins to extend the functionality

Writing the TestSum test case example for pytest would look like this:

```python
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"
```

**You have dropped the TestCase, any use of classes, and the command-line entry point.**

---------------------------------------------------------

## Writing Your First Test

Create a new project folder and, inside that, create a new folder called ```my_sum```. Inside ```my_sum```, create an empty file called ```__init__.py```. Creating the ```__init__.py``` file means that the ```my_sum``` folder can be imported as a module from the parent directory.

Your project folder should look like this:
```
project/
│
└── my_sum/
    └── __init__.py
```
Open up ```my_sum/__init__.py``` and create a new function called ```sum()```, which takes an iterable (a list, tuple, or set) and adds the values together:

```python
def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total
```

### Where to Write the Test

To get started writing tests, you can simply create a file called ```test.py```, which will contain your first test case. Because the file will need to be able to import your application to be able to test it, you want to place ```test.py``` above the package folder, so your directory tree will look something like this:

```
project/
│
├── my_sum/
│   └── __init__.py
|
└── test.py
```

You’ll find that, as you add more and more tests, your single file will become cluttered and hard to maintain, so you can create a folder called ```tests/``` and split the tests into multiple files. It is convention to ensure each file starts with ```test_``` so all test runners will assume that Python file contains tests to be executed. Some very large projects split tests into more subdirectories based on their purpose or usage.

### How to structure a simple test

Before you dive into writing tests, you’ll want to first make a couple of decisions:
- What do you want to test?
- Are you writing a unit test or an integration test?

Then the structure of a test should loosely follow this workflow:
- Create your inputs
- Execute the code being tested, capturing the output
- Compare the output with an expected result

For this application, you’re testing ```sum()```. There are many behaviors in ```sum()``` you could check, such as:
- Can it sum a list of whole numbers (integers)?
- Can it sum a tuple or set?
- Can it sum a list of floats?
- What happens when you provide it with a bad value, such as a single integer or a string?
- What happens when one of the values is negative?

The most simple test would be a list of integers. Create a file, ```test.py``` with the following Python code:

```python
import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
```

### How to Write Assertions

The last step of writing a test is to validate the output against a known response. This is known as an **assertion**. There are some general best practices around how to write assertions:
- Make sure tests are repeatable and run your test multiple times to make sure it gives the same result every time
- Try and assert results that relate to your input data, such as checking that the result is the actual sum of values in the ```sum()``` example

```unittest``` comes with lots of methods to assert on the values, types, and existence of variables. Here are some of the most commonly used methods:

|Method	| Equivalent to |
|-------|---------------|
|```.assertEqual(a, b)```|	```a == b``` |
|```.assertTrue(x)```|	```bool(x) is True``` |
|```.assertFalse(x)```|	```bool(x) is False```|
|```.assertIs(a, b)```|	```a is b```|
|```.assertIsNone(x)```|	```x is None```|
|```.assertIn(a, b)```|	```a in b```|
|```.assertIsInstance(a, b)```|	```isinstance(a, b)```|


```.assertIs()```, ```.assertIsNone()```, ```.assertIn()```, and ```.assertIsInstance()``` all have opposite methods, named ```.assertIsNot()```, and so forth.

### Side Effects

When you’re writing tests, it’s often not as simple as looking at the return value of a function. Often, executing a piece of code will alter other things in the environment, such as the attribute of a class, a file on the filesystem, or a value in a database. These are known as side effects and are an important part of testing. Decide if the side effect is being tested before including it in your list of assertions.

If you find that the unit of code you want to test has lots of side effects, you might be breaking the **Single Responsibility Principle**. Breaking the Single Responsibility Principle means the piece of code is doing too many things and would be better off being refactored. Following the Single Responsibility Principle is a great way to design code that it is easy to write repeatable and simple unit tests for, and ultimately, reliable applications.

----------------------------------------------------------

## Executing Your First Test

Before you create more complex tests, you should check that you can execute the tests successfully.

### Executing Test Runners

> The Python application that executes your test code, checks the assertions, and gives you test results in your console is called the **test runner**.

At the bottom of ```test.py```, you added this small snippet of code:

```python
if __name__ == '__main__':
    unittest.main()
```

This is a **command line entry point**. It means that if you execute the script alone by running python ```test.py``` at the command line, it will call ```unittest.main()```. This executes the test runner by discovering all classes in this file that inherit from ```unittest.TestCase```.

Another way is using the unittest command line. Try this:

This will execute the same test module (called ```test```) via the command line.

```bash
$ python -m unittest test
```

Verbose

```bash
$ python -m unittest -v test
```

Instead of providing the name of a module containing tests, you can request an auto-discovery. This will search the current directory for any files named ```test*.py``` and attempt to test them.

```bash
$ python -m unittest discover
```

Once you have multiple test files, as long as you follow the test*.py naming pattern, you can provide the name of the directory instead by using the -s flag and the name of the directory:

```bash
$ python -m unittest discover -s tests
```

Lastly, if your source code is not in the directory root and contained in a subdirectory, for example in a folder called src/, you can tell unittest where to execute the tests so that it can import the modules correctly with the -t flag:

```bash
$ python -m unittest discover -s tests -t src
```

unittest will change to the ```src/``` directory, scan for all ```test*.py``` files inside the the tests directory, and execute them.

### Running Your Tests From Visual Studio Code

If you’re using the Microsoft Visual Studio Code IDE, support for ```unittest```, ```nose```, and ```pytest``` execution is built into the Python plugin.

If you have the Python plugin installed, you can set up the configuration of your tests by opening the Command Palette with ```Ctrl+Shift+P``` and typing “Python test”. You will see a range of options:

Choose **Debug All Unit Tests**, and VSCode will then raise a prompt to configure the test framework. Click on the cog to select the test runner (```unittest```) and the home directory (.).

Once this is set up, you will see the status of your tests at the bottom of the window, and you can quickly access the test logs and run the tests again by clicking on these icons.


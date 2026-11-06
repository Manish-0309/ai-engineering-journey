# AI Engineering Journey

A topic-based record of my progress as I learn AI engineering. This README tracks what I am learning by subject, rather than by day.

## Learning roadmap

- [x] Python foundations
- [ ] Data handling and software development foundations
- [ ] Machine learning and deep learning
- [ ] Generative AI and large language models
- [ ] Prompt engineering and LLM application development
- [ ] Embeddings, vector databases, and retrieval-augmented generation (RAG)
- [ ] AI agents and workflows
- [ ] Evaluation, deployment, and monitoring

## Topics covered

### Python foundations

#### Python basics

- **Introduction to Python**: High-level, interpreted, general-purpose programming language with dynamic typing and multi-paradigm support
- **Print function**: Using `print()` with custom separators and end characters
- **Variables**: Dynamic typing, multiple assignments, and value swapping
- **Data types**: Numeric (`int`, `float`, `complex`), Boolean, sequence (`list`, `tuple`, `range`), mapping (dictionary), set, and `None` types
- **Type checking**: Using `type()` to identify variable data types
- **User input**: Taking input with `input()` and type casting (implicit and explicit conversions)

#### Operators

- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Bitwise operators
- Membership operators
- Identity operators

#### Control flow

Control flow lets Python programs make decisions, repeat tasks, and change execution order. Without it, programs execute from top to bottom.

- **Conditionals**: `if`, `elif`, and `else` statements for decision making
- **Truthiness**: Truthy and falsy values
- **Loops**: `for` and `while` loops for repetitive tasks
- **Loop control**: `break`, `continue`, and `pass` statements

#### Data structures

##### Lists

- List basics and methods
- List slicing
- `enumerate()` and `len()`
- List comprehensions

##### Tuples

- Tuple basics and immutability
- Tuple creation and indexing
- Tuple unpacking and multiple assignment
- Tuple slicing and iteration
- Common tuple use cases

##### Sets

- Set creation and uniqueness of elements
- Set operations: union, intersection, difference, symmetric difference
- Adding and removing items


##### Dictionaries

- Dictionary creation and key-value pairs
- Accessing values with keys
- Updating, adding, and removing entries
- Common dictionary methods (`keys()`, `values()`, `items()`, `get()`, `update()`)
- Iterating through dictionaries
- Nested dictionaries and dictionary comprehensions

#### Functions

- Defining and calling reusable functions with `def`
- Parameters and arguments, including single and multiple parameters
- Default parameter values and return values
- Variable-length arguments: `*args` for positional arguments and `**kwargs` for keyword arguments
- Combining positional and keyword arguments, and the rule that positional arguments must come before keyword arguments in a call
- Recursive functions and the importance of a base case

#### Lambda, map, and filter

- **Lambda functions**: Anonymous, single-expression functions, including examples with multiple arguments and sorting with a `key` function. See [lambda_function.ipynb](./python/lambda_function.ipynb).
- **`map()`**: Applying a function to each item in one or more iterables, including transforming numbers and extracting values from dictionaries. See [mapfunctions.ipynb](./python/mapfunctions.ipynb).
- **`filter()`**: Selecting items that satisfy a condition, including filtering numbers and dictionaries. See [filterfunction.py](./python/filterfunction.py).

#### File handling

- Text and binary files and common file modes (`r`, `w`, `a`, `r+`, and `w+`)
- Reading, writing, and appending content, using `with` to manage files, and writing multiple lines
- Copying content from one file to another and counting lines in a file

See the [file-handling notebook](./python/file_handling/file_handling.ipynb), [about_files.txt](./python/file_handling/about_files.txt), [writelines.txt](./python/file_handling/writelines.txt), and [countinfiles.py](./python/file_handling/countinfiles.py).

## Repository guide

### Python lessons

- [basic.ipynb](./python/basic.ipynb): Python basics, variables, and data types
- [operators.ipynb](./python/operators.ipynb): Python operators
- [control_flow.ipynb](./python/control_flow.ipynb): Conditional statements and loops
- [list.py](./python/list.py): List operations, methods, nested lists, and comprehensions
- [list_slicing.ipynb](./python/list_slicing.ipynb): List slicing examples
- [tuples.ipynb](./python/tuples.ipynb): Tuple operations
- [sets.ipynb](./python/sets.ipynb): Set operations
- [dictionary.ipynb](./python/dictionary.ipynb): Dictionary operations
- [functions.ipynb](./python/functions.ipynb): Function examples
- [lambda_function.ipynb](./python/lambda_function.ipynb): Lambda expressions
- [mapfunctions.ipynb](./python/mapfunctions.ipynb): The `map()` built-in
- [filterfunction.py](./python/filterfunction.py): The `filter()` built-in

### File handling examples

- [file_handling.ipynb](./python/file_handling/file_handling.ipynb): Reading, writing, appending, and copying file content
- [about_files.txt](./python/file_handling/about_files.txt): Text-file example used by the file-handling lesson
- [writelines.txt](./python/file_handling/writelines.txt): Text-file example for line-based writing
- [countinfiles.py](./python/file_handling/countinfiles.py): Counts the lines in a file

### Practice

- [product_collection.ipynb](./practice1/product_collection.ipynb): Practice with product lists and tuples and a category set

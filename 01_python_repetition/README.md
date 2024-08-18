# Python summary 

Watch the video on Python summary part 1 - functional :tv:
[![python_summary part 1](https://github.com/kokchun/assets/blob/main/python/python_summary_part1_video.png?raw=true)](https://www.youtube.com/watch?v=szKVpybz2Gg)

Watch the video on Python summary part 2 - functional :tv:
[![python_summary part 2](https://github.com/kokchun/assets/blob/main/python/python_summary_part2_video.png?raw=true)](https://youtu.be/twlOySku1PM)

Watch the video on Python summary part 3 - functional :tv:
[![python_summary part 3](https://github.com/kokchun/assets/blob/main/python/python_summary_part3_video.png?raw=true)](https://youtu.be/Y1_P4ZMGLGo)

Watch the video on Python summary part 4 - functional :tv:
[![python_summary part 4](https://github.com/kokchun/assets/blob/main/python/python_summary_part4_video.png?raw=true)](https://youtu.be/fh5rZY4AVOI)

Watch the video on Python summary part 5 - OOP :tv:
[![python_summary part 5](https://github.com/kokchun/assets/blob/main/python/python_summary_part5_video.png?raw=true)](https://youtu.be/fNOUYJzxNTg)

Watch the video on Python summary part 6 - OOP :tv:
[![python_summary part 6](https://github.com/kokchun/assets/blob/main/python/python_summary_part6_video.png?raw=true)](https://youtu.be/4QyyCbLBAWk)




In this folder, you'll find jupyter notebooks for summary of different Python concepts starting from fundamentals to object oriented programming. These concepts are useful and prepares you for your continued journey in Python into data processing.

> Study tip: if some programming concepts are unfamiliar to you, make sure to learn it. Concepts are more important than syntax, as the syntax will come the more you write in the language. Make use of lecture notes, LLM and classical googling. 

## Setup 

This setup requires that you have the following prerequisites already setup
- python
- pip 

If you haven't [installed Python](https://www.python.org/downloads/),  install **3.11**, don't install 3.12. Also remember to tick the box: `add to path` in the installation, in order for Python to be properly installed. 

> [!WARNING]
> Don't install several versions of python if you don't have experience in switching between versions, e.g. using pyenv. 

### Virtual environment

We'll be using a virtual environment with the [uv package](https://github.com/astral-sh/uv), which is a package installer and resolver for Python. Start by installing uv globally using this command

```bash
pip install uv
```

> [!NOTE]
> Make sure no virtual environment is activated when running that comamnd in order to install it globally. 


Navigate to your repository and run 

```bash
uv venv 
```
This creates a `.venv`  directory, which stores information of your virtual environment. Now you can activate this venv through 

```bash
# in windows
source .venv/Scripts/activate

# in mac/linux
source .venv/bin/activate
```

> [!NOTE]
> On `windows`, you should use git bash, and not powershell or cmd. You can configure vscode to open git bash as default terminal. 

You will see a paranthesis around your directory name in the terminal when your venv is activated. Now you can install packages without affecting the global installations.


## Other videos :video_camera:

Learn [Git and GitHub][git_tutorial] for version control and file storage

[git_tutorial]: https://www.youtube.com/watch?v=USjZcfj8yxE

  When entering the commands `python` or `pip` in command prompt or terminal and there is an error :x:, you need to set the path manually
  - set path in [Windows][windows_path]
  - set path in [Mac/Linux][mac_path]
  
[windows_path]: https://www.youtube.com/watch?v=dj5oOPaeIqI 
[mac_path]: https://www.youtube.com/watch?v=PUIE7CPANfo

Concepts 
- learn [variables][variables] to store data
- learn [input][input] to let user input to the program
- learn [while statement][while_video] to repeat code with given condition
- learn [for statement][for_video] to efficiently repeat code
- learn [lists][lists_video] for organizing data
- learn [list comprehension][list_comp_vid] for efficient and clean code
- learn [matplotlib][matplot_video] to plot graphs
- learn [functions][func_vid] to organize and reuse code
- learn [strings][string_vid] to work with text
- learn [f-string][f_string_vid] to nicely format strings
- learn [exceptions][except_vid] for error handling
- learn [files][file_vid] for reading and writing to files
- learn [dictionary][dict_vid] for storing and accessing data using key-value pairs
- learn [numpy](https://www.youtube.com/watch?v=DcfYgePyedM) for working with arrays, computations and mathematics

[file_vid]: https://www.youtube.com/watch?v=4mX0uPQFLDU
[dict_vid]: https://www.youtube.com/watch?v=XCcpzWs-CI4
[except_vid]: https://www.youtube.com/watch?v=nlCKrKGHSSk&t=1s
[func_vid]: https://www.youtube.com/watch?v=NE97ylAnrz4
[string_vid]: https://www.youtube.com/watch?v=k9TUPpGqYTo
[f_string_vid]: https://www.youtube.com/watch?v=nghuHvKLhJA
[matplot_video]: https://www.youtube.com/watch?v=nzKy9GY12yo
[for_video]: https://www.youtube.com/watch?v=OnDr4J2UXSA
[lists_video]: https://www.youtube.com/watch?v=ohCDWZgNIU0&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=14
[list_comp_vid]: https://www.youtube.com/watch?v=AhSvKGTh28Q&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=22
[venv_video]: https://www.youtube.com/watch?v=Kg1Yvry_Ydk&t=1s
[while_video]: https://www.youtube.com/watch?v=6TEGxJXLAWQ
[variables]: https://www.youtube.com/watch?v=Z1Yd7upQsXY&t=470s
[input]: https://www.youtube.com/watch?v=4OX49nLNPEE

OOP 
- [OOP - Real Python][OOP_real]
- [OOP - w3schools][w3OOP]
- [property][prop]
- [type hints](https://realpython.com/lessons/type-hinting/)
- [documentation - Real Python](https://realpython.com/documenting-python-code/)
- [operator overloading](https://www.geeksforgeeks.org/operator-overloading-in-python/)
- [polymorphism](https://www.programiz.com/python-programming/polymorphism)
- [UML](https://python.astrotech.io/design-patterns/uml/class-diagram.html)
- [classes - Python docs](https://docs.python.org/3/tutorial/classes.html)
- [property - Python docs](https://docs.python.org/3/library/functions.html?highlight=property#property)
- [namespace - Python docs](https://docs.python.org/3/glossary.html#term-namespace)

Some other useful concepts
- [modules - w3schools](https://www.w3schools.com/python/python_modules.asp)
- [theory about unit testing](https://en.wikipedia.org/wiki/Unit_testing)
- [dataclasses - Python docs](https://docs.python.org/3/library/dataclasses.html?highlight=dataclass#module-dataclasses)
- [dataclasses - Hjelle G. A. Real Python ](https://realpython.com/python-data-classes/)

[OOP_real]: https://realpython.com/python3-object-oriented-programming/
[w3OOP]: https://www.w3schools.com/python/python_classes.asp
[prop]: https://www.programiz.com/python-programming/property

## Read more :eyeglasses:

Concepts 
- learn [Classes and objects][class_vid] for code organization and reusability 
- continue on [classes and objects][class_vid2]
- [UML](https://realpython.com/lessons/uml-diagrams/)

[class_vid]: https://www.youtube.com/watch?v=wfcWRAxRVBA
[class_vid2]: https://www.youtube.com/watch?v=WOwi0h_-dfA
# tudmil - Turtle-drawing graphics mini language

This is my Python 3.11 based implementation of Exercise 5 of *Pragmatic Programmer*[1] : a mini-language
for drawing "turtle" graphics. 

## Usage

```shell
python tudmil.py <input_file> 
```

This saves a figure `output.png`  in the current directory.

### Input file

The input file is a text file with one command per line. Commands consists of a single-letter, and
some commands accept a numeric argument separated by space. See [](example_input.txt) for an example
from [1]. Notice that `#` denotes comments, and everything after that symbol is ignored.

Currently, every file must begin with a `P`  command and end with `U`

## References

[1] Hunt, Andrew; Thomas, Dave. The Pragmatic Programmer: From Journeyman to Master. Reading: Addison Wesley, 2000

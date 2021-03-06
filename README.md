# Stackscript
<img align="right" src="reference/example.png">

Stackscript is an interpreted [concatinative language](https://en.wikipedia.org/wiki/Concatenative_programming_language),
written in python 3.10. The language's goal is to be able to (theoretically) function as a general purpose language feature wise. It was coded in seven days or less,
as it is customary for world changing innovations.

Although the language "probably" won't change much syntax wise, it is always possible that old code breaks, especially modules as some functions might be changed or transferred into other modules or to and from the builtins.

Stackscript is inspired by [porth](https://gitlab.com/tsoding/porth) by tsoding [twitch](https://www.twitch.tv/tsoding) / [youtube](https://www.youtube.com/c/TsodingDaily), which is way better and acutally compiled to machine code.

Sadly Github does not support markdown for custom file types :( <br>
For that reason colored screenshots are appended to the documentation when there's a bit more code.
ALso Github thinks `.st` files are "[smalltalk](https://en.wikipedia.org/wiki/Smalltalk)" files. That is not true. `.st` stands for stackscript. Github really should be having a feature for custom languages.

### Run The Interpreter
Until running scripts from the command line is supported (yk, with a cool `stackscript -r path/to/myfile.st` or sth like that), just execute either [console.py](console.py) or [from_file.py](from_file.py) to (as the names imply) start either a command line session or run a `.st` respectively. 

### Navigation
- [Syntax Highlighting](editors/syntaxHighlighting.md)
- [Language Reference](reference/reference.md)
  - [Syntax & Builtins](reference/reference/structure_syntax_builtins.md)
  - [Program FLow](reference/reference/program_flow.md)
  - [Variables & Modules](reference/reference/variables_modules.md)
- [Examples](examples/examples.md)
  
### TODO:
<details>
<summary>General TODO's</summary>

  - [ ] make a logo
  - [ ] restructure / refactor a lot
  - [ ] create/fix a bunch of examples
  - [ ] find out what's important to do next
</details>

<details>
<summary>Language features</summary>

  - [x] modules
  - [ ] imports from local scope files ("relative imports"?)
  - [x] convert builtins to module that's imported automatically
  - standard modules
    - [x] math
    - [x] types
    - [x] os
    - io:
      - [x] file
      - [ ] networking
  - [ ] simple gfx/window module to draw on canvas for example
  - [ ] consistent error throwing
  - [ ] error handling try/except, etc
  - [ ] support for "instant key input" without the need to press enter (as used in vim for example)
  - [ ] map python's sqlite3 to a stackscript module (most likely just named "sql")
</details>

<details>
<summary>Documentation</summary>

  - [x] figure out structure
  - [x] first draft
  - [x] finish the first version
  - [ ] keep it up to date
</details>

# Structure, Syntax & Builtins
###### Go back to [README](../../README.md).
###### Go back to [reference](../reference.md).
###### [Next](program_flow.md)

---

###### Go down to [Builtins](#Builtins).

---

### Structure & Syntax
Stackscript is made of two main components: the stack and the... variable stack.
Let's first focus on the normal stack. (You can learn more about variables [here](variables_modules.md))

You can follow the explanation with the command line interface by executing [console.py](../../console.py).

A stackscript file typically ends with `.st`, or in case of [modules](variables_modules.md#modules) that map python
libraries, `.st.py`.

---
###### Go to [top](#Structure-Syntax--Builtins).
To add a value to the stack, simply write it and pressing enter:
`1`<kbd>Enter</kbd><br>
Valid values are: `ints/floats`, `true/false` and `"strings"/'also strings'`.

The stack shows up as a list by default after every line as a list, the right side representing the top: <br>
(The command line arguments, currently only path to interpreter, are on the stack by default but can either be removed by `drop` or `clear`)<br>
`["path/to/console.py", 1]`<br>
The command line arguments (here only the paht of the executed file) are on the stack by default.
If you want to clear the stack, simply write `clear`.<br>
`[]`<br>
Tokens are separated by either whitespace or a newline. That means you can write multiple instructions into one line:
`42 96`. This will push both values onto the stack.<br>
`[42, 96]`

Comments are proceeded by `//`, similar to Java/C/C++/C#/js/...<br>
There are no multiline comments.

---
###### Go to [top](#Structure-Syntax--Builtins).
Now let's add the two values on the stack. To execute an operation, simply write it: `+`.
The operation will take as many values as it needs from the stack, in this case two (a + b).
After the execution of the operation, the result will be appended onto the stack again.<br>
`[138]`<br>
If an operation doesn't find enough values, it will throw an error.

Onto something more difficult:<br>
We want to find out what the previously computed `138` times `(8-6)` is. To do that, we first add `8`and `6` onto the stack,
then execute minus, popping `8` and `6` off the stack and returning `2` onto the stack, and then execute multiplication:
`8 6 - *` (note that a whitespace is required after each token and that the `138` is still on the stack. If you cleared she stack before, the `*` will onyl find one value and throw an error).<br>
`[276]`<br>
As we can see the result is `276`! Good job!

```
// in cnsole, whole code from above:
# clear
[]
# 42 96
[42, 96]
# +
[138]
# 8 6 - *
[276]
#
```

---
###### Go to [top](#Structure-Syntax--Builtins).
As you might have seen, the operations pop their arguments off the stack.
This is less than ideal when it is important to keep the original value for later use.
We now want to get the quarter of the result of last time, but keep that original value:
`dup 4 /`. `dup` duplicates the last value onto the stack. We then can add `4` to the stack and divide the duplicated value by it.<br>
```
// in console:
[276]
# dup 4 /
[276, 69.0]
#
```
As you can see, the result is `69` and the original value is still on the stack!

One last function before letting you try soemthing out in your own: `swap`<br>
As the name implies, `swap` swaps the last two values of the stack. This is importnt for example for the 
order of division or subraction.<br>
```
// in console:
# swap
[69.0, 276]
# /
[0.25]
#
```

---
###### Go to [top](#Structure-Syntax--Builtins).
Take a look at the builtins and try out some calculations to wrap your head around this unusual concept.

Once you have tried out a bit, go [here](program_flow.md) to learn about program flow (if, else, while, functions).

---
### Builtins
###### Go to [top](#Structure-Syntax--Builtins).
These operators work exactly like in python, for example: `a b + -> a + b`

`% & * ** + - / < << <= = > >= >> ^ | ~`

Special operators:<br>
`!` not operator, inverts `true`/`false`<br>
`@` [function/variable pointer](variables_modules.md#function-and-variable-pointers)

| function  | description |
| --------- | --------- |
| clear     | clears stack |
| collect   | a, b, c, ..., len -> [a, b, c, ...] |
| expand    | [a, b, c, ...] -> a, b, c, ..., len |
| drop      | drops last value off stack |
| dump      | appends a string representation of itself to the stack |
| dup       | a -> a, a |
| exit      | a -> exit(a) |
| import    | imports [module](variables_modules.md#Modules) |
| in        | a -> input(a) |
| index     | a, i -> a[i] (works for array/str) |
| len       | a -> len(a) |
| out       | a -> print(a, end='') |
| outln     | a -> print(a) |
| pull      | n -> pulls the nth element onto the top of the stack |
| push      | a, n -> pushes a n places into the stack |
| rem       | n -> drops the last n elements |
| sqrt      | a -> sqrt(a) |
| stacklen  | length of stack |
| sth       | a, b, c -> c, a, b |
| swap      | a, b -> b, a |
| trace     | adds a function trace string onto the stack |
| int       | a -> (int)a  (works for: int, float, bool) |
| inch      | single character input. Does not wait for <kbd>Enter</kbd> to be pressed |

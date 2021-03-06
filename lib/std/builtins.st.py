from interpreter import Builtin, to_str, Import, lenlist


def call_ref(interpreter, v):
    try:
        v.call(interpreter)
    except AttributeError:
        raise TypeError(f'"{v}" is not a reference')


_list = list


def _find_getch():
    try:
        import termios
    except ImportError:
        # Non-POSIX. Return msvcrt's (Windows') getch.
        import msvcrt
        return msvcrt.getch

    # POSIX system. Create and return a getch that manipulates the tty.
    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    return _getch


getch = _find_getch()


def fint(v: float):
    assert isinstance(v, (float, int, bool)), '"int" expects number or bool'
    return int(v)


def export():
    values = {
        'clear': Builtin('clear', 0, lambda interpreter: interpreter.stack.clear()),
        'dump': Builtin('dump', 0, lambda interpreter: interpreter.stack.append(f'[{", ".join(to_str(v, repr_=True) for v in interpreter.stack)}]')),
        'trace': Builtin('trace', 0, lambda interpreter: interpreter.stack.append(interpreter.trace())),
        'stacklen': Builtin('stacklen', 0, lambda interpreter: interpreter.stack.append(len(interpreter.stack))),
        # CHARACTER IN DOES NOT WORK IN PYCHARM IDE!! ONLY WORKS IN NORMAL CMD!!!
        'inch': Builtin('inch', 0, lambda interpreter: interpreter.stack.append(getch())),

        '~': Builtin('~', 1, lambda interpreter, v: interpreter.stack.append(~v)),
        '!': Builtin('!', 1, lambda interpreter, v: interpreter.stack.append(True if v == 0 else False)),
        '@': Builtin('@', 1, lambda interpreter, v: call_ref(interpreter, v)),
        'out': Builtin('out', 1, lambda interpreter, v: print(to_str(v), end='')),
        'outln': Builtin('outln', 1, lambda interpreter, v: print(v)),
        'in': Builtin('in', 1, lambda interpreter, v: interpreter.stack.append(input(v))),
        'exit': Builtin('exit', 1, lambda interpreter, v: exit(v)),
        'sqrt': Builtin('in', 1, lambda interpreter, v: interpreter.stack.append(input(v))),
        'int': Builtin('int', 1, lambda interpreter, v: interpreter.stack.append(fint(v))),
        'dup': Builtin('dup', 1, lambda interpreter, v: interpreter.stack.extend((v, v))),
        'rem': Builtin('rem', 1, lambda interpreter, v: [interpreter.stack.pop() for _ in range(v)]),
        'pull': Builtin('pull', 1, lambda interpreter, v: interpreter.stack.append(interpreter.stack.pop(-v))),
        'import': Import('import'),
        'expand': Builtin('expand', 1, lambda interpreter, v: interpreter.stack.extend(lenlist(v))),
        'collect': Builtin('collect', 1, lambda interpreter, v: interpreter.stack.append(interpreter.pop_stack(v))),
        'len': Builtin('len', 1, lambda interpreter, v: interpreter.stack.append(len(v))),
        'index': Builtin('index', 2, lambda interpreter, a, b: interpreter.stack.append(a[b])),  # array/str(a) index(b)
        'drop': Builtin('drop', 1, lambda interpreter, v: ()),

        '+': Builtin('+', 2, lambda interpreter, a, b: interpreter.stack.append(a + b)),
        '-': Builtin('-', 2, lambda interpreter, a, b: interpreter.stack.append(a - b)),
        '*': Builtin('*', 2, lambda interpreter, a, b: interpreter.stack.append(a * b)),
        '/': Builtin('/', 2, lambda interpreter, a, b: interpreter.stack.append(a / b)),
        '**': Builtin('**', 2, lambda interpreter, a, b: interpreter.stack.append(a ** b)),
        '%': Builtin('%', 2, lambda interpreter, a, b: interpreter.stack.append(a % b)),
        '|': Builtin('|', 2, lambda interpreter, a, b: interpreter.stack.append(a | b)),
        '^': Builtin('^', 2, lambda interpreter, a, b: interpreter.stack.append(a ^ b)),
        '&': Builtin('&', 2, lambda interpreter, a, b: interpreter.stack.append(a & b)),
        '>>': Builtin('>>', 2, lambda interpreter, a, b: interpreter.stack.append(a >> b)),
        '<<': Builtin('<<', 2, lambda interpreter, a, b: interpreter.stack.append(a << b)),
        '=': Builtin('=', 2, lambda interpreter, a, b: interpreter.stack.append(a == b)),
        '>': Builtin('>', 2, lambda interpreter, a, b: interpreter.stack.append(a > b)),
        '<': Builtin('<', 2, lambda interpreter, a, b: interpreter.stack.append(a < b)),
        '>=': Builtin('>=', 2, lambda interpreter, a, b: interpreter.stack.append(a >= b)),
        '<=': Builtin('<=', 2, lambda interpreter, a, b: interpreter.stack.append(a <= b)),
        'swap': Builtin('swap', 2, lambda interpreter, a, b: interpreter.stack.extend((b, a))),
        'push': Builtin('push', 2, lambda interpreter, a, b: interpreter.stack.insert(-b, a)),  # obj(a) dest (b)

        'sth': Builtin('sth', 3, lambda interpreter, a, b, c: interpreter.stack.extend((c, a, b))),  # a b c -> c b a
    }
    return values

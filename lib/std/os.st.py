import sys

import os
from ctypes import windll, c_short

from _ctypes import Structure

from interpreter import Builtin, get_type, parse_value, to_str, Variable, lenlist

def set_cmd_cur_pos(x, y):
    STD_OUTPUT_HANDLE = -11

    class COORD(Structure):
        pass

    COORD._fields_ = [("X", c_short), ("Y", c_short)]


    h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(x, y))

def export(): # TODO: stat calls (~2-3), waitstatus to exitcode, get_handle_Inheritable, scandir, walk, _walk, fdopen add_dll_directory _fspath
    values = {
        'sysargv': Builtin('sysargv', 0, lambda interpreter: interpreter.stack.append(sys.argv)),
        'recursionlimit': Builtin('recursionlimit', 0, lambda interpreter: interpreter.stack.append(sys.getrecursionlimit())),

        'getcwd': Builtin('getcwd', 0, lambda interpreter: interpreter.stack.append(os.getcwd())),
        'getpid': Builtin('getpid', 0, lambda interpreter: interpreter.stack.append(os.getpid())),
        'getppid': Builtin('getppid', 0, lambda interpreter: interpreter.stack.append(os.getppid())),
        'getlogin': Builtin('getlogin', 0, lambda interpreter: interpreter.stack.append(os.getlogin())),
        'get_terminal_size': Builtin('get_terminal_size', 0, lambda interpreter: interpreter.stack.append([*os.get_terminal_size()])), # fixed size 2: x, y
        'cpu_count': Builtin('cpu_count', 0, lambda interpreter: interpreter.stack.append(os.cpu_count())),
        'get_exec_path': Builtin('get_exec_path', 0, lambda interpreter: interpreter.stack.append(os.get_exec_path())),
        'times': Builtin('times', 0, lambda interpreter: interpreter.stack.append([*os.times()])),  # fixed size 4

        'stat': Builtin('stat', 1, lambda interpreter, v: interpreter.stack.append([*os.stat(v)])),  # st_mode, st_ino, st_dev, st_nlink, st_uid, st_gid, st_size, st_atime, st_mtime, st_ctime
        'listdir': Builtin('listdir', 1, lambda interpreter, v: interpreter.stack.append(os.listdir(v))),
        'access': Builtin('access', 2, lambda interpreter, a, b: interpreter.stack.append(os.access(a, b))),
        'chdir': Builtin('chdir', 1, lambda interpreter, v: os.chdir(v)),
        'chmod': Builtin('chmod', 2, lambda interpreter, a, b: os.chmod(a, b)),
        'cmdcurpos': Builtin('cmdcurpos', 2, lambda interpreter, a, b: set_cmd_cur_pos(a, b)),
        'link': Builtin('link', 2, lambda interpreter, a, b: os.link(a, b)),
        'mkdir': Builtin('mkdir', 2, lambda interpreter, a, b: os.mkdir(a, b)),
        'readlink': Builtin('readlink', 1, lambda interpreter, v: interpreter.stack.append(str(os.readlink(v)))),
        'rename': Builtin('rename', 2, lambda interpreter, a, b: os.rename(a, b)),
        'replace': Builtin('replace', 2, lambda interpreter, a, b: os.replace(a, b)),
        'rmdir': Builtin('rmdir', 1, lambda interpreter, v: os.rmdir(v)),
        'symlink': Builtin('symlink', 3, lambda interpreter, a, b, c: os.symlink(a, b, c)),
        'system': Builtin('system', 1, lambda interpreter, v: interpreter.stack.append(os.system(v))),
        'umask': Builtin('umask', 1, lambda interpreter, v: interpreter.stack.append(os.umask(v))),
        'unlink': Builtin('unlink', 1, lambda interpreter, v: os.unlink(v)),
        'remove': Builtin('remove', 1, lambda interpreter, v: os.remove(v)),
        'utime': Builtin('utime', 3, lambda interpreter, a, b, c: os.utime(a, (b, c))),
        'execv': Builtin('execv', 2, lambda interpreter, a, b: os.execv(a, b)),
        'spawnv': Builtin('spawnv', 3, lambda interpreter, a, b, c: interpreter.stack.append(os.spawnv(a, b, c))),
        'kill': Builtin('kill', 2, lambda interpreter, a, b: os.kill(a, b)),
        'openfile': Builtin('openfile', 1, lambda interpreter, v: os.startfile(v)),
        'startfile': Builtin('startfile', 2, lambda interpreter, a, b: os.startfile(a, b)),
        'waitpid': Builtin('waitpid', 2, lambda interpreter, a, b: interpreter.stack.append([*os.waitpid(a, b)])),  # returns two values
        'open': Builtin('open', 2, lambda interpreter, a, b: interpreter.stack.append(os.open(a, b))),
        'close': Builtin('close', 1, lambda interpreter, v: os.close(v)),
        'closerange': Builtin('closerange', 2, lambda interpreter, a, b: os.closerange(a, b)),
        'device_encoding': Builtin('device_encoding', 1, lambda interpreter, v: interpreter.stack.append(os.device_encoding(v))),
        'dup': Builtin('dup', 1, lambda interpreter, v:  interpreter.stack.append(os.dup(v))),
        'lseek': Builtin('lseek', 3, lambda interpreter, a, b, c: interpreter.stack.append(os.lseek(a, b, c))),
        'read': Builtin('read', 2, lambda interpreter, a, b: interpreter.stack.append(os.read(a, b))),
        'write': Builtin('write', 2, lambda interpreter, a, b: interpreter.stack.append(os.write(a, bytes(b)))),
        'isatty': Builtin('isatty', 1, lambda interpreter, v: interpreter.stack.append(os.isatty(v))),
        'pipe': Builtin('pipe', 0, lambda interpreter: interpreter.stack.append([*os.pipe()])),  # returns two values
        'ftruncate': Builtin('ftruncate', 2, lambda interpreter, a, b: os.ftruncate(a, b)),
        'truncate': Builtin('truncate', 2, lambda interpreter, a, b: os.truncate(a, b)),
        'putenv': Builtin('putenv', 2, lambda interpreter, a, b: os.putenv(a, b)),
        'unsetenv': Builtin('unsetenv', 1, lambda interpreter, v: os.unsetenv(v)),
        'strerror': Builtin('strerror', 1, lambda interpreter, v: interpreter.stack.append(os.strerror(v))),
        'fsync': Builtin('fsync', 1, lambda interpreter, v: os.fsync(1)),
        'abort': Builtin('abort', 0, lambda interpreter: os.abort()),
        'urandom': Builtin('urandom', 1, lambda interpreter, v: interpreter.stack.append([*os.urandom(v)])), # returns same length as input
        'get_inheritable': Builtin('get_inheritable', 1, lambda interpreter, v: interpreter.stack.append(os.get_inheritable(v))),
        'set_inheritable': Builtin('set_inheritable', 2, lambda interpreter, a, b: os.set_inheritable(a, b)),
        'fspath': Builtin('fspath', 1, lambda interpreter, v: interpreter.stack.append(str(os.fspath(v)))),
        '_exit': Builtin('_exit', 1, lambda interpreter, v: os._exit(v)),
        'makedirs': Builtin('makedirs', 3, lambda interpreter, a, b, c: os.makedirs(a, b, c)),
        'removedirs': Builtin('removedirs', 1, lambda interpreter, v: os.removedirs(v)),
        'renames': Builtin('renames', 2, lambda interpreter, a, b: os.renames(a, b)),
        'execl': Builtin('execl', 3, lambda interpreter, a, b, c: os.execl(a, b, *c)),
        'execvp': Builtin('execvp', 2, lambda interpreter, a, b: os.execvp(a, b)),
        'getenv': Builtin('getenv', 1, lambda interpreter, v: interpreter.stack.append(os.getenv(v))),
        'fsencode': Builtin('fsencode', 1, lambda interpreter, v: interpreter.stack.append(os.fsencode(v))),
        'fsdecode': Builtin('fsdecode', 1, lambda interpreter, v: interpreter.stack.append(os.fsdecode(v))),
        'spawnl': Builtin('spawnl', 4, lambda interpreter, a, b, c, d: interpreter.stack.append(os.spawnl(a, b, c, *d))),
        'popen': Builtin('popen', 3, lambda interpreter, a, b, c: os.popen(a, b, c)),  # TODO: return? important? yes/no? prolly not?

        'name': Variable('name', os.name),
        'linesep': Variable('linesep', os.linesep),
        'F_OK': Variable('F_OK', os.F_OK),
        'R_OK': Variable('R_OK', os.R_OK),
        'W_OK': Variable('W_OK', os.W_OK),
        'X_OK': Variable('X_OK', os.X_OK),
        'TMP_MAX': Variable('TMP_MAX', os.TMP_MAX),
        'O_RDONLY': Variable('O_RDONLY', os.O_RDONLY),
        'O_WRONLY': Variable('O_WRONLY', os.O_WRONLY),
        'O_RDWR': Variable('O_RDWR', os.O_RDWR),
        'O_APPEND': Variable('O_APPEND', os.O_APPEND),
        'O_CREAT': Variable('O_CREAT', os.O_CREAT),
        'O_EXCL': Variable('O_EXCL', os.O_EXCL),
        'O_TRUNC': Variable('O_TRUNC', os.O_TRUNC),
        'O_BINARY': Variable('O_BINARY', os.O_BINARY),
        'O_TEXT': Variable('O_TEXT', os.O_TEXT),
        'O_NOINHERIT': Variable('O_NOINHERIT', os.O_NOINHERIT),
        'O_SHORT_LIVED': Variable('O_SHORT_LIVED', os.O_SHORT_LIVED),
        'O_TEMPORARY': Variable('O_TEMPORARY', os.O_TEMPORARY),
        'O_RANDOM': Variable('O_RANDOM', os.O_RANDOM),
        'O_SEQUENTIAL': Variable('O_SEQUENTIAL', os.O_SEQUENTIAL),
        'P_WAIT': Variable('P_WAIT', os.P_WAIT),
        'P_NOWAIT': Variable('P_NOWAIT', os.P_NOWAIT),
        'P_NOWAITO': Variable('P_NOWAITO', os.P_NOWAITO),
        'P_OVERLAY': Variable('P_OVERLAY', os.P_OVERLAY),
        'P_DETACH': Variable('P_DETACH', os.P_DETACH),
        'curdir': Variable('curdir', os.curdir),
        'pardir': Variable('pardir', os.pardir),
        'sep': Variable('sep', os.sep),
        'pathsep': Variable('pathsep', os.pathsep),
        'defpath': Variable('defpath', os.defpath),
        'extsep': Variable('extsep', os.extsep),
        'altsep': Variable('altsep', os.altsep),
        'devnull': Variable('devnull', os.devnull),
        'SEEK_SET': Variable('SEEK_SET', os.SEEK_SET),
        'SEEK_CUR': Variable('SEEK_CUR', os.SEEK_CUR),
        'SEEK_END': Variable('SEEK_END', os.SEEK_END),
        'supports_bytes_environ': Variable('supports_bytes_environ', os.supports_bytes_environ)
    }
    return values

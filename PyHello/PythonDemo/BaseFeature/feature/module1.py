
import sys

dir(sys)  # get list of attributes for sys module
ww = 123
print(ww)
['__displayhook__', '__doc__', '__excepthook__', '__name__', '__stderr__',
 '__stdin__', '__stdout__', '_getframe', 'api_version', 'argv',
 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats',
 'copyright', 'displayhook', 'exc_clear', 'exc_info', 'exc_type',
 'excepthook', 'exec_prefix', 'executable', 'exit', 'getcheckinterval',
 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencoding',
 'getrecursionlimit', 'getrefcount', 'hexversion', 'maxint', 'maxunicode',
 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache',
 'platform', 'prefix', 'ps1', 'ps2', 'setcheckinterval', 'setdlopenflags',
 'setprofile', 'setrecursionlimit', 'settrace', 'stderr', 'stdin', 'stdout',
 'version', 'version_info', 'warnoptions']
dir()  # get list of attributes for current module
['__builtins__', '__doc__', '__name__', 'sys']

a = 5  # create a new variable 'a'
dir()
['__builtins__', '__doc__', '__name__', 'a', 'sys']
del a  # delete/remove a name

dir()
['__builtins__', '__doc__', '__name__', 'sys']

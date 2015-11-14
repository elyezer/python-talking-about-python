import inspect

def foo(a, *args, b:int, **kwargs):
    pass

signature = inspect.signature(foo)

print(signature)

# Output:
# (a, *args, b:int, **kwargs)

print(signature.parameters['b'].annotation)

# Output:
# <class 'int'>

for name, parameter in signature.parameters.items():
    print(parameter.kind, ':', name, '=', parameter.default)

# Output:
# POSITIONAL_OR_KEYWORD : a = <class 'inspect._empty'>
# VAR_POSITIONAL : args = <class 'inspect._empty'>
# KEYWORD_ONLY : b = <class 'inspect._empty'>
# VAR_KEYWORD : kwargs = <class 'inspect._empty'>

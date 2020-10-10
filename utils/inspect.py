from inspect import getsource
try:
    from IPython.display import Markdown, display

    def print_code(code):
        display(Markdown(f"```python\n{code}```"))
except ImportError:
    print_code = print


def inspect(object):
    code = getsource(object)
    print_code(code)
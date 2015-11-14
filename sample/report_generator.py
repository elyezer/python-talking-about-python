import argparse
import ast
import io


def title(message, underline='='):
    """Return a string formated as a Markdown title.

    underline argument will be printed on the line below the message.
    """
    return '{}\n{}\n\n'.format(message, underline * len(message))





















def generate_report(file_handler):
    """Generate a report about a test module in Markdown format."""
    tree = ast.parse(file_handler.read())
    with io.StringIO() as output:
        nodes = [
            node for node in ast.walk(tree)
            if isinstance(node, (ast.ClassDef, ast.FunctionDef))
        ]
        for node in nodes:
            separator = '='
            if isinstance(node, ast.FunctionDef):
                separator = '-'
            output.write(title(node.name, separator))
            docstring = ast.get_docstring(node)
            if docstring:
                output.write('{}\n\n'.format(docstring))
            else:
                output.write('No docstring provided.\n')
        return output.getvalue()





















def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'test_path',
        help='path to the test module',
        type=argparse.FileType()
    )
    args = parser.parse_args()
    print(generate_report(args.test_path), end='')

if __name__ == "__main__":
    main()

import os


def get_js_files(directory):
    js_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.js'):
                js_files.append(os.path.join(root, file))
    return js_files


def make_import_tags(files):
    tag_template = "<script src='i%SRC%'></script>"
    result = ""
    for file_path in files:
        result += tag_template.replace('i%SRC%', '/' + file_path.replace('\\', '/')) + '\n'
    return result


files = get_js_files('static/scripts/compiled')
html_script_imports = make_import_tags(files)

print(html_script_imports)
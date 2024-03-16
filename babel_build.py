import os


def get_js_files(directory):
    js_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.js'):
                js_files.append(os.path.join(root, file))
    return js_files


def babel_transform(js_files, output_directory):
    os.makedirs(output_directory, exist_ok=True)

    for js_file in js_files:
        output_filename = os.path.splitext(os.path.basename(js_file))[0] + '.js'
        output_filepath = os.path.join(output_directory, output_filename)

        # Run Babel with JSX preset on the JavaScript file using os.system
        os.system(f'babel {js_file} --out-file {output_filepath} --presets=@babel/preset-react')

        print(f'File {js_file} transformed with Babel and saved as {output_filepath}.')


# Specify the directories for input and output files
js_directory = 'static\\scripts'
output_directory = 'static\\scripts\\compiled'

js_files = get_js_files(js_directory)
babel_transform(js_files, output_directory)
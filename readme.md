#Simple Python, React Env run in browser

### (use Node.js only for bundle babel js files for production build )

You **don't need** to use Node.js for run app

### (use Python Flask for making server)

## Documentation:

This project use flask library, So you need to install python flask with this command:

```shell
pip install flask
```

Next we should install @babel/preset-react node js package (for production build only, you can run project without this)
with this command:

```shell
npm install
```

npm will automatically install this package

You can now run app.py file with python. when you run this file flask server started and you can
go to http://localhost and see the index.html template

In index.html, babel, react and our javascript scripts was imported
We can edit and add scripts in static/scripts

For example, We have an index.js and App.js. in index.js we imported the app component from App.js and render it on
div#root

`NOTE: We cannot use import and require for import components from other files becuse the require is only in node.js.
When we want to access to other files, we import it with a <script> tag in index.html with type="text/babel""`

I think we can also use class components (if we want state) because `useState()` is not available here.

## babel_build.py and js_import_maker.py: Production build

They are two tool for make work easier.
With `babel_build.py` we can make all script folder's javascript files, pure js. They made in static/scripts/compiled,
and we don't need to babel to run they.

When build completed, We need import all static/scripts/compiled into our html.
The `js_import_maker.py` make the tags for import **all compiled files** that we make it with `babel_build.py`

## Notes

It is not a suitable development environment for almost any medium project and is only for learning. It is hoped that by
developing this it can be used. Changes and suggestions are welcome

if you enjoy, please follow me on github
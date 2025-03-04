### [Guitar Tab Editor](https://github.com/calesce/tab-editor)

![](https://img.shields.io/github/license/calesce/tab-editor) [![](https://img.shields.io/github/last-commit/scillidan/tab-editor/master?label=last%20commit%20(fork))](https://github.com/scillidan/tab-editor) ![](https://img.shields.io/badge/GitHub%20Pages-121013?logo=github&logoColor=white)

````{tab} From source
```sh
git clone --depth=1 https://github.com/calesce/tab-editor
cd tab-editor
npm install
npm start
```
````

If you need to change port, edit `server.js`:

```js
app.listen(4321, 'localhost', function(err) {
  if (err) {
    return console.log(err);
  }

  console.log('Listening at http://localhost:4321');
});
```
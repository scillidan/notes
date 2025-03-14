### [BallonsTranslator](https://github.com/dmMaze/BallonsTranslator)

````{tab} From source
```sh
git clone --depth=1 https://github.com/dmMaze/BallonsTranslator
cd BallonsTranslator
uv venv
.venv\Scripts\activate.bat
uv python install 
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
uv pip install -r requirements.txt
python launch.py
```
````

#### Menu setting

```
- BallonsTranslator → Setting
	- DL Module → Translator
	- General → Typesetting → Auto layout (Off)
```
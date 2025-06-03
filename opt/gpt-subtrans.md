### [GPT-Subtrans](https://github.com/machinewrapped/gpt-subtrans)

![](https://img.shields.io/github/license/machinewrapped/gpt-subtrans?style=flat-square)

````{tab} From source
```sh
git clone --depth=1 https://github.com/machinewrapped/gpt-subtrans
uv venv
.venv\Scripts\activate.bat
uv pip install -r requirements.txt
scripts\generate-cmd.bat gui-subtrans
scripts\generate-cmd.bat llm-subtrans
gui-subtrans
```
````

#### Setting

- Settings → Processing
	- Preprocess Subtitles (On)
	- Postprocess Translation (On)
	- Save Preprocessed Subtitles (On)

#### Usage

- Open file → Select `<subtitle>` → Project Settings → Entry `Movie Name`, `Target Language` → Start
### [GPT-Subtrans](https://github.com/machinewrapped/gpt-subtrans)

```sh
git clone --depth=1 https://github.com/machinewrapped/gpt-subtrans
uv venv
.venv\Scripts\activate.bat
uv pip install -r requirements.txt
scripts\generate-cmd.bat gui-subtrans
scripts\generate-cmd.bat llm-subtrans
```

With GUI:

```sh
gui-subtrans
```

Settings → Processing:

```
Preprocess Subtitles (On)
Postprocess Translation (On)
Save Preprocessed Subtitles (On)
```

Open file → Select `<subtitle>` → Project Settings → Entry `Movie Name`, `Target Language` → Start
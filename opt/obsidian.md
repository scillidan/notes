### [Obsidian](https://obsidian.md/)

#### Resource

##### [Kokoro TTS Plugin for Obsidian](https://github.com/Mithadon/obsidian-kokoro-tts-plugin#manual-installation) [^1]

```sh
cd <your_vault>/.obsidian/plugins
mkdir kokoro-tts
cd kokoro-tts
```

Get files from [Releases](https://github.com/Mithadon/obsidian-kokoro-tts-plugin/releases):

```
main.js
manifest.json
styles.css
kokoro_backend.py
requirements.txt
```

```sh
conda create -n kokoro-tts python=3.10
conda activate kokoro-tts
pip install torch==2.5.1 torchvision==0.20.1 --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt
```

Get `kokoro-v0_19.pth` from [here](https://huggingface.co/hexgrad/kLegacy/tree/main/v0.19).
...

#### Reference

- [Embed files](https://help.obsidian.md/embeds)
- [Aliases](https://help.obsidian.md/aliases)

[^1]: [https://github.com/Mithadon/obsidian-kokoro-tts-plugin#manual-installation](https://github.com/Mithadon/obsidian-kokoro-tts-plugin#manual-installation)
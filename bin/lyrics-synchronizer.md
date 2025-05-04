### [Sync Lyrics and Produce an LRC file using spleeter, whisper, and text similarity.](https://github.com/feliks720/Lyrics-synchronizer)

````{tab} Conda
```sh
conda create --name lyrics python=3.10.12
conda activate lyrics
pip install spleeter openai-whisper
python pysync <music> <lyric>
```
````
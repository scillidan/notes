# [Sync Lyrics and Produce an LRC file using spleeter, whisper, and text similarity.](https://github.com/feliks720/Lyrics-synchronizer) (Cache)

````{tab} Conda
```sh
conda create --name lyrics python=3.10.12
conda activate lyrics
pip install spleeter openai-whisper
pip uninstall numpy
pip install numpy==1.26.4
python pysync sample.mp3 sample.txt
python pysync <music> <lyric>
```
````
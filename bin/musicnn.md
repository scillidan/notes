# [musicnn](https://github.com/jordipons/musicnn)

```sh
git clone --depth=1 https://github.com/jordipons/musicnn
cd musicnn
```

````{tab} Windows 10
```sh
subl requirements.txt
```

```
audioread==3.0.1
librosa==0.8.1
musicnn==0.1.0
numpy==1.16.6
pandas==1.1.5
scikit-learn==0.24.2
scipy==1.5.4
soundfile==0.12.1
tensorflow==2.3.4
resampy==0.2.2
ipython==7.16.3
```

```sh
conda create --name musicnn python=3.6.13
conda activate musicnn
pip install -r requirements.txt
pip install matplotlib
conda install  ipykernel jupyterlab
python -m ipykernel install --user --name musicnn
jupter lab
```
````

````{tab} Arch [^1] (Cache)
```sh
uv python install 3.7.9
uv venv --python 3.7.9
source .venv\Scripts\activate.bat
uv pip install -e .
uv pip install matplotlib
yay -S libxcrypt-compat
uv run --with jupyter jupyter lab
```
````

[^1]: [Using uv with Jupyter](https://docs.astral.sh/uv/guides/integration/jupyter/)
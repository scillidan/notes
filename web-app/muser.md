### [Muser](https://github.com/jonshamir/muser)

![](https://img.shields.io/github/license/jonshamir/muser)<br \>
![](https://img.shields.io/badge/GitHub%20Pages-121013?logo=github&logoColor=white)

```sh
git clone --depth=1 https://github.com/jonshamir/muser
cd muser
```

Create `requirements.txt`:

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
conda create --name muser python=3.6.13
conda activate muser
pip install -r requirements.txt
pip install matplotlib
```

Edit `tools/tagger.py`, `playlist-creator.py`:

```py
# %matplotlib inline
```

```sh
python tools/tagger.py
pip install eyed3
python tools/playlist-creator.py
```

```sh
npm install
npm install --save-dev cross-env
npm run start
# set NODE_ENV=development && node tools/bundler.js
```

#### Reference

- [batch_muser_tagger.py](https://gist.github.com/scillidan/92b36835451da63a247e287e6753ea5c)

[^1]: [Instruction how to install the package to solve dependency issues](https://github.com/jordipons/musicnn/issues/28)
[^2]: [Install TensorFlow with pip](https://www.tensorflow.org/install/pip)
[^3]: [Python pip 清华安装源被封禁下载](https://rewrz.com/archive/tsinghua-pip-source-blocked-requests)
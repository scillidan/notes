### [Anaconda](https://www.anaconda.com/) [^1]

```sh
subl ~/.condarc
```

```
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.ustc.edu.cn/anaconda/pkgs/main
  - https://mirrors.ustc.edu.cn/anaconda/pkgs/r
  - https://mirrors.ustc.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.ustc.edu.cn/anaconda/cloud
  bioconda: https://mirrors.ustc.edu.cn/anaconda/cloud
```

```sh
conda clean -i
```

[^1]: [USTC Mirror Help - Anaconda](https://mirrors.ustc.edu.cn/help/anaconda.html)
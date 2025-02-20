### [RapidVideOCR](https://github.com/SWHL/RapidVideOCR)

1. Get `VideoSubFinder` form [SourceForge](https://sourceforge.net/projects/videosubfinder/).
2. Decompress `VideoSubFinder_*.zip` to `VideoSubFinder`.
3. Run `VideoSubFinderWXW.exe`.
4. Settings → Parameters Influencing Image Processing (Optional):
  ```
  FFMPEG Video Devices `cuda`
  Use CUDA GPU Acceleration `On`
  ```
5. File → Open Video
6. Run Search → When shows subtitle, Stop Search → Modify the ScanBox
7. Begin Time → `00:00:00:000` → Run Search
8. Output will be on `.\RGBImages\` 

Power by CPU [^1]:

```sh
pip install rapid_videocr
rapid_videocr -o srt -i <rgb_images_dir> -s _output
```

Power by GPU [^2][^3]:

```sh
git clone --depth=1 https://github.com/SWHL/RapidVideOCR
uv venv
.venv\Scripts\activate.bat
uv pip install paddlepaddle-gpu==3.0.0b1 -i https://www.paddlepaddle.org.cn/packages/stable/cu123/
uv pip install get-pypi-latest-version
python setup.py install
# pip uninstall onnxruntime
# pip install onnxruntime-directml
uv pip install rapidocr_paddle
rapid_videocr --use_cuda -o srt -i <rgb_images_dir> -s _output
```

[^1]: [RapidVideOCR - 高级教程](https://swhl.github.io/RapidVideOCR/docs/tutorial/senior/)
[^2]: [飞桨 - 快速安装](https://www.paddlepaddle.org.cn/install/quick)
[^3]: [rapidocr_paddle - 安装及使用](https://rapidai.github.io/RapidOCRDocs/install_usage/rapidocr_paddle/usage/)
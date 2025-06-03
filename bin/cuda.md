### [CUDA](https://developer.nvidia.com/cuda-toolkit)

#### Requirement

1. Have a GPU. Check [Your GPU Compute Capability](https://developer.nvidia.com/cuda-gpus).  
2. Install `python 3.10` from [Python Releases for Windows](https://www.python.org/downloads/windows/). I test on `3.10.11`.
3. Install `CUDA` from [CUDA Toolkit - Downloads](https://developer.nvidia.com/cuda-downloads). I used `CUDA 12.1.0`.
4. Check [PyTorch - Start Locally](https://pytorch.org/get-started/locally/) to install `torch``.

Check:

```
python --version
nvcc -V
echo %CUDA_PATH%
# echo %CUDA_PATH_V12_1%
```
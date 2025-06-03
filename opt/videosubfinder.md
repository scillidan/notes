### [VideoSubFinder](https://sourceforge.net/projects/videosubfinder/)

1. Get `VideoSubFinder` form [SourceForge](https://sourceforge.net/projects/videosubfinder/)
2. Decompress `VideoSubFinder_*.zip` to `VideoSubFinder`
3. Run `VideoSubFinderWXW.exe`
4. Settings → Parameters Influencing Image Processing (Optional):
  ```
  FFMPEG Video Devices `cuda`
  Use CUDA GPU Acceleration `On`
  ```
5. File → Open Video
6. Run Search → When shows subtitle, Stop Search → Modify the ScanBox
7. Begin Time → `00:00:00:000` → Run Search
8. Output will be on `.\RGBImages\`

#### Cross-reference

- [videosubfinder.md](https://scillidan.github.io/notes/bin/rapidvideocr.html)
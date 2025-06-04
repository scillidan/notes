# [Renpy](https://www.renpy.org/)

## Build Distributions

1. Download `SDK.zip` from [Download Ren'Py](https://www.renpy.org/latest.html)
2. Decompress it to `renpy-*-sdk\`
3. Run `renpy-*-sdk\renpy.exe`
4. preferences → General → Projects Directory → `C:\Users\User\Project\renpy` → Return
5. Go to `C:\Users\User\Project\renpy`，`git clone --depth=1 https://codeberg.org/fhs/katawa-shoujo-re-engineered`
6. Renpy → PROJECTS → refresh → Select `katawa-shoujo-re-engineered`
7. Build Distributions → Build

## Build Android (Draft)

1. Renpy → Android → Build
  1. Install SDK
  2. Generate Keys
  3. Build Package
2. 这个步骤会检测环境要求，需要JDK和Gradle
  1. 这里会涉及到Library文件的存放位置。我个人没分CDEF盘，只有C盘，也优先使用软件的便携版，一般就是压缩包。下面步骤就根据你的实际情况做修改
  2. 按照提示下载JDK和Gradle的文件。解压`OpenJDK21U-jdk_x64_windows_hotspot_21.0.4_7.zip`到`C:\Users\User\Lib\jdk-21.04`
  3. 解压`gradle-8.5-bin.zip`到`C:\Users\User\Lib\gradle-8.5`。
  4. Windows设置 → 查看高级系统设置 → 环境变量 → 用户变量 → 选中Path → 编辑 → 新建 → `C:\Users\User\Lib\jdk-21.04\bin` → 再新建 → `C:\Users\User\Lib\gradle-8.5\bin`
  5. 重启`renpy.exe` → Andriod → Build Package
3. 如果在gradle相关的步骤提示`需要下载gradle`，这可能是个bug。可以把`gradle-8.5-bin.zip`放进`C:\Users\User\.gradle\wrapper\dists\gradle-8.5-bin\<一串字符>\`下。重启renpy.exe，再试一次
4. 如果出现未知错误，可尝试关闭梯子。重启renpy.exe再试
# [Everything](https://www.voidtools.com/)

## Setting [^1][^2]

- 选项 → 索引/排除列表 → 启用排除列表 → 添加筛选器
  ```
  .*
  _build
  node_modules
  public
  site
  watch_later*
  *.bak
  *.tmp
  Hiberfil.sys
  Pagefile.sys
  Windows.old
  ```
  - 添加文件夹 → 文件夹
  ```
  C:\$Recycle.Bin
  C:\ProgramData
  C:\SysReset
  C:\System Volume Information
  C:\Users\<username>\AppData\Local\Temp
  C:\Windows
  ```
- 选项 → 常规 → 结果 → 双击路径列打开目录 On
- 索引 → NTFS → 自动... Off → 不搜索的本地磁盘 → 包含到数据库 Off, 启用USN日志 Off

[^1]: [Omit Recycle Bin Files From Search](https://www.voidtools.com/forum/viewtopic.php?t=6454)
[^2]: [Tools Options Exclude "Exclude files" .tmp :: not working ??](https://www.voidtools.com/forum/viewtopic.php?t=11617)

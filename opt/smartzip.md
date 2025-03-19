### [SmartZip](https://github.com/vvyoko/SmartZip)

````{tab} Download
```sh
1. Download `SmartZip*.zip` from [SmartZip - Releases](https://github.com/vvyoko/SmartZip/releases).
2. Decompress it to `SmartZip\`.
```
````

#### Create `light.ico` form `dark.ico`

```sh
magick convert dark.ico -channel RGB -negate light.ico
```

#### Setting

1. SmartZip → 自定义 → 图标路径 → `%SmartZipDir%\light.ico`
2. 关联 → 右键菜单 → Select `SmartZip Decompress`, `SmartZip Compress` → 注册
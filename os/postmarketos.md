### [postmarketOS](https://postmarketos.org/) (Cache)

1. Windows 10 → 计算机管理 → 系统工具 → 设备管理器 → 便携设备 → ONEPLUS A5010
2. 驱动程序 → 更新驱动程序 → 浏览我的电脑以查找驱动程序 → `usb_driver\`

- [Using ADB and fastboot](https://wiki.lineageos.org/adb_fastboot_guide)
- [Get the Google USB Driver](https://developer.android.com/studio/run/win-usb)
- [Install a USB driver](https://developer.android.com/studio/run/oem-usb#InstallingDriver)

1. OnePlus 5 → 设置 → 关于手机 → 版本号 → 点击7下
2. 设置 → 开发者选项 → OEM解锁 → 启用
3. 拔掉USB → 电源键+音量上键 → FastBoot Mode
4. 插上USB → 在PC上运行`fastboot oem unlock`

- [postmarketOS Wiki - OnePlus 5](https://wiki.postmarketos.org/wiki/OnePlus_5_(oneplus-cheeseburger))
- [Enable USB Debugging and OEM Unlock](https://doc.e.foundation/pages/enable-usb-debugging)
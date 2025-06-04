# [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)

## USB host boot mode [^1][^2][^3]

```sh
sudo vim /root/firmware/config.txt
```

```
# at to the end
[all]
program_usb_boot_mode=0
otg_mode=1
```

[^1]: [USB host boot mode](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#usb-host-boot-mode)
[^2]: [Boot from USB, if no then SD card](https://raspberrypi.stackexchange.com/questions/91889/boot-from-usb-if-no-then-sd-card)
[^3]: [What's the best filesystem to use for an NVMe SSD?](https://www.reddit.com/r/linux4noobs/comments/lmf8ju/whats_the_best_filesystem_to_use_for_an_nvme_ssd/)
# [ClamAV](https://www.clamav.net/)

```sh
mkdir -p <path_to>\ClamAV\database
subl <path_to>\freshclam.conf
```

```
DatabaseDirectory "<path_to>\ClamAV\database"
```

```sh
freshclam
clamscan -r -i <dir>
clamscan -v -a --max-filesize=1000M --max-scansize=1000M --alert-exceeds-max=yes <file>
```

## Reference

- [在 EC2 Linux 操作系统上部署 ClamAV 并开启实时防护、集中日志采集和统一告警](https://aws.amazon.com/cn/blogs/china/deploy-clamav-on-ec2-with-realtime-scan-and-centralized-alarm/)

## Troubleshoot

- [Clamscan on Windows does not skip large files (>2 GB) and outputs error reports cl_scandesc_callback: Can't fstat descriptor 3 instead](https://github.com/Cisco-Talos/clamav/issues/1315)
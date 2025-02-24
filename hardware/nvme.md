### NVMe

For example:

```sh
sudo mkdir -p /mnt/nvme
ls -l /mnt/nvme
sudo mount -o uid=root,gid=root,umask=000 /dev/sda2 /mnt/nvme
```
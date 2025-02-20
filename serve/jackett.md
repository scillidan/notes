### [Jackett](https://github.com/Jackett/Jackett)

````{tab} Ubuntu ARM [^1]
```sh
sudo apt install mono-devel
```

Get `Jackett.Binaries.LinuxARM64.tar.gz` from [Jackett - Releases](https://github.com/Jackett/Jackett/releases).

```sh
tar -xvzf Jackett.Binaries.LinuxARM64.tar.gz
cd Jackett
./jackett
```

```sh
sudo ./install_service_systemd.sh
```

```sh
sudo systemctl status jackett.service
```
````

[^1]: [How to Install Jackett on Ubuntu 20.04](https://varhowto.com/install-jackett-ubuntu-20-04/)
[^2]: [Security Risk: Your instance has external access enabled without using an admin password.](https://github.com/Jackett/Jackett/wiki/Troubleshooting#security-risk-your-instance-has-external-access-enabled-without-using-an-admin-password)

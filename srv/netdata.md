### [Netdata](https://www.netdata.cloud/)

````{tab} Ubuntu 22 ARM [^1]
```sh
sudo apt install netdata -y
sudo vim /etc/netdata/netdata.conf
```

```
[global]
  run as user = netdata
  web files owner = root
  web files group = root
  # Netdata is not designed to be exposed to potentially hostile
  # networks. See https://github.com/netdata/netdata/issues/164
  bind socket to IP = 0.0.0.0
```

```sh
sudo systemctl enable --now netdata
```
````

[^1]: [How to Install Netdata on Ubuntu 22.04](https://wiki.crowncloud.net/?how_to_Install_netdata_monitoring_tool_ubuntu_22_04)
## [Battize](https://bazzite.gg) [^1]

```sh
ujust enable-tailscale
ujust setup-decky ACTION="install"
ujust setup-sunshine
sudo vim /etc/hostname
hostnamectl hostname <hostname>
sudo reboot
```

```sh
sudo tailscale up
```

```pwsh
netsh advfirewall firewall add rule name="GameStream UDP" dir=in protocol=udp localport=48010 action=allow
netsh advfirewall firewall add rule name="GameStream TCP" dir=in protocol=tcp localport=48000,48010 action=allow
```

#### Reference

- [Installing Bazzite for Desktop/Laptop Hardware](https://docs.bazzite.gg/General/Installation_Guide/Installing_Bazzite_for_Desktop_or_Laptop_Hardware/#__tabbed_1_3)

[^1]: [Can I change the hostname of my device?](https://docs.bazzite.gg/General/FAQ/#can-i-change-the-hostname-of-my-device)
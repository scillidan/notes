## [Battize](https://bazzite.gg) (Later)

```sh
ujust enable-tailscale
ujust setup-decky
ujust setup-sunshine
sudo vim /etc/hostname
hostnamectl hostname <hostname>
sudo reboot
```

```pwsh
netsh advfirewall firewall add rule name="GameStream UDP" dir=in protocol=udp localport=48010 action=allow
netsh advfirewall firewall add rule name="GameStream TCP" dir=in protocol=tcp localport=48000,48010 action=allow
```

```sh
sudo tailscale up
```

[^1]: [Can I change the hostname of my device?](https://docs.bazzite.gg/General/FAQ/#can-i-change-the-hostname-of-my-device)
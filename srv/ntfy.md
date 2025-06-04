# [ntfy.sh](https://ntfy.sh/)

````{tab} Ubuntu 24 ARM [^1]
```sh
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://archive.heckel.io/apt/pubkey.txt | sudo gpg --dearmor -o /etc/apt/keyrings/archive.heckel.io.gpg
sudo apt install apt-transport-https
sudo sh -c "echo 'deb [arch=arm64 signed-by=/etc/apt/keyrings/archive.heckel.io.gpg] https://archive.heckel.io/apt debian main' \
    > /etc/apt/sources.list.d/archive.heckel.io.list"
sudo apt update
sudo apt install ntfy
sudo systemctl enable --now ntfy
```
````

[^1]: [Installing ntfy - Debian/Ubuntu repository](https://docs.ntfy.sh/install/#debianubuntu-repository)
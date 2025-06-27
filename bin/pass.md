# [pass](https://www.passwordstore.org/)

````{tab} ArchWSL
```sh
sudo pacman -S pass gnupg
gpg --full-generate-key
```

```sh
pass init <your_email>
pass insert <key_name>
pass show <key_name>
```
````
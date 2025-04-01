### [starfetch](https://github.com/Haruno19/starfetch)

````{tab} ArchWSL
```sh
git clone --depth=1 https://github.com/Haruno19/starfetch
cd starfetch
make -j8
sudo make install
starfetch -r
```
````

````{tab} MSYS2
```sh
git clone --depth=1 https://github.com/K1ngst0m/starfetch
cd starfetch
make
./starfetch.exe -r
```
````

````{tab} Cargo
```sh
git clone --depth=1 https://github.com/CoderCharmander/starfetch
cargo build
C:\Users\User\.cargo\tmp\debug\starfetch.exe
starfetch -d
starfetch -l
starfetch orion
```
````

#### Terminal record

```{eval-rst}
.. asciinema :: NB2yVHswCBwZNlmsphzVcGv20
```

```{eval-rst}
.. asciinema :: 0t3VQXFYqoyiDyCnY8IggZf8B
```
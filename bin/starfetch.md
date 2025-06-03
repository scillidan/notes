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

#### Resource

- [summer_triangle(CoderCharmander_starfetch).json](https://gist.github.com/scillidan/83ba8a592eaed7c8256b6e1984c56809)
- [summer_triangle(Haruno19_starfetch).json](https://gist.github.com/scillidan/773260fba75a1bfc9b203c445d371b55)

#### Terminal record

```{eval-rst}
.. asciinema :: NB2yVHswCBwZNlmsphzVcGv20
```

```{eval-rst}
.. asciinema :: 0t3VQXFYqoyiDyCnY8IggZf8B
```
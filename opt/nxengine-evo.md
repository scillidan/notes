### [NXEngine-evo](https://github.com/nxengine/nxengine-evo)

#### Build local data

```sh
git clone --depth=1 https://github.com/nxengine/translations
cd translations
```

I want to run some steps step by step, so:

````{tab} Arch
```sh
cp build-local.sh build-local.sh.bak
vim build-local.sh
```

```
# wget https://github.com/nxengine/tsc-converter/releases/download/v1.1/tsc.tar.gz
# tar -zxf tsc.tar.gz
# rm -f tsc.tar.gz
# 
# wget https://github.com/nxengine/nx-fontgen/releases/download/v1.3/fontbm.tar.gz
# tar -zxf fontbm.tar.gz
# rm -f fontbm.tar.gz

# rm -f fontbm
# rm -f fontbm.bin
# rm -f tsc
# rm -rf assets
# rm -rf lib
```

```sh
cd local
wget https://github.com/nxengine/tsc-converter/releases/download/v1.1/tsc.tar.gz
tar -zxf tsc.tar.gz
wget https://github.com/nxengine/nx-fontgen/releases/download/v1.3/fontbm.tar.gz
tar -zxf fontbm.tar.gz
mv <font.ttf> assets/
git clone --depth=1 https://github.com/nxengine/lang_chinese lang_chinese
cp lang_chinese/metadata lang_chinese/metadata.bak
vim lang_chinese/metadata
```

Edit `unifont-10.0.06.ttf` to `ark-pixel-12px-proportional-zh_cn.ttf`.

```sh
cd ..
./build-local.sh
```
````

````{tab} Ubuntu 24 ARM
```sh
sudo apt update
sudo apt install build-essential cmake libsdl2-dev libsdl2-ttf-dev libsdl2-mixer-dev libsdl2-image-dev libpng-dev libjpeg-dev
```

```sh
git clone --depth=1 https://github.com/nxengine/tsc-converter
cd tsc-converter
mkdir build
cd build
cmake ..
make
cp ../bin/tsc ~/translations/local/tsc
git clone --depth=1 https://github.com/nxengine/nx-fontgen
```

```sh
git clone --depth=1 https://github.com/nxengine/translations
cd translations
mkdir build
cd build
cmake ..
make #ERROR
```
````

#### Build nxengine-evo [^1]

````{tab} Arch
```sh
git clone --depth=1 https://github.com/nxengine/nxengine-evo
cd nxengine-evo
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release -DPORTABLE=ON ..
make
cd ..
wget https://www.cavestory.org/downloads/cavestoryen.zip
unzip cavestoryen.zip
cp -r ../translations/local/data/lang/chinese/* CaveStory/data/
cp -r CaveStory/Doukutsu.exe CaveStory/data ./
build/nxextract
mkdir desk
cp -r build/nxengine-evo data desk/
desk/nxengine-evo
```
````

[^1]: [Building on Linux](https://github.com/nxengine/nxengine-evo/wiki/Building-on-Linux)
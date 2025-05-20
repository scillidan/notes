### [FlowGram.AI](https://github.com/bytedance/flowgram.ai)

````{tab} From source
```sh
git clone --depth=1 https://github.com/bytedance/flowgram.ai
cd flowgram.ai
nvm install lts
nvm use lts
npm i -g pnpm@9.12.0 @microsoft/rush@5.140.0
rush update
rush build
rush dev:docs
rush dev:demo-fixed-layout
rush dev:demo-free-layout
```
````
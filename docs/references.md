# References

👇 公式ですら、記事がメンテナンスされてない  

* 📖 [PyCUDA Tutorial](https://documen.tician.de/pycuda/tutorial.html)  

👇 ググって１番上に出てくる記事でもエラー出る（前提知識が飛ばされているから）  

* 📖 [PyCUDAを使ってみよう](https://scrapbox.io/PythonOsaka/PyCUDA%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%81%BF%E3%82%88%E3%81%86)  

```shell
pip install -U pycuda
```

👇 「金子邦彦研究室」というところが PyCUDA に詳しいかも  

* 📖 [pycuda のインストール（Windows 上）](https://www.kkaneko.jp/tools/win/pycuda.html)

## PyCUDA やるならビルドツールをインストールしろ

* 📖 [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/ja/visual-cpp-build-tools/)
    * オプションは選択せずに　ビルドツールズ　だけインストールすればいいかも
    * （これは要るか分からない）Visual Studio インストーラーから、 `C++によるデスクトップ開発`、 `v143 ビルドツール用 C++/CLI サポート（最新）` オプションを追加してインストール

### vcvarsall.bat ファイルがほしい

amd用の設定をするのに使う  

Windowsのすべてのアプリから `x64 Native Tools Command Prompt for VS 2022` を実行  

👇 `amd64` を引数に指定して実行できるか？  

```plaintext
# Visual C++ Build Tools を AMD のCPUで使うための設定
"C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvarsall.bat" amd64

# 場所が違うことがある
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" amd64
```

👇 「ビルドツール」インストール完了の確認  

Input:  

```shell
where cl
```

Output:  

```plaintext
les\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.35.32215\bin\Hostx64\x64\cl.exe
```

## NVIDIA CUDA ツールキットのインストール

### Windows のユーザ名が日本語のとき，nvcc がうまく動作しないエラーを回避するための処理

📖 [NVIDIA ドライバ，NVIDIA CUDA ツールキット 11.8，NVIDIA cuDNN v8.8 のインストールと動作確認（Windows 上）](https://www.kkaneko.jp/tools/win/cuda.html)  

ユーザー環境変数 `TEMP` に、 `C:\TEMP` を追加している？？  

```shell
mkdir C:\TEMP
call powershell -command "[System.Environment]::SetEnvironmentVariable(\"TEMP\", \"C:\TEMP\", \"User\")"
```

📖 [CUDA Toolkit 12.1 Update 1 Downloads](https://developer.nvidia.com/cuda-downloads)  

CUDA ツールキットのインストール後、アカウント登録が求められる  

👇 インストール完了の確認  

システム環境変数を確認  

* システム環境変数 `Path`
    * 値: `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1\bin`
    * 値: `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1\libnvvp`
* システム環境変数 `CUDA_PATH`
    * 値: `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1`
* システム環境変数 `CUDA_PATH_V12_1` （※バージョン12.1系列なら）
    * 値: `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1`

👇 これで `PyCUDA` をインストールできるはず  

```shell
pip install -U pycuda
```

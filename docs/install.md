# PyCUDAのインストール

# Step 1. 「Microsoft C++ Build Tools」（いわゆるビルドツールズ）のインストール手順

## Step 1-1. インストーラーのダウンロード

👇 以下のサイトからインストーラーをダウンロードして実行  

📖 [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/ja/visual-cpp-build-tools/)  

## Step 1-2. インストール

Visual Studio Installer のウィンドウが表示されていると思う  

* `ワークロード` タブが開いているはず
* `Microsoft C++ Build Tools` がすでに選ばれている
* （チェックしていなければ）「C++ によるデスクトップ開発」をチェック
* （これは要るか分からない）Visual Studio インストーラーから、 `C++によるデスクトップ開発`、 `v143 ビルドツール用 C++/CLI サポート（最新）` オプションを追加
* インストールする

## Step 1-3. ビルドツールズを有効にするための、環境変数の設定

（ビルドツールズへのビルドパスを通す環境変数は、） **自分で設定してはいけない** （雑多だから）。 用意されている `.bat` ファイルを使う  

Windows 10 なら「すべてのアプリ」から `[Visual Studio 2022] - [x64 Native Tools Command Prompt for VS 2022]` を探して実行  
あるいは、
`.bat` ファイルを直接実行する

例: Visual C++ Build Tools を AMD のCPUで使うための設定  
インストール先が違う可能性に注意  

```shell
# 例１（場所が違うことがある）
"C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvarsall.bat" amd64

# 例２
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" amd64
```

👇 「ビルドツール」インストール完了の確認  

（**cl.exeへのビルドパスが通る**か確認する）  

Input:  

```shell
where cl
```

Output:  

```plaintext
les\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.35.32215\bin\Hostx64\x64\cl.exe
```

# Step 2. 「NVIDIA CUDA ツールキット」のインストール手順

## Step 2-1. （事前処理）Windows のユーザ名が日本語のとき，nvcc がうまく動作しないエラーを回避するために

よく分からないが、以下のコマンドを打鍵する（よくある不具合への回避策らしい）  

```shell
mkdir C:\TEMP
call powershell -command "[System.Environment]::SetEnvironmentVariable(\"TEMP\", \"C:\TEMP\", \"User\")"
```

これで、ユーザー環境変数 `TEMP` に、 `C:\TEMP` が設定される？？  

参考: 📖 [NVIDIA ドライバ，NVIDIA CUDA ツールキット 11.8，NVIDIA cuDNN v8.8 のインストールと動作確認（Windows 上）](https://www.kkaneko.jp/tools/win/cuda.html)  

## Step 2-2. インストール

👇 以下のWebサイトで質問に答えると、最適なインストール方法が示される（のだろう）  

📖 [CUDA Toolkit 12.1 Update 1 Downloads](https://developer.nvidia.com/cuda-downloads)  

👇 インストール完了の確認  

システム環境変数を確認  

* システム環境変数 `Path`
    * 値: `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1\bin`
    * 値: `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1\libnvvp`
* システム環境変数 `CUDA_PATH`
    * 値: `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1`
* システム環境変数 `CUDA_PATH_V12_1` （※バージョン12.1系列なら）
    * 値: `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1`

## Step 2-3. GEFORCE EXPERIENCE へのアカウント登録

CUDA ツールキットのインストール後、アカウント登録が求められる  

# Step 3. 「PyCUDA」のインストール

```shell
pip install -U pycuda
```

次に、 （PyCUDA パッケージが正しくインストールされたかを確認するために）Pythonスクリプトを実行したい  

👇 もし、Python インタープリターを、Anaconda の仮想環境に切り替えたいなら、コマンド・プロンプトで以下を打鍵    

```shell
%windir%\system32\cmd.exe "/K" %USERPROFILE%\Anaconda3\Scripts\activate.bat %USERPROFILE%\Anaconda3
```

👇 Pythonスクリプトの実行  

Input:  

```shell
python hello_gpu.py
```

Output:  

```plaintext
C:\GitHub\pycuda-practice\hello_gpu.py:14: UserWarning: The CUDA compiler succeeded, but said the following:
kernel.cu

  mod = SourceModule("""
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
```

# 参考にした記事

* 📖 [PyCUDA Install](https://documen.tician.de/pycuda/install.html) - 肝心の公式なのに、記事がメンテナンスされてない
* 📖 [pycuda のインストール（Windows 上）](https://www.kkaneko.jp/tools/win/pycuda.html) - この「金子邦彦研究室」の記事がよい。ここでしか、まともなインストール記事を見つけられなかった
* 📖 [PyCUDAを使ってみよう](https://scrapbox.io/PythonOsaka/PyCUDA%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%81%BF%E3%82%88%E3%81%86) - インストールが終わったあとに読む記事

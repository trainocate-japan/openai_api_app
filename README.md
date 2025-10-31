# 生成AIアプリ開発入門 ～OpenAI API活用～

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/trainocate-japan/OpenAIAPIApp_Lecture_github/blob/main/OpenAIAPIApp_Lecture_github/Google%20Colaboratoryを使ってみよう.ipynb)

---

## 概要
このリポジトリは、**OpenAI API** を活用した講義・学習用教材です。  
Google Colab 上で動作する Jupyter Notebook を通して、以下のトピックを実践的に学ぶことができます。

- 文章生成（Chat Completion）
- 画像生成 (Image Generation)  
- 音声合成 (Text-to-Speech)  
- テキスト埋め込み (Embeddings)  


## 使用方法

### 1 Colabで開く
上部の **「Open in Colab」バッジ** をクリックして、`Google Colaboratoryを使ってみよう.ipynb` を開きます。

### 2️ APIキー設定
ノートブック内で以下を実行してOpenAI APIキーを設定します：
```python
import os
os.environ["OPENAI_API_KEY"] = "sk-xxxxx..."
```

### 3️ 各章のノートブックを実行

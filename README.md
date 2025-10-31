# 📘 OpenAI API Lecture Materials

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Trainocate-f/OpenAIAPIApp_Lecture_github/blob/main/OpenAIAPIApp_Lecture_github/Google%20Colaboratoryを使ってみよう.ipynb)

---

## 🧠 概要
このリポジトリは、**OpenAI API** を活用した講義・学習用教材です。  
Google Colab 上で動作する Jupyter Notebook を通して、以下のトピックを実践的に学ぶことができます。

- ChatGPTによる会話生成  
- 画像生成 (Image Generation)  
- 音声合成 (Text-to-Speech)  
- テキスト埋め込み (Embeddings)  
- 連続的な対話アプリケーションの実装  

---

## 📂 ディレクトリ構成

```
OpenAIAPIApp_Lecture_github/
├── OpenAIAPIApp_Lecture_github/
│   ├── add_colab_badge.py
│   ├── Google Colaboratoryを使ってみよう.ipynb
│   ├── chapter2/
│   │   ├── 第2章 Chat Completions.ipynb
│   │   └── 第2章 (オプション) 連続した対話機能の実装.ipynb
│   ├── chapter3/
│   │   ├── 第3章 Text-to-speech.ipynb
│   │   └── 第3章 画像生成.ipynb
│   ├── chapter4/
│   │   └── 第4章 Embedding.ipynb
│   ├── data/
│   │   └── 走れメロス(青空文庫).txt
│   └── utils/
│       └── embeddings_utils.py
```

---

## 🚀 実行環境

本教材は **Google Colaboratory** 上での実行を推奨します。

### 🔧 必要条件
- Google アカウント  
- OpenAI APIキー  
- Python 3.10 以上  
- 以下の主要ライブラリ：
  ```
  openai
  numpy
  pandas
  matplotlib
  requests
  ```

---

## ▶️ 使用方法

### 1️⃣ Colabで開く
上部の **「Open in Colab」バッジ** をクリックして、`Google Colaboratoryを使ってみよう.ipynb` を開きます。

### 2️⃣ APIキー設定
ノートブック内で以下を実行してOpenAI APIキーを設定します：
```python
import os
os.environ["OPENAI_API_KEY"] = "sk-xxxxx..."
```

### 3️⃣ 各章のノートブックを実行
| 章 | 内容 | Colabリンク |
|----|------|--------------|
| 第2章 | Chat Completionsと連続対話 | [Open in Colab](https://colab.research.google.com/github/Trainocate-f/OpenAIAPIApp_Lecture_github/blob/main/OpenAIAPIApp_Lecture_github/chapter2/第2章%20Chat%20Completions.ipynb) |
| 第3章 | Text-to-Speechと画像生成 | [Open in Colab](https://colab.research.google.com/github/Trainocate-f/OpenAIAPIApp_Lecture_github/blob/main/OpenAIAPIApp_Lecture_github/chapter3/第3章%20Text-to-speech.ipynb) |
| 第4章 | Embeddingsによる検索と類似度 | [Open in Colab](https://colab.research.google.com/github/Trainocate-f/OpenAIAPIApp_Lecture_github/blob/main/OpenAIAPIApp_Lecture_github/chapter4/第4章%20Embedding.ipynb) |

---

## 📚 学べる内容
- OpenAI API の使い方と基本構成  
- ChatGPTを活用した応答設計  
- 音声・画像・テキスト変換の応用例  
- Embeddingによる意味検索・類似度計算  
- APIを組み合わせたアプリ開発の基礎  

---

## ⚠️ 注意事項
- **APIキーは絶対に公開リポジトリに含めないでください。**
- 本教材は教育目的のために作成されています。商用利用の際はOpenAI利用規約を遵守してください。

---

## 🧑‍🏫 作者・ライセンス
- Author: Trainocate  
- License: MIT  
- Platform: Google Colaboratory

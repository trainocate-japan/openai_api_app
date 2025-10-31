# 生成AIアプリ開発入門 ～OpenAI API活用～

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Trainocate-f/OpenAIAPIApp_Lecture_github/blob/main/OpenAIAPIApp_Lecture_github/Google%20Colaboratoryを使ってみよう.ipynb)

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
| 章 | 内容 | Colabリンク |
|----|------|--------------|
| 第2章 | Chat Completionsと連続対話 | [Open in Colab](https://colab.research.google.com/github/Trainocate-f/OpenAIAPIApp_Lecture_github/blob/main/OpenAIAPIApp_Lecture_github/chapter2/第2章%20Chat%20Completions.ipynb) |
| 第3章 | Text-to-Speechと画像生成 | [Open in Colab](https://colab.research.google.com/github/Trainocate-f/OpenAIAPIApp_Lecture_github/blob/main/OpenAIAPIApp_Lecture_github/chapter3/第3章%20Text-to-speech.ipynb) |
| 第4章 | Embeddingsによる検索と類似度 | [Open in Colab](https://colab.research.google.com/github/Trainocate-f/OpenAIAPIApp_Lecture_github/blob/main/OpenAIAPIApp_Lecture_github/chapter4/第4章%20Embedding.ipynb) |

---

## 注意事項
- **APIキーは絶対に公開リポジトリに含めないでください。**
- 本教材は教育目的のために作成されています。商用利用の際はOpenAI利用規約を遵守してください。

---
title: AI 圖片生成工具
emoji: 🎨
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: "4.26.0"
python_version: "3.9"
app_file: app.py
pinned: false
---

# AI 圖片生成工具

一個專業的 AI 圖片生成工具，支持多種先進的圖片生成模型。

## 功能特性

- 🤖 支持多個 AI 模型（grok-image、qwen-image、glm-image、gpt-image-1、gpt-image-1.5）
- 🎯 靈活的參數配置（尺寸、質量、風格）
- 🚀 快速響應和高質量輸出
- 💻 友好的 Web 界面（Gradio）
- 📱 完全響應式設計

## 快速開始

1. 輸入圖片描述
2. 選擇模型和參數
3. 點擊「生成圖片」按鈕
4. 等待結果

## 支持的模型

| 模型 | 提供商 | 特點 |
|------|------|------|
| grok-image | XAI | 快速、高效 |
| qwen-image | 阿里 | 中文優化 |
| glm-image | 清華 | 多模態 |
| gpt-image-1 | OpenAI | 高質量 |
| gpt-image-1.5 | OpenAI | 最佳效果 |

## 環境變數

需要設置以下環境變數：

- `API_KEY`: 你的 API 密鑰

在 HuggingFace Spaces 中，通過 Repository secrets 設置。

## 文檔

- [完整文檔](README.md)
- [快速開始](QUICKSTART.md)
- [API 參考](API_REFERENCE.md)
- [部署指南](DEPLOYMENT_GUIDE.md)
- [高級配置](ADVANCED_CONFIG.md)

---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

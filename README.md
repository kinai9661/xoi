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

# 🎨 AI 圖片生成工具

一個專業的 AI 圖片生成工具，支持多種先進的圖片生成模型，可直接部署到 HuggingFace Spaces。

## ✨ 功能特性

- 🤖 支持多個 AI 模型（grok-image、qwen-image、glm-image、gpt-image-1、gpt-image-1.5）
- 🎯 靈活的參數配置（尺寸、質量、風格）
- 🚀 快速響應和高質量輸出
- 💻 友好的 Web 界面（Gradio）
- 📱 完全響應式設計
- 🔒 安全的 API 密鑰管理

## 📋 支持的模型

| 模型 | 提供商 | 特點 | 推薦場景 |
|------|------|------|--------|
| grok-image | XAI | 快速、高效 | 實時應用 |
| qwen-image | 阿里 | 中文理解強 | 中文提示詞 |
| glm-image | 清華 | 多模態 | 複雜場景 |
| gpt-image-1 | OpenAI | 高質量 | 專業用途 |
| gpt-image-1.5 | OpenAI | 最新版本 | 最佳效果 |

## 🔧 API 參數

### 請求參數

```json
{
  "prompt": "圖片描述文本",
  "model": "grok-image",
  "size": "1024x1024",
  "quality": "standard",
  "style": "natural",
  "n": 1,
  "response_format": "url"
}
```

### 參數說明

| 參數 | 類型 | 默認值 | 說明 |
|------|------|--------|------|
| prompt | string | 必需 | 圖片描述，越詳細越好 |
| model | string | grok-image | 選擇生成模型 |
| size | string | 1024x1024 | 圖片尺寸：512x512, 1024x1024, 1792x1024, 1024x1792 |
| quality | string | standard | 質量等級：standard, hd |
| style | string | natural | 風格：natural, vivid |
| n | integer | 1 | 生成數量：1-10 |
| response_format | string | url | 返回格式：url, b64_json |

## 🚀 快速開始

### 本地運行

1. **安裝依賴**
```bash
pip install -r requirements.txt
```

2. **配置環境變數**
```bash
# 編輯 .env 文件
API_KEY=your_api_key_here
```

3. **運行應用**
```bash
python app.py
```

4. **訪問應用**
打開瀏覽器訪問 `http://localhost:7860`

### 部署到 HuggingFace Spaces

#### 方法 1：Web 界面部署（最簡單）

1. 訪問 [HuggingFace Spaces](https://huggingface.co/spaces)
2. 點擊 "Create new Space"
3. 填寫信息並選擇 "Gradio" SDK
4. 上傳文件：`app.py`、`requirements.txt`
5. 進入 Settings → Repository secrets
6. 添加 `API_KEY` = 你的密鑰
7. 完成！

#### 方法 2：Git 推送部署

```bash
git init
git add .
git commit -m "Initial commit"
git remote add space https://huggingface.co/spaces/<username>/<space-name>
git push space main
```

## 📝 使用示例

### 示例 1：生成風景圖片
```
提示詞：一隻在雪山上的紅色狐狸，高清攝影，逆光，細節豐富
模型：grok-image
尺寸：1024x1024
質量：hd
風格：vivid
```

### 示例 2：生成城市場景
```
提示詞：未來城市，霓虹燈，賽博朋克風格，夜景，高樓大廈
模型：qwen-image
尺寸：1792x1024
質量：standard
風格：vivid
```

### 示例 3：生成自然風景
```
提示詞：寧靜的日本花園，櫻花盛開，石燈籠，小橋流水
模型：glm-image
尺寸：1024x1024
質量：standard
風格：natural
```

## 💡 提示和最佳實踐

### 提示詞編寫建議

1. **詳細描述**：提供盡可能多的細節
   - ✅ 好：「一隻紅色的狐狸，坐在雪地上，背景是雪山，陽光照射，高清攝影」
   - ❌ 差：「狐狸」

2. **包含風格信息**：
   - 藝術風格：油畫、水彩、素描、3D 渲染
   - 攝影風格：高清、4K、電影級、逆光
   - 光線效果：金色時光、藍色時刻、霓虹燈

3. **指定質量**：
   - 「高清」、「超高清」、「4K」、「8K」
   - 「細節豐富」、「精細」、「逼真」

### 模型選擇建議

- **快速生成**：使用 `grok-image`
- **中文優化**：使用 `qwen-image`
- **複雜場景**：使用 `glm-image`
- **專業用途**：使用 `gpt-image-1` 或 `gpt-image-1.5`

### 尺寸選擇建議

- **正方形**：1024x1024（通用）
- **橫幅**：1792x1024（寬屏展示）
- **豎幅**：1024x1792（手機展示）
- **小圖**：512x512（快速預覽）

## 📦 文件結構

```
.
├── app.py              # 主應用程序
├── requirements.txt    # Python 依賴
├── .env               # 環境變數（本地開發）
├── .env.example       # 環境變數示例
├── .gitignore         # Git 忽略文件
├── README.md          # 本文件
├── QUICKSTART.md      # 快速開始指南
├── DEPLOYMENT_GUIDE.md # 部署指南
├── API_REFERENCE.md   # API 參考文檔
├── ADVANCED_CONFIG.md # 高級配置指南
└── PROJECT_SUMMARY.md # 項目總結
```

## 🛠️ 技術棧

- **前端框架**：Gradio 4.26.0
- **HTTP 客戶端**：requests 2.31.0
- **環境管理**：python-dotenv 1.0.0
- **Python 版本**：3.8+

## 🔐 安全性

- API 密鑰存儲在環境變數中
- 不在代碼中硬編碼敏感信息
- HuggingFace Secrets 用於安全存儲

## 📄 許可證

MIT License

## 🤝 貢獻

歡迎提交 Issue 和 Pull Request！

## 📞 支持

如有問題，請：
1. 檢查 API 密鑰是否正確
2. 確認網絡連接
3. 查看錯誤日誌
4. 提交 Issue

## 🔗 相關資源

- [Gradio 文檔](https://www.gradio.app/)
- [HuggingFace Spaces](https://huggingface.co/spaces)
- [AI 圖片生成 API](https://ai.ezif.in)
- [快速開始指南](QUICKSTART.md)
- [API 參考文檔](API_REFERENCE.md)
- [部署指南](DEPLOYMENT_GUIDE.md)
- [高級配置](ADVANCED_CONFIG.md)
- [項目總結](PROJECT_SUMMARY.md)

---

**最後更新**：2026-04-02

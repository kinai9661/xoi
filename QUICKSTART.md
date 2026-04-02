# ⚡ 快速開始指南

## 5 分鐘快速上手

### 1️⃣ 本地運行（最快）

```bash
# 克隆或下載項目
cd image-generator

# 安裝依賴
pip install -r requirements.txt

# 運行應用
python app.py
```

訪問 `http://localhost:7860` 即可使用。

---

### 2️⃣ 部署到 HuggingFace（推薦）

#### 方式 A：Web 界面（無需命令行）

1. 訪問 https://huggingface.co/spaces
2. 點擊 "Create new Space"
3. 選擇 "Gradio" SDK
4. 上傳文件：`app.py`、`requirements.txt`
5. 進入 Settings → Repository secrets
6. 添加 `API_KEY` = 你的密鑰
7. 完成！

#### 方式 B：Git 推送（推薦開發者）

```bash
# 初始化 Git
git init
git add .
git commit -m "Initial commit"

# 添加 HuggingFace 遠程
git remote add space https://huggingface.co/spaces/<username>/<space-name>

# 推送
git push space main
```

---

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

---

## 🎯 模型選擇速查表

| 需求 | 推薦模型 | 原因 |
|------|--------|------|
| 最快速度 | grok-image | ⚡ 最快 |
| 中文優化 | qwen-image | 🇨🇳 中文理解強 |
| 複雜場景 | glm-image | 🎨 多模態能力 |
| 最高質量 | gpt-image-1.5 | ⭐ 最佳效果 |
| 預算有限 | grok-image | 💰 成本低 |

---

## 🔧 常見配置

### 快速預覽
```
尺寸：512x512
質量：standard
數量：1
```

### 標準輸出
```
尺寸：1024x1024
質量：standard
數量：1
```

### 高質量輸出
```
尺寸：1024x1024
質量：hd
數量：1
```

### 批量生成
```
尺寸：1024x1024
質量：standard
數量：5
```

---

## 💡 提示詞技巧

### ✅ 好的提示詞結構

```
[主體] + [動作] + [背景] + [光線] + [風格] + [質量]
```

### 示例

```
一隻紅色的狐狸 + 坐著 + 雪地和雪山 + 陽光照射 + 高清攝影 + 4K 超高清
```

### 關鍵詞參考

**風格**：油畫、水彩、素描、3D 渲染、電影級、攝影

**光線**：金色時光、藍色時刻、逆光、側光、背光

**質量**：高清、超高清、4K、8K、細節豐富、逼真

---

## 🚀 部署檢查清單

- [ ] 安裝了依賴
- [ ] 本地測試成功
- [ ] 獲得了 API 密鑰
- [ ] 創建了 HuggingFace Space
- [ ] 上傳了文件
- [ ] 配置了 API_KEY secret
- [ ] 部署成功
- [ ] 可以生成圖片

---

## 🆘 快速故障排除

### 問題：`ModuleNotFoundError`
```bash
# 解決：安裝依賴
pip install -r requirements.txt
```

### 問題：API 密鑰錯誤
```
檢查：
1. 密鑰是否正確
2. 是否添加到 .env 或 secrets
3. 重啟應用
```

### 問題：生成超時
```
嘗試：
1. 使用更快的模型（grok-image）
2. 減少生成數量
3. 使用更小的尺寸
```

### 問題：部署失敗
```
檢查：
1. requirements.txt 是否正確
2. app.py 是否有語法錯誤
3. 查看 Logs 標籤
```

---

## 📚 下一步

- 📖 閱讀 [完整文檔](README.md)
- 🔗 查看 [API 參考](API_REFERENCE.md)
- 🚀 查看 [部署指南](DEPLOYMENT_GUIDE.md)
- 💬 提交 Issue 或 PR

---

## 🎉 成功標誌

✅ 你已成功設置了 AI 圖片生成工具！

現在你可以：
- 🎨 生成高質量圖片
- 🔄 嘗試不同的模型
- 📤 分享你的創作
- 🚀 部署到生產環境

---

**祝你使用愉快！** 🚀

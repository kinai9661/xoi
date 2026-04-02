# 🚀 HuggingFace Spaces 部署指南

## 📋 前置要求

- HuggingFace 賬戶
- Git 已安裝
- API 密鑰

## 方法 1：Web 界面部署（最簡單）

### 步驟 1：創建 Space

1. 訪問 [HuggingFace Spaces](https://huggingface.co/spaces)
2. 點擊右上角 "Create new Space"
3. 填寫信息：
   - **Space name**: `image-generator`（或自定義名稱）
   - **License**: 選擇 "MIT"
   - **Space SDK**: 選擇 "Gradio"
   - **Visibility**: 選擇 "Public" 或 "Private"

4. 點擊 "Create Space"

### 步驟 2：上傳文件

1. 進入新建的 Space
2. 點擊 "Files" 標籤
3. 上傳以下文件：
   - `app.py`
   - `requirements.txt`
   - `README.md`

### 步驟 3：配置環境變數

1. 進入 Space 設置（Settings）
2. 找到 "Repository secrets" 部分
3. 點擊 "Add a secret"
4. 填寫：
   - **Name**: `API_KEY`
   - **Value**: 你的 API 密鑰
5. 點擊 "Add secret"

### 步驟 4：等待部署

Space 會自動部署，你可以在 "Logs" 標籤中查看部署進度。

---

## 方法 2：Git 推送部署

### 步驟 1：準備本地倉庫

```bash
# 進入項目目錄
cd image-generator

# 初始化 Git 倉庫
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit: AI Image Generator"
```

### 步驟 2：創建 HuggingFace Space

1. 訪問 [HuggingFace Spaces](https://huggingface.co/spaces)
2. 點擊 "Create new Space"
3. 選擇 "Gradio" SDK
4. 創建 Space

### 步驟 3：添加遠程倉庫

```bash
# 替換 <username> 和 <space-name>
git remote add space https://huggingface.co/spaces/<username>/<space-name>

# 例如：
# git remote add space https://huggingface.co/spaces/myusername/image-generator
```

### 步驟 4：推送代碼

```bash
git push space main
```

如果提示需要認證，使用你的 HuggingFace 用戶名和 token。

### 步驟 5：配置 Secrets

1. 進入 Space 設置
2. 添加 `API_KEY` secret（同方法 1 的步驟 3）

---

## 方法 3：使用 HuggingFace CLI

### 步驟 1：安裝 HuggingFace CLI

```bash
pip install huggingface-hub
```

### 步驟 2：登錄

```bash
huggingface-cli login
```

### 步驟 3：創建 Space

```bash
huggingface-cli repo create image-generator --type space --space-sdk gradio
```

### 步驟 4：克隆 Space

```bash
git clone https://huggingface.co/spaces/<username>/image-generator
cd image-generator
```

### 步驟 5：添加文件

```bash
# 複製你的文件到這個目錄
cp ../app.py .
cp ../requirements.txt .
cp ../README.md .
```

### 步驟 6：推送

```bash
git add .
git commit -m "Add image generator"
git push
```

---

## 🔐 安全性檢查清單

- [ ] API 密鑰已添加到 Repository secrets
- [ ] `.env` 文件已添加到 `.gitignore`
- [ ] 代碼中沒有硬編碼的敏感信息
- [ ] 使用了 `os.getenv()` 讀取環境變數

---

## 🧪 測試部署

### 本地測試

```bash
# 安裝依賴
pip install -r requirements.txt

# 運行應用
python app.py
```

訪問 `http://localhost:7860` 測試。

### 遠程測試

部署完成後，訪問你的 Space URL：
```
https://huggingface.co/spaces/<username>/<space-name>
```

---

## 🐛 故障排除

### 問題 1：部署失敗

**症狀**：Space 顯示紅色錯誤

**解決方案**：
1. 檢查 "Logs" 標籤中的錯誤信息
2. 確保 `requirements.txt` 中的所有依賴都正確
3. 確保 `app.py` 中沒有語法錯誤

### 問題 2：API 密鑰錯誤

**症狀**：生成圖片時出現認證錯誤

**解決方案**：
1. 檢查 API 密鑰是否正確
2. 確保 secret 名稱是 `API_KEY`
3. 重新啟動 Space（Settings → Restart this Space）

### 問題 3：超時錯誤

**症狀**：生成圖片時超時

**解決方案**：
1. 檢查網絡連接
2. 嘗試使用更快的模型（如 `grok-image`）
3. 減少生成數量

### 問題 4：內存不足

**症狀**：Space 崩潰或無響應

**解決方案**：
1. 減少並發請求
2. 使用更小的圖片尺寸
3. 升級 Space 計算資源

---

## 📊 監控和維護

### 查看日誌

1. 進入 Space
2. 點擊 "Logs" 標籤
3. 查看實時日誌

### 更新代碼

```bash
# 本地修改後
git add .
git commit -m "Update: description"
git push space main
```

### 重啟 Space

1. 進入 Settings
2. 點擊 "Restart this Space"

---

## 💰 成本考慮

- **免費層**：有限的計算資源，可能會休眠
- **付費層**：持續運行，更多資源

詳見 [HuggingFace Pricing](https://huggingface.co/pricing)

---

## 📚 相關資源

- [Gradio 文檔](https://www.gradio.app/)
- [HuggingFace Spaces 文檔](https://huggingface.co/docs/hub/spaces)
- [HuggingFace Hub 庫](https://github.com/huggingface/hub)

---

## ✅ 部署檢查清單

- [ ] 創建了 HuggingFace Space
- [ ] 上傳了所有必要文件
- [ ] 配置了 API_KEY secret
- [ ] 本地測試成功
- [ ] 遠程部署成功
- [ ] 可以訪問 Space URL
- [ ] 可以生成圖片

---

**祝部署順利！** 🎉

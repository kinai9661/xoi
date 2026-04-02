# Leapcell 部署配置

## 部署步驟

### 1. 準備文件
確保以下文件已準備好：
- app.py
- requirements.txt
- .env（包含 API_KEY）

### 2. 在 Leapcell 中創建應用

1. 訪問 [Leapcell](https://leapcell.io)
2. 登錄或註冊賬戶
3. 點擊 "Create New App"
4. 選擇 "Python" 運行時
5. 上傳項目文件

### 3. 配置環境變數

在 Leapcell 應用設置中：
1. 進入 "Environment Variables"
2. 添加 `API_KEY` = 你的 API 密鑰

### 4. 配置啟動命令

設置啟動命令為：
```
python app.py
```

### 5. 部署

1. 點擊 "Deploy"
2. 等待部署完成
3. 訪問提供的 URL

## 本地測試

在部署前，建議本地測試：

```bash
pip install -r requirements.txt
python app.py
```

訪問 `http://localhost:7860`

## 故障排除

### 問題：API 密鑰錯誤
- 檢查環境變數是否正確設置
- 確保密鑰沒有多餘的空格

### 問題：模塊導入錯誤
- 確保 requirements.txt 中的所有依賴都已列出
- 檢查 Python 版本兼容性

### 問題：超時
- 增加超時設置
- 檢查網絡連接

## 監控

部署後，可以在 Leapcell 儀表板中：
- 查看應用日誌
- 監控資源使用
- 管理環境變數
- 查看部署歷史

## 更新應用

要更新應用：
1. 修改本地文件
2. 提交更改
3. 在 Leapcell 中重新部署

---

更多信息請訪問 [Leapcell 文檔](https://docs.leapcell.io)

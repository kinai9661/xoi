# 🔧 高級配置指南

## 自定義應用

### 修改 UI 主題

編輯 `app.py` 中的 `create_interface()` 方法：

```python
# 更改主題
with gr.Blocks(
    title="AI 圖片生成工具",
    theme=gr.themes.Soft(),  # 可選：Soft, Default, Base, Glass
    css="""
    .container { max-width: 1200px; margin: 0 auto; }
    """
) as demo:
```

**可用主題**：
- `gr.themes.Soft()` - 柔和風格
- `gr.themes.Default()` - 默認風格
- `gr.themes.Base()` - 基礎風格
- `gr.themes.Glass()` - 玻璃風格

### 自定義 CSS

```python
css="""
/* 自定義樣式 */
.header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 20px;
    border-radius: 10px;
}

.button-primary {
    background-color: #667eea;
    border-radius: 8px;
}
"""
```

---

## 添加新模型

### 步驟 1：更新模型列表

編輯 `app.py` 中的 `__init__` 方法：

```python
self.models = [
    "grok-image",
    "qwen-image", 
    "glm-image",
    "gpt-image-1",
    "gpt-image-1.5",
    "your-new-model"  # 添加新模型
]
```

### 步驟 2：添加模型描述

在 `create_interface()` 中添加：

```python
model_info = {
    "grok-image": "XAI 的 Grok 模型，快速高效",
    "your-new-model": "新模型的描述"
}
```

---

## 擴展功能

### 添加圖片下載功能

```python
def download_image(url):
    """下載圖片"""
    import urllib.request
    filename = url.split('/')[-1]
    urllib.request.urlretrieve(url, filename)
    return f"已下載：{filename}"

# 在界面中添加
download_btn = gr.Button("⬇️ 下載圖片")
download_btn.click(
    fn=download_image,
    inputs=output_url,
    outputs=gr.Textbox()
)
```

### 添加歷史記錄

```python
import json
from datetime import datetime

class HistoryManager:
    def __init__(self, filename="history.json"):
        self.filename = filename
    
    def save(self, prompt, model, result):
        """保存生成記錄"""
        record = {
            "timestamp": datetime.now().isoformat(),
            "prompt": prompt,
            "model": model,
            "result": result
        }
        
        try:
            with open(self.filename, 'r') as f:
                history = json.load(f)
        except:
            history = []
        
        history.append(record)
        
        with open(self.filename, 'w') as f:
            json.dump(history, f, indent=2, ensure_ascii=False)
    
    def load(self):
        """加載歷史記錄"""
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except:
            return []
```

### 添加用戶反饋

```python
def save_feedback(rating, comment):
    """保存用戶反饋"""
    feedback = {
        "timestamp": datetime.now().isoformat(),
        "rating": rating,
        "comment": comment
    }
    
    with open("feedback.json", 'a') as f:
        json.dump(feedback, f, ensure_ascii=False)
        f.write('\n')
    
    return "感謝你的反饋！"

# 在界面中添加
with gr.Row():
    rating = gr.Radio(
        choices=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
        label="評分"
    )
    comment = gr.Textbox(label="評論", placeholder="分享你的想法...")
    feedback_btn = gr.Button("提交反饋")

feedback_btn.click(
    fn=save_feedback,
    inputs=[rating, comment],
    outputs=gr.Textbox()
)
```

---

## 性能優化

### 1. 添加緩存

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def get_model_info(model_name):
    """緩存模型信息"""
    # 模型信息查詢邏輯
    pass
```

### 2. 異步請求

```python
import asyncio
import aiohttp

async def generate_async(prompt, model):
    """異步生成圖片"""
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://ai.ezif.in/v1/images/generations",
            json=payload
        ) as resp:
            return await resp.json()
```

### 3. 請求超時設置

```python
response = requests.post(
    url,
    headers=headers,
    json=payload,
    timeout=120  # 120 秒超時
)
```

---

## 安全性增強

### 1. 輸入驗證

```python
def validate_prompt(prompt):
    """驗證提示詞"""
    if not prompt or len(prompt) < 5:
        raise ValueError("提示詞太短")
    
    if len(prompt) > 4000:
        raise ValueError("提示詞太長")
    
    # 檢查敏感詞
    forbidden_words = ["xxx", "yyy"]
    if any(word in prompt.lower() for word in forbidden_words):
        raise ValueError("包含不允許的內容")
    
    return True
```

### 2. 速率限制

```python
from datetime import datetime, timedelta

class RateLimiter:
    def __init__(self, max_requests=10, window_seconds=60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = []
    
    def is_allowed(self):
        """檢查是否允許請求"""
        now = datetime.now()
        # 移除過期的請求記錄
        self.requests = [
            req_time for req_time in self.requests
            if now - req_time < timedelta(seconds=self.window_seconds)
        ]
        
        if len(self.requests) < self.max_requests:
            self.requests.append(now)
            return True
        return False
```

### 3. 日誌記錄

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# 使用
logger.info(f"生成圖片: {prompt}")
logger.error(f"API 錯誤: {error}")
```

---

## 部署優化

### 1. Docker 部署

創建 `Dockerfile`：

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV API_KEY=${API_KEY}

CMD ["python", "app.py"]
```

構建和運行：

```bash
docker build -t image-generator .
docker run -e API_KEY=your_key -p 7860:7860 image-generator
```

### 2. 環境變數管理

```python
import os
from dotenv import load_dotenv

load_dotenv()

# 必需的環境變數
REQUIRED_ENV_VARS = ['API_KEY']

for var in REQUIRED_ENV_VARS:
    if not os.getenv(var):
        raise ValueError(f"缺少必需的環境變數: {var}")

API_KEY = os.getenv('API_KEY')
API_URL = os.getenv('API_URL', 'https://ai.ezif.in')
DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
```

### 3. 健康檢查

```python
@app.get("/health")
def health_check():
    """健康檢查端點"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }
```

---

## 監控和分析

### 1. 使用統計

```python
class UsageStats:
    def __init__(self):
        self.total_requests = 0
        self.total_images = 0
        self.model_usage = {}
    
    def record(self, model, count):
        """記錄使用統計"""
        self.total_requests += 1
        self.total_images += count
        self.model_usage[model] = self.model_usage.get(model, 0) + count
    
    def get_stats(self):
        """獲取統計信息"""
        return {
            "total_requests": self.total_requests,
            "total_images": self.total_images,
            "model_usage": self.model_usage
        }
```

### 2. 性能監控

```python
import time

def measure_time(func):
    """測量函數執行時間"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        logger.info(f"{func.__name__} 耗時: {elapsed:.2f}s")
        return result
    return wrapper

@measure_time
def generate(prompt, model):
    # 生成邏輯
    pass
```

---

## 故障排除

### 常見問題

**Q: 如何增加超時時間？**
```python
response = requests.post(url, timeout=300)  # 5 分鐘
```

**Q: 如何添加代理？**
```python
proxies = {
    "http": "http://proxy.example.com:8080",
    "https": "http://proxy.example.com:8080"
}
response = requests.post(url, proxies=proxies)
```

**Q: 如何處理大量並發請求？**
```python
# 使用隊列
from queue import Queue
import threading

request_queue = Queue()

def worker():
    while True:
        request = request_queue.get()
        # 處理請求
        request_queue.task_done()

# 啟動工作線程
for _ in range(5):
    threading.Thread(target=worker, daemon=True).start()
```

---

## 相關資源

- [Gradio 高級功能](https://www.gradio.app/docs/advanced)
- [Python 最佳實踐](https://pep8.org/)
- [Docker 文檔](https://docs.docker.com/)

---

**最後更新**: 2026-04-02

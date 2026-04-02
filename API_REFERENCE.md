# 📚 API 參數參考

## 完整 API 文檔

### 端點

```
POST https://ai.ezif.in/v1/images/generations
```

### 認證

```
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

---

## 請求參數

### 必需參數

#### `prompt` (string)

圖片描述文本。

- **類型**: string
- **必需**: 是
- **最大長度**: 4000 字符
- **示例**: `"一隻在雪山上的紅色狐狸，高清攝影"`

**提示詞編寫建議**：
- 詳細描述場景、主體、背景
- 包含風格、光線、質量信息
- 使用具體的形容詞而不是模糊的描述

---

### 可選參數

#### `model` (string)

選擇圖片生成模型。

- **類型**: string
- **默認值**: `grok-image`
- **可選值**:
  - `grok-image` - XAI 的 Grok 模型，快速高效
  - `qwen-image` - 阿里的通義千問，中文優化
  - `glm-image` - 清華的 GLM，多模態能力強
  - `gpt-image-1` - OpenAI 的 DALL-E 3，高質量
  - `gpt-image-1.5` - OpenAI 最新版本，最佳效果

**模型對比**:

| 模型 | 速度 | 質量 | 中文支持 | 推薦場景 |
|------|------|------|--------|--------|
| grok-image | ⚡⚡⚡ | ⭐⭐⭐ | 中等 | 實時應用 |
| qwen-image | ⚡⚡ | ⭐⭐⭐⭐ | 優秀 | 中文提示詞 |
| glm-image | ⚡⚡ | ⭐⭐⭐⭐ | 優秀 | 複雜場景 |
| gpt-image-1 | ⚡ | ⭐⭐⭐⭐⭐ | 中等 | 專業用途 |
| gpt-image-1.5 | ⚡ | ⭐⭐⭐⭐⭐ | 中等 | 最佳效果 |

---

#### `size` (string)

圖片輸出尺寸。

- **類型**: string
- **默認值**: `1024x1024`
- **可選值**:
  - `512x512` - 小圖，快速預覽
  - `1024x1024` - 標準正方形，通用
  - `1792x1024` - 寬屏橫幅
  - `1024x1792` - 豎屏手機

**尺寸選擇建議**:

| 尺寸 | 寬高比 | 用途 | 生成時間 |
|------|--------|------|--------|
| 512x512 | 1:1 | 快速預覽、縮略圖 | 最快 |
| 1024x1024 | 1:1 | 通用、社交媒體 | 中等 |
| 1792x1024 | 16:9 | 寬屏展示、橫幅 | 較慢 |
| 1024x1792 | 9:16 | 手機展示、豎幅 | 較慢 |

---

#### `quality` (string)

圖片質量等級。

- **類型**: string
- **默認值**: `standard`
- **可選值**:
  - `standard` - 標準質量，快速生成
  - `hd` - 高清質量，更多細節

**質量對比**:

| 質量 | 細節 | 生成時間 | 成本 | 推薦場景 |
|------|------|--------|------|--------|
| standard | 中等 | 快 | 低 | 快速預覽、實時應用 |
| hd | 豐富 | 慢 | 高 | 專業用途、最終輸出 |

---

#### `style` (string)

圖片風格。

- **類型**: string
- **默認值**: `natural`
- **可選值**:
  - `natural` - 自然風格，逼真寫實
  - `vivid` - 鮮豔風格，藝術化

**風格對比**:

| 風格 | 特點 | 適用場景 |
|------|------|--------|
| natural | 逼真、寫實、細節豐富 | 產品圖、風景、人物 |
| vivid | 鮮豔、藝術化、色彩飽和 | 藝術創作、概念設計 |

---

#### `n` (integer)

一次生成的圖片數量。

- **類型**: integer
- **默認值**: `1`
- **範圍**: 1-10
- **示例**: `3`

**注意**:
- 生成數量越多，耗時越長
- 成本與生成數量成正比

---

#### `response_format` (string)

返回格式。

- **類型**: string
- **默認值**: `url`
- **可選值**:
  - `url` - 返回圖片 URL
  - `b64_json` - 返回 Base64 編碼的圖片

**格式對比**:

| 格式 | 優點 | 缺點 | 用途 |
|------|------|------|------|
| url | 直接訪問、節省帶寬 | 需要網絡訪問 | 通常使用 |
| b64_json | 完全離線、安全 | 數據量大 | 特殊需求 |

---

## 請求示例

### 示例 1：基礎請求

```bash
curl -X POST "https://ai.ezif.in/v1/images/generations" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-YOUR_API_KEY" \
  -d '{
    "prompt": "一隻紅色的狐狸",
    "model": "grok-image",
    "size": "1024x1024"
  }'
```

### 示例 2：完整請求

```bash
curl -X POST "https://ai.ezif.in/v1/images/generations" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-YOUR_API_KEY" \
  -d '{
    "prompt": "一隻在雪山上的紅色狐狸，高清攝影，逆光，細節豐富",
    "model": "gpt-image-1.5",
    "size": "1024x1024",
    "quality": "hd",
    "style": "vivid",
    "n": 2,
    "response_format": "url"
  }'
```

### 示例 3：Python 請求

```python
import requests

api_key = "sk-YOUR_API_KEY"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "prompt": "未來城市，霓虹燈，賽博朋克風格",
    "model": "qwen-image",
    "size": "1792x1024",
    "quality": "standard",
    "style": "vivid",
    "n": 1
}

response = requests.post(
    "https://ai.ezif.in/v1/images/generations",
    headers=headers,
    json=payload
)

result = response.json()
print(result)
```

### 示例 4：JavaScript 請求

```javascript
const apiKey = "sk-YOUR_API_KEY";

const payload = {
  prompt: "寧靜的日本花園，櫻花盛開",
  model: "glm-image",
  size: "1024x1024",
  quality: "standard",
  style: "natural",
  n: 1
};

fetch("https://ai.ezif.in/v1/images/generations", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "Authorization": `Bearer ${apiKey}`
  },
  body: JSON.stringify(payload)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

## 響應格式

### 成功響應 (200 OK)

```json
{
  "created": 1712145600,
  "data": [
    {
      "url": "https://example.com/image1.png",
      "revised_prompt": "A red fox on a snowy mountain..."
    },
    {
      "url": "https://example.com/image2.png",
      "revised_prompt": "A red fox on a snowy mountain..."
    }
  ]
}
```

**響應字段**:

| 字段 | 類型 | 說明 |
|------|------|------|
| created | integer | Unix 時間戳 |
| data | array | 生成的圖片列表 |
| data[].url | string | 圖片 URL |
| data[].revised_prompt | string | 修訂後的提示詞 |

### 錯誤響應

```json
{
  "error": {
    "message": "Invalid API key",
    "type": "invalid_request_error",
    "param": "api_key",
    "code": "invalid_api_key"
  }
}
```

**常見錯誤**:

| 錯誤碼 | 說明 | 解決方案 |
|--------|------|--------|
| invalid_api_key | API 密鑰無效 | 檢查密鑰是否正確 |
| invalid_request_error | 請求參數錯誤 | 檢查參數格式 |
| rate_limit_exceeded | 超過速率限制 | 等待後重試 |
| server_error | 服務器錯誤 | 稍後重試 |

---

## 提示詞最佳實踐

### ✅ 好的提示詞

```
"一隻紅色的狐狸，坐在雪地上，背景是雪山，陽光照射，高清攝影，
逆光效果，細節豐富，4K 超高清，專業攝影"
```

### ❌ 不好的提示詞

```
"狐狸"
```

### 提示詞結構

```
[主體] + [動作/狀態] + [背景] + [光線] + [風格] + [質量]
```

**示例**:
- 主體：一隻紅色的狐狸
- 動作：坐著
- 背景：雪地和雪山
- 光線：陽光照射，逆光
- 風格：高清攝影
- 質量：4K 超高清

---

## 速率限制

- **免費層**: 每分鐘 10 個請求
- **付費層**: 根據訂閱級別而定

超過限制時會返回 429 錯誤。

---

## 成本估算

| 模型 | 尺寸 | 質量 | 成本 |
|------|------|------|------|
| grok-image | 1024x1024 | standard | 低 |
| qwen-image | 1024x1024 | standard | 中 |
| gpt-image-1 | 1024x1024 | hd | 高 |
| gpt-image-1.5 | 1792x1024 | hd | 最高 |

詳見官方定價頁面。

---

## 常見問題

### Q: 如何提高圖片質量？
A: 使用 `quality: "hd"` 和更詳細的提示詞。

### Q: 哪個模型最快？
A: `grok-image` 最快。

### Q: 支持中文提示詞嗎？
A: 支持，`qwen-image` 對中文優化最好。

### Q: 可以生成多少張圖片？
A: 最多 10 張（`n: 10`）。

### Q: 圖片 URL 有效期多長？
A: 通常 24 小時。

---

## 相關資源

- [官方 API 文檔](https://ai.ezif.in/docs)
- [模型對比](https://ai.ezif.in/models)
- [定價信息](https://ai.ezif.in/pricing)

---

**最後更新**: 2026-04-02

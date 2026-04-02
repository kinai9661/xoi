import os
from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY", "sk-VwTjpXD9eteIuJx27ZXCyAqNsdGrkUFo3mjBq8gK1s1OVt0K")
API_URL = "https://ai.ezif.in/v1/images/generations"

MODELS = [
    "grok-image",
    "qwen-image",
    "glm-image",
    "gpt-image-1",
    "gpt-image-1.5"
]

SIZES = [
    "512x512",
    "1024x1024",
    "1792x1024",
    "1024x1792"
]

@app.route('/')
def index():
    return render_template('index.html', models=MODELS, sizes=SIZES)

@app.route('/api/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        prompt = data.get('prompt', '').strip()
        
        if not prompt:
            return jsonify({"error": "請輸入圖片描述"}), 400
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        
        payload = {
            "model": data.get('model', 'grok-image'),
            "prompt": prompt,
            "size": data.get('size', '1024x1024'),
            "quality": data.get('quality', 'standard'),
            "style": data.get('style', 'natural'),
            "n": int(data.get('n', 1)),
            "response_format": "url"
        }
        
        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=120
        )
        
        if response.status_code != 200:
            return jsonify({"error": f"API 錯誤: {response.status_code}"}), 500
        
        return jsonify(response.json())
    
    except requests.exceptions.Timeout:
        return jsonify({"error": "請求超時"}), 500
    except requests.exceptions.ConnectionError:
        return jsonify({"error": "連接失敗"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/models', methods=['GET'])
def get_models():
    return jsonify({
        "models": MODELS,
        "sizes": SIZES
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)

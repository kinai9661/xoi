import os
import sys
os.environ['GRADIO_ANALYTICS_ENABLED'] = 'False'

import gradio as gr
import requests
import json
from typing import Optional, List, Dict, Any
from dotenv import load_dotenv

load_dotenv()

class ImageGeneratorAPI:
    def __init__(self, api_key: str, api_url: str = "https://ai.ezif.in"):
        self.api_key = api_key
        self.api_url = api_url
        self.models = [
            "grok-image",
            "qwen-image", 
            "glm-image",
            "gpt-image-1",
            "gpt-image-1.5"
        ]
        self.sizes = [
            "512x512",
            "1024x1024",
            "1792x1024",
            "1024x1792"
        ]
    
    def generate(
        self,
        prompt: str,
        model: str = "grok-image",
        size: str = "1024x1024",
        quality: str = "standard",
        style: str = "natural",
        n: int = 1
    ) -> Dict[str, Any]:
        """生成圖片"""
        if not prompt or not prompt.strip():
            return {"error": "請輸入圖片描述"}
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        payload = {
            "model": model,
            "prompt": prompt,
            "size": size,
            "quality": quality,
            "style": style,
            "n": n,
            "response_format": "url"
        }
        
        try:
            response = requests.post(
                f"{self.api_url}/v1/images/generations",
                headers=headers,
                json=payload,
                timeout=120
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            return {"error": "請求超時，請稍後重試"}
        except requests.exceptions.ConnectionError:
            return {"error": "連接失敗，請檢查網絡"}
        except requests.exceptions.HTTPError as e:
            return {"error": f"API 錯誤: {e.response.status_code}"}
        except Exception as e:
            return {"error": f"錯誤: {str(e)}"}
    
    def create_interface(self):
        """創建 Gradio 界面"""
        def generate_wrapper(prompt, model, size, quality, style, n):
            result = self.generate(prompt, model, size, quality, style, int(n))
            
            if "error" in result:
                return f"❌ {result['error']}"
            
            if "data" in result:
                images = result["data"]
                output = f"✅ 成功生成 {len(images)} 張圖片\n\n"
                for i, img in enumerate(images, 1):
                    url = img.get('url', 'N/A')
                    output += f"圖片 {i}: {url}\n"
                return output
            
            return "❌ 未知錯誤"
        
        with gr.Blocks(title="AI 圖片生成工具") as demo:
            gr.Markdown("""
            # 🎨 AI 圖片生成工具
            
            使用先進的 AI 模型生成高質量圖片。支持多種模型和自定義參數。
            """)
            
            with gr.Row():
                with gr.Column(scale=2):
                    gr.Markdown("### 📝 輸入設置")
                    
                    prompt = gr.Textbox(
                        label="圖片描述",
                        placeholder="詳細描述你想要生成的圖片...",
                        lines=4
                    )
                    
                    with gr.Row():
                        model = gr.Dropdown(
                            choices=self.models,
                            value="grok-image",
                            label="模型選擇"
                        )
                        size = gr.Dropdown(
                            choices=self.sizes,
                            value="1024x1024",
                            label="圖片尺寸"
                        )
                    
                    with gr.Row():
                        quality = gr.Radio(
                            choices=["standard", "hd"],
                            value="standard",
                            label="質量等級"
                        )
                        style = gr.Radio(
                            choices=["natural", "vivid"],
                            value="natural",
                            label="風格"
                        )
                    
                    n = gr.Slider(
                        minimum=1,
                        maximum=10,
                        value=1,
                        step=1,
                        label="生成數量"
                    )
                    
                    generate_btn = gr.Button(
                        "🚀 生成圖片",
                        variant="primary"
                    )
                
                with gr.Column(scale=2):
                    gr.Markdown("### 📤 結果")
                    output = gr.Textbox(
                        label="生成結果",
                        lines=15,
                        interactive=False
                    )
            
            gr.Markdown("### 📚 使用示例")
            gr.Examples(
                examples=[
                    [
                        "一隻在雪山上的紅色狐狸，高清攝影，逆光，細節豐富",
                        "grok-image",
                        "1024x1024",
                        "hd",
                        "vivid",
                        1
                    ],
                    [
                        "未來城市，霓虹燈，賽博朋克風格，夜景，高樓大廈",
                        "qwen-image",
                        "1792x1024",
                        "standard",
                        "vivid",
                        1
                    ],
                    [
                        "寧靜的日本花園，櫻花盛開，石燈籠，小橋流水",
                        "glm-image",
                        "1024x1024",
                        "standard",
                        "natural",
                        1
                    ],
                ],
                inputs=[prompt, model, size, quality, style, n],
                outputs=output,
                fn=generate_wrapper,
                cache_examples=False
            )
            
            generate_btn.click(
                fn=generate_wrapper,
                inputs=[prompt, model, size, quality, style, n],
                outputs=output
            )
        
        return demo


def main():
    api_key = os.getenv("API_KEY", "sk-VwTjpXD9eteIuJx27ZXCyAqNsdGrkUFo3mjBq8gK1s1OVt0K")
    
    if not api_key:
        raise ValueError("API_KEY 環境變數未設置")
    
    generator = ImageGeneratorAPI(api_key)
    demo = generator.create_interface()
    
    demo.launch(
        share=True,
        server_name="0.0.0.0",
        server_port=7860
    )


if __name__ == "__main__":
    main()

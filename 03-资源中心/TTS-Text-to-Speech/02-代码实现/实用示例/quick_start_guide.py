#!/usr/bin/env python3
"""
TTS快速开始指南
包含主流TTS模型的简单使用示例
"""

import os
import warnings
warnings.filterwarnings('ignore')

def setup_environment():
    """检查并安装必要的依赖"""
    required_packages = [
        'torch',
        'librosa',
        'numpy',
        'soundfile'
    ]
    
    print("检查TTS环境依赖...")
    for package in required_packages:
        try:
            __import__(package)
            print(f"✓ {package} 已安装")
        except ImportError:
            print(f"✗ {package} 未安装，请运行: pip install {package}")

def model_selection_guide():
    """模型选择指南"""
    print("\n" + "="*60)
    print("TTS模型选择指南")
    print("="*60)
    
    scenarios = {
        "个人学习/体验": "XTTS v2 - 开源易用，效果平衡",
        "中文商业应用": "Microsoft Azure TTS - 中文自然度最高",
        "英文内容创作": "OpenAI TTS - 英文效果出色",
        "语音克隆项目": "Fish Speech (开源) / ElevenLabs (商业)",
        "实时应用部署": "FastSpeech 2 - 推理速度快",
        "研究开发": "VITS / StyleTTS 2 - 架构清晰，效果前沿"
    }
    
    for scenario, recommendation in scenarios.items():
        print(f"• {scenario}: {recommendation}")

def api_usage_example():
    """API使用示例（伪代码）"""
    print("\n" + "="*60)
    print("主流TTS API使用示例")
    print("="*60)
    
    print("\n1. OpenAI TTS (Python示例):")
    print("""
from openai import OpenAI
client = OpenAI()

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="你好，这是一个TTS测试"
)
response.stream_to_file("output.mp3")
""")
    
    print("\n2. Azure Speech Service:")
    print("""
import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(
    subscription="your-key",
    region="your-region"
)

synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
result = synthesizer.speak_text_async("Hello, this is a TTS test").get()
""")

def resource_requirements():
    """资源需求说明"""
    print("\n" + "="*60)
    print("资源需求概览")
    print("="*60)
    
    requirements = {
        "XTTS v2": "GPU推荐，8GB+显存，多语言支持",
        "VITS/FastSpeech 2": "GPU必需，训练需要16GB+显存",
        "Fish Speech": "GPU推荐，语音克隆需要少量音频样本",
        "OpenAI/Azure TTS": "无需本地GPU，API调用即可",
        "ElevenLabs": "无需本地GPU，付费API服务"
    }
    
    for model, req in requirements.items():
        print(f"• {model}: {req}")

def main():
    """主函数"""
    print("🚀 TTS模型快速开始指南")
    print("本指南帮助您选择合适的TTS模型并快速上手")
    
    # 检查环境
    setup_environment()
    
    # 模型选择指南
    model_selection_guide()
    
    # API使用示例
    api_usage_example()
    
    # 资源需求
    resource_requirements()
    
    print("\n" + "="*60)
    print("🎯 下一步行动建议")
    print("="*60)
    print("1. 根据您的需求选择合适模型")
    print("2. 查看对应模型的详细文档")
    print("3. 准备所需的环境和资源")
    print("4. 从简单示例开始测试")

if __name__ == "__main__":
    main()
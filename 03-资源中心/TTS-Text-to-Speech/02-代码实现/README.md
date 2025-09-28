# 代码实现

## 基础TTS实现

### 传统方法
- **基于HMM的TTS**
- **基于DNN的TTS**

### 现代神经TTS
- **Tacotron系列** (Tacotron, Tacotron2)
- **WaveNet声码器**
- **FastSpeech系列** (FastSpeech, FastSpeech2)
- **VITS** (端到端TTS)

## 项目结构

```
代码实现/
├── 基础实现/           # 简单的TTS模型
├── Tacotron系列/       # Tacotron相关实现
├── FastSpeech系列/     # FastSpeech相关实现
├── 声码器/            # 神经声码器实现
├── 端到端模型/        # VITS等端到端方法
└── 工具脚本/          # 数据处理和评估脚本
```

## 依赖环境

- Python 3.8+
- PyTorch 1.9+
- Librosa
- NumPy
- SciPy
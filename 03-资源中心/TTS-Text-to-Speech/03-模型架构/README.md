# 模型架构

## 主要TTS模型架构

### 1. Tacotron系列
- **Tacotron**: 基于注意力机制的端到端TTS
- **Tacotron2**: 改进的Tacotron + WaveNet声码器

### 2. WaveNet系列
- **WaveNet**: 自回归波形生成模型
- **Parallel WaveNet**: 并行的WaveNet变体

### 3. FastSpeech系列
- **FastSpeech**: 非自回归TTS模型
- **FastSpeech2**: 改进的FastSpeech

### 4. 端到端模型
- **VITS**: 变分推理+端到端TTS
- **Glow-TTS**: 基于流的TTS模型

## 架构对比

| 模型 | 生成方式 | 推理速度 | 音质 | 复杂度 |
|------|----------|----------|------|--------|
| Tacotron | 自回归 | 慢 | 高 | 中等 |
| FastSpeech | 非自回归 | 快 | 高 | 中等 |
| VITS | 端到端 | 中等 | 很高 | 高 |
| WaveNet | 自回归 | 很慢 | 极高 | 高 |

## 技术特点

### 自回归模型
- 逐个生成音频样本
- 音质高但速度慢
- 适合高质量合成

### 非自回归模型
- 并行生成整个序列
- 速度快但需要更多训练数据
- 适合实时应用

### 端到端模型
- 简化训练流程
- 减少人工特征工程
- 需要大量高质量数据
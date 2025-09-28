# 阿里云百炼平台 · 通义千问语音合成(TTS)模型

## 📊 模型概览与计费

| 项目 | 详情 |
| :--- | :--- |
| **产品名称** | 通义千问语音合成模型 (Tongyi Qianwen TTS) |
| **服务平台** | 阿里云 · 大模型服务平台百炼 |
| **推荐模型** | **Qwen3-TTS** (相比旧版 Qwen-TTS，音色更多，语种更广) |
| **当前版本** | `qwen3-tts-flash` (稳定版) |
| **定价** | **0.8元 / 万字符** |
| **最大输入** | 600 字符 |
| **免费额度** | 每个支持的语种各 **2000 字符** (百炼开通后90天内有效) |

---

## 🚀 功能与技术规格

### 核心特性对比

| 功能特性        | Qwen3-TTS                      | 备注                               |
| :---------- | :----------------------------- | :------------------------------- |
| **接入方式**    | Python SDK, Java SDK, HTTP API |                                  |
| **流式输出**    | **支持**                         | 以 Base64 编码的 PCM 格式实时返回音频数据      |
| **流式输入**    | 不支持                            | 旧版 `Qwen-TTS Realtime API` 支持此功能 |
| **合成音频格式**  | WAV                            |                                  |
| **音频采样率**   | **24kHz**                      |                                  |
| **时间戳**     | 不支持                            |                                  |
| **声音复刻**    | 不支持                            |                                  |
| **SSML 支持** | 不支持                            |                                  |

### 语言支持
- **支持语言**: 中文（含多种方言）、英、法、德、俄、意、西、葡、日、韩等
- **总计**: 10+ 种主流语言
- **特色**: 远超旧版的语言覆盖范围

### 重要提示
1. **音频文件 URL 有效期**: **24小时**
2. **输入格式**: 暂不支持 Markdown 格式输入

---

## 💻 API 调用与开发

### 核心调用接口
```python
import dashscope
from dashscope import MultiModalConversation

# 核心调用接口
response = MultiModalConversation.call(
    model="qwen3-tts-flash",
    text="要合成的文本",
    voice="音色名称",
    language_type="语言类型"
)
```

### 关键请求参数
| 参数 | 说明 | 示例 |
| :--- | :--- | :--- |
| `model` | 模型名称 | `"qwen3-tts-flash"` |
| `text` | 要合成的文本 | `"你好，这是一个TTS测试"` |
| `voice` | 音色名称 | `"Cherry"` (芊悦) |
| `language_type` | 建议与文本语种一致 | `"zh"` (中文) |
| `stream` | 流式/非流式 | `True` (流式) / `False` (非流式) |

### SDK 版本要求
- **Python**: `dashscope >= 1.24.6`
- **Java**: `dashscope >= 2.21.9`

---

## 🎙️ 支持的音色列表 (Qwen3-TTS)

总计 **17种** 高度拟人化的音色，覆盖标准普通话、多种方言及特色音。

### 普通话音色
| 音色名 | `voice` 参数 | 描述 |
| :--- | :--- | :--- |
| **芊悦** | `Cherry` | 阳光积极、亲切自然小姐姐 |
| **晨煦** | `Ethan` | 阳光、温暖、活力的北方口音男生 |
| **不吃鱼** | `Nofish` | 不会翘舌音的设计师 |
| **甜茶** | `Ryan` | 节奏拉满，戏感炸裂，张力十足 |
| **卡捷琳娜** | `Katerina` | 御姐音色，韵律回味十足 |
| **墨讲师** | `Elias` | 严谨又不失生动的知识型讲师 |
| **詹妮弗** | `Jennifer` | 品牌级、电影质感般美语女声 |

### 方言特色音色
| 音色名 | `voice` 参数 | 方言/特色 | 描述 |
| :--- | :--- | :--- | :--- |
| **四川-程川** | `Eric` | 四川话 | 跳脱市井的成都男子 |
| **上海-阿珍** | `Jada` | 上海话 | 风风火火的沪上阿姐 |
| **北京-晓东** | `Dylan` | 北京话 | 北京胡同里长大的少年 |
| **四川-晴儿** | `Sunny` | 四川话 | 甜到心里的川妹子 |
| **南京-老李** | `li` | 南京话 | 耐心的瑜伽老师 |
| **陕西-秦川** | `Marcus` | 陕西话 | 心实声沉的老陕 |
| **闽南-阿杰** | `Roy` | 闽南语 | 诙谐直爽的台湾哥仔 |
| **天津-李彼得** | `Peter` | 天津话 | 专业捧哏的天津相声演员 |
| **粤语-阿强** | `Rocky` | 粤语 | 幽默风趣的阿强 |
| **粤语-阿清** | `Kiki` | 粤语 | 甜美的港妹闺蜜 |

---

## 🔧 实用示例代码

### Python 基础调用示例
```python
import dashscope
from dashscope import MultiModalConversation

# 设置API密钥
dashscope.api_key = 'your-api-key'

def tts_synthesize(text, voice='Cherry', language='zh'):
    """语音合成基础调用"""
    response = MultiModalConversation.call(
        model='qwen3-tts-flash',
        text=text,
        voice=voice,
        language_type=language
    )
    
    if response.status_code == 200:
        # 获取音频URL
        audio_url = response.output.audio_url
        print(f"合成成功，音频URL: {audio_url}")
        return audio_url
    else:
        print(f"合成失败: {response.message}")
        return None

# 使用示例
audio_url = tts_synthesize("你好，欢迎使用通义千问语音合成服务", voice="Eric")
```

### 流式输出示例
```python
def tts_streaming(text, voice='Cherry'):
    """流式语音合成"""
    response = MultiModalConversation.call(
        model='qwen3-tts-flash',
        text=text,
        voice=voice,
        stream=True
    )
    
    for chunk in response:
        if chunk.status_code == 200:
            # 处理流式音频数据
            audio_data = chunk.output.audio_data
            # 解码Base64并播放/保存
            print("收到音频数据块")
```

---

## 📈 竞争优势分析

### 成本优势
- **定价**: 0.8元/万字符，相比其他云服务商有显著价格优势
- **免费额度**: 每个语种2000字符，适合测试和小规模使用

### 技术特色
- **方言支持**: 目前方言支持最全面的商业TTS服务
- **流式输出**: 低延迟实时音频生成
- **多语言**: 覆盖10+主流语言

### 适用场景
- **方言应用**: 需要多种方言支持的项目
- **成本敏感**: 大规模文本转语音应用
- **阿里云生态**: 已在阿里云平台的项目

---


*最后更新: 2025-09-28*
# SSML (Speech Synthesis Markup Language) 高级控制指南

## 📋 SSML 基础与用法

| 项目 | 描述 |
| :--- | :--- |
| **定义** | SSML 是一种基于 XML 的标记语言，用于精细控制语音合成的输出效果。 |
| **核心作用** | 控制发音、语速、音量、停顿、多音字、数字/日期/货币读法，甚至可以添加背景音乐和情感。 |
| **基本规则** | 1. 所有需要使用 SSML 的文本都必须包裹在 `<speak>` 和 `</speak>` 标签内。<br>2. 标签内的文本如包含特殊字符 (`<`, `>`, `&`, `"`, `'`) 需要进行转义。 |
| **使用方式** | 将包含 SSML 标签的整个字符串作为语音合成接口的 `text` 参数值进行传递。 |

---

## 🎛️ 核心标签 `<speak>` 的全局控制属性

`<speak>` 标签作为根元素，可以通过设置其属性来对整段语音进行全局配置，优先级高于 API 请求中的同名参数。

| 属性 | 功能描述 | 示例值 / 注意事项 |
| :--- | :--- | :--- |
| `voice` | **指定发音人**。 | `voice="siyue"` <br>**注意：** 在百炼平台调用时，此参数对应的是 `model` 参数。 |
| `rate` | **调节语速**。正数加快，负数减慢。 | `rate="150"` <br>**注意：** 在百炼平台调用时，范围为 `[0.5, 2]`，代表实际倍速。 |
| `pitch` | **调节音高**。正数升高，负数降低。 | `pitch="-100"` <br>**注意：** 在百炼平台调用时，范围为 `[0.5, 2]`，代表实际音高。 |
| `volume` | **调节音量**。 | `volume="80"` (范围 [0, 100]，默认 50) |
| `encodeType` | **指定音频格式**。 | `encodeType="mp3"` (可选 PCM/WAV/MP3) |
| `sampleRate` | **指定音频采样率**。 | `sampleRate="24000"` (可选 8000/16000/24000/48000) |
| `effect` | **添加音效**。 | `effect="robot"` (可选：机器人、萝莉、回声等) |
| `bgm` | **添加背景音乐**。 | `bgm="http://.../bgm.wav"` (值为一个音频文件的 URL) |
| `backgroundMusicVolume` | **调节背景音乐音量**。 | `backgroundMusicVolume="30"` |

---

## 🔧 内容控制与结构标签

这些标签用于处理文本内部的结构、停顿和发音。

| 标签 | 功能描述 | 关键属性 & 示例 |
| :--- | :--- | :--- |
| `<break>` | **插入停顿**。 | `time="500ms"` 或 `time="2s"`。 |
| `<emotion>` | **指定情感** (仅支持多情感发音人)。 | `category="happy"`， `intensity="1.5"`。 |
| `<phoneme>` | **指定多音字/词的拼音**。 | `<phoneme alphabet="py" ph="he2 bao1">钱包</phoneme>` |
| `<s>` | **标记句子**，用于辅助引擎理解文本结构。 | `<s>这是第一句。</s><s>这是第二句。</s>` |
| `<sub>` | **文本替换**，读出 `alias` 属性的内容。 | `<sub alias="万维网联盟">W3C</sub>` |
| `<w>` | **强制分词**，用于处理分词歧义。 | `南京市长<w>江大桥</w>` |
| `<soundEvent>` | 在语音中**插入提示音** (如"叮咚"声)。 | `src="http://.../dingdong.wav"` |

---

## 💬 `<say-as>` 标签：指定文本内容的读法

这是 SSML 中最强大和复杂的标签之一，用于告诉引擎如何"理解"和"朗读"特定类型的文本。

| `interpret-as` 属性值 | 用途 | 示例 |
| :--- | :--- | :--- |
| `cardinal` | **读作基数** (数值)。 | `<say-as interpret-as="cardinal">123</say-as>` -> "一百二十三" |
| `digits` | **读作单个数字**。 | `<say-as interpret-as="digits">123</say-as>` -> "一二三" |
| `telephone` | **按电话号码习惯朗读**。 | `<say-as interpret-as="telephone">13812345678</say-as>` -> "幺三八 幺二三四 五六七八" |
| `date` | **按日期格式朗读**。 | `<say-as interpret-as="date">2024-01-01</say-as>` -> "二零二四年一月一日" |
| `time` | **按时间格式朗读**。 | `<say-as interpret-as="time">14:30</say-as>` -> "十四点三十分" |
| `currency` | **按货币金额朗读**。 | `<say-as interpret-as="currency">¥199.5</say-as>` -> "一百九十九点五元" |
| `measure` | **按度量单位朗读**。 | `<say-as interpret-as="measure">10kg</say-as>` -> "十千克" |
| `characters` | **逐个读出字符**。 | `<say-as interpret-as="characters">ABC</say-as>` -> "A B C" |
| `address` | **按地址习惯朗读**。 | `<say-as interpret-as="address">3号楼2单元</say-as>` -> "三号楼二单元" |
| `name` | **按人名习惯朗读** (处理多音字姓氏等)。 | `<say-as interpret-as="name">解晓东</say-as>` |
| `id` | **按ID/昵称习惯朗读** (中英文数字混合)。 | `<say-as interpret-as="id">user_007</say-as>` -> "U S E R 下划线 零 零 七" |

---

## 🎭 特殊用途标签

| 标签 | 功能描述 | 关键属性 & 示例 |
| :--- | :--- | :--- |
| `<vhml>` | **虚拟人标记语言**。用于在语音流中插入一个标记，该标记的时间戳会返回给客户端，用于**驱动虚拟人做出相应的表情或动作**，但本身不发声。 | `<vhml src="wink_eye"/>` |

---

## 💻 实用代码示例

### Python SSML 基础使用
```python
import dashscope
from dashscope import MultiModalConversation

# 设置API密钥
dashscope.api_key = 'your-api-key'

def synthesize_with_ssml(text_with_ssml):
    """使用SSML进行语音合成"""
    response = MultiModalConversation.call(
        model='qwen3-tts-flash',
        text=text_with_ssml
    )
    
    if response.status_code == 200:
        return response.output.audio_url
    else:
        print(f"合成失败: {response.message}")
        return None

# SSML 示例：控制语速和情感
ssml_content = """
<speak rate="120" pitch="+50" voice="siyue">
    <s>大家好，欢迎使用SSML高级控制功能。</s>
    <break time="500ms"/>
    <s>我可以精确控制语音的每一个细节。</s>
    <emotion category="excited" intensity="1.2">
        这真是太棒了！
    </emotion>
</speak>
"""

audio_url = synthesize_with_ssml(ssml_content)
```

### 数字和日期读法控制
```python
# 数字和日期读法示例
ssml_numeric = """
<speak>
    电话号码：<say-as interpret-as="telephone">13812345678</say-as>
    金额：<say-as interpret-as="currency">¥199.5</say-as>
    日期：<say-as interpret-as="date">2024-01-01</say-as>
    数字：<say-as interpret-as="digits">123</say-as>
</speak>
"""
```

### 多音字和专有名词处理
```python
# 多音字和专有名词处理
ssml_pronunciation = """
<speak>
    这个<phoneme alphabet="py" ph="zhong4">重</phoneme>要的会议
    将在<phoneme alphabet="py" ph="chong2">重</phoneme>庆举行。
    
    网址：<say-as interpret-as="characters">www.w3c.org</say-as>
    名称：<sub alias="万维网联盟">W3C</sub>
</speak>
"""
```

---

## 🎯 最佳实践指南

### 1. 停顿控制
- 使用 `<break time="500ms"/>` 在句子间添加自然停顿
- 对于列表项，在每项后添加适当的停顿

### 2. 情感表达
- 仅在支持多情感的发音人上使用 `<emotion>` 标签
- 合理设置情感强度，避免过度夸张

### 3. 数字和单位
- 对于电话号码，使用 `telephone` 类型确保正确读法
- 对于金额和日期，指定正确的格式类型

### 4. 特殊字符转义
- 在 SSML 中使用 `<` 和 `>` 等特殊字符时进行转义
- 使用 `&lt;` 代替 `<`，`&gt;` 代替 `>`

### 5. 背景音乐
- 背景音乐音量通常设置为 20-30，避免掩盖语音
- 确保背景音乐 URL 可访问且格式支持

---

## 📊 SSML 与其他平台对比

| 特性 | 阿里云 SSML | 其他平台 SSML |
| :--- | :--- | :--- |
| **方言支持** | ⭐⭐⭐⭐⭐ (全面) | ⭐⭐⭐ (有限) |
| **情感控制** | ⭐⭐⭐⭐ (支持多情感) | ⭐⭐⭐ (基础) |
| **背景音乐** | ⭐⭐⭐⭐ (支持) | ⭐⭐ (部分支持) |
| **虚拟人集成** | ⭐⭐⭐⭐ (VHML支持) | ⭐ (较少) |
| **文档完整性** | ⭐⭐⭐⭐⭐ (详细) | ⭐⭐⭐ (基础) |

---

**注意**: 文档中的更新时间为 `2025-04-18`，这是一个未来的日期，可能为文档模板的预设。

*最后更新: 2025-09-28*
import torch
import torch.nn as nn
import numpy as np
import librosa

class SimpleTTS(nn.Module):
    """简单的TTS模型实现"""
    
    def __init__(self, vocab_size, hidden_dim=256, mel_dim=80):
        super(SimpleTTS, self).__init__()
        
        # 文本编码器
        self.embedding = nn.Embedding(vocab_size, hidden_dim)
        self.encoder = nn.LSTM(hidden_dim, hidden_dim, batch_first=True)
        
        # 解码器
        self.decoder = nn.LSTM(hidden_dim, hidden_dim, batch_first=True)
        self.mel_output = nn.Linear(hidden_dim, mel_dim)
        
    def forward(self, text_input):
        # 文本编码
        embedded = self.embedding(text_input)
        encoded, _ = self.encoder(embedded)
        
        # 生成梅尔频谱
        mel_outputs = []
        for i in range(encoded.size(1)):
            decoded, _ = self.decoder(encoded[:, i:i+1, :])
            mel = self.mel_output(decoded.squeeze(1))
            mel_outputs.append(mel)
            
        mel_spectrogram = torch.stack(mel_outputs, dim=1)
        return mel_spectrogram

def text_to_mel(text, model, vocab):
    """文本转梅尔频谱"""
    # 文本预处理
    tokens = [vocab.get(char, 0) for char in text]
    tokens_tensor = torch.tensor([tokens], dtype=torch.long)
    
    # 模型推理
    with torch.no_grad():
        mel = model(tokens_tensor)
    
    return mel.squeeze().numpy()

if __name__ == "__main__":
    # 示例使用
    vocab = {'<pad>': 0, '<unk>': 1, ' ': 2, 'a': 3, 'b': 4, 'c': 5}
    model = SimpleTTS(len(vocab))
    
    text = "hello world"
    mel = text_to_mel(text, model, vocab)
    print(f"生成的梅尔频谱形状: {mel.shape}")
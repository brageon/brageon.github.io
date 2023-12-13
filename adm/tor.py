import math, torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
class Transformer(nn.Module):
    def __init__(self, input_size, output_size, num_heads, num_layers, hidden_size, dropout):
        super(Transformer, self).__init__()
        self.embedding = nn.Embedding(input_size, hidden_size)
        self.position_encoding = PositionalEncoding(hidden_size, dropout)
        self.encoder = nn.ModuleList([EncoderLayer(hidden_size, num_heads, hidden_size * 4, dropout) for _ in range(num_layers)])
        self.decoder = nn.ModuleList([DecoderLayer(hidden_size, num_heads, hidden_size * 4, dropout) for _ in range(num_layers)])
        self.fc = nn.Linear(hidden_size, output_size)
    def forward(self, src):
        embedded = self.embedding(src)
        encoded = self.position_encoding(embedded)
        for layer in self.encoder:
            encoded = layer(encoded)
        for layer in self.decoder:
            decoded = layer(encoded, encoded)
        output = self.fc(decoded)
        return output
class PositionalEncoding(nn.Module):
    def __init__(self, hidden_size, dropout, max_len=5000):
        super(PositionalEncoding, self).__init__()
        self.dropout = nn.Dropout(p=dropout)
        pe = torch.zeros(max_len, hidden_size)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, hidden_size, 2).float() * (-math.log(10000.0) / hidden_size))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0).transpose(0, 1)
        self.register_buffer('pe', pe)
    def forward(self, x):
        x = x + self.pe[:x.size(0), :]
        return self.dropout(x)
class EncoderLayer(nn.Module):
    def __init__(self, hidden_size, num_heads, ff_size, dropout):
        super(EncoderLayer, self).__init__()
        self.multihead_attention = MultiHeadAttention(hidden_size, num_heads, dropout)
        self.ffn = FeedForwardNetwork(hidden_size, ff_size, dropout)
        self.dropout = nn.Dropout(p=dropout)
        self.layer_norm = nn.LayerNorm(hidden_size)    
    def forward(self, x):
        attended = self.multihead_attention(x, x, x)
        attended = self.dropout(attended)
        attended = self.layer_norm(attended + x)     
        ffn_output = self.ffn(attended)
        ffn_output = self.dropout(ffn_output)
        output = self.layer_norm(ffn_output + attended)     
        return output
class DecoderLayer(nn.Module):
    def __init__(self, hidden_size, num_heads, ff_size, dropout):
        super(DecoderLayer, self).__init__()        
        self.self_attention = MultiHeadAttention(hidden_size, num_heads, dropout)
        self.encoder_attention = MultiHeadAttention(hidden_size, num_heads, dropout)
        self.ffn = FeedForwardNetwork(hidden_size, ff_size, dropout)
        self.dropout = nn.Dropout(p=dropout)
        self.layer_norm = nn.LayerNorm(hidden_size)
    def forward(self, x, encoded):
        self_attended = self.self_attention(x, x, x)
        self_attended = self.dropout(self_attended)
        self_attended = self.layer_norm(self_attended + x)       
        attended = self.encoder_attention(self_attended, encoded, encoded)
        attended = self.dropout(attended)
        attended = self.layer_norm(attended + self_attended)        
        ffn_output = self.ffn(attended)
        ffn_output = self.dropout(ffn_output)
        output = self.layer_norm(ffn_output + attended)       
        return output
class MultiHeadAttention(nn.Module):
    def __init__(self, hidden_size, num_heads, dropout):
        super(MultiHeadAttention, self).__init__()        
        self.hidden_size = hidden_size
        self.num_heads = num_heads      
        self.head_size = hidden_size // num_heads        
        self.linear_query = nn.Linear(hidden_size, hidden_size)
        self.linear_key = nn.Linear(hidden_size, hidden_size)
        self.linear_value = nn.Linear(hidden_size, hidden_size)        
        self.linear_out = nn.Linear(hidden_size, hidden_size)       
        self.dropout = nn.Dropout(p=dropout)    
    def forward(self, query, key, value):
        batch_size = query.size(0)        
        query = self.linear_query(query).view(batch_size, -1, self.num_heads, self.head_size).transpose(1, 2)
        key = self.linear_key(key).view(batch_size, -1, self.num_heads, self.head_size).transpose(1, 2)
        value = self.linear_value(value).view(batch_size, -1, self.num_heads, self.head_size).transpose(1, 2)        
        scores = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(self.head_size)
        scores = F.softmax(scores, dim=-1)        
        attn_output = torch.matmul(self.dropout(scores), value)       
        attn_output = attn_output.transpose(1, 2).contiguous().view(batch_size, -1, self.hidden_size)        
        output = self.linear_out(attn_output)      
        return output
class FeedForwardNetwork(nn.Module):
    def __init__(self, hidden_size, ff_size, dropout):
        super(FeedForwardNetwork, self).__init__()     
        self.linear1 = nn.Linear(hidden_size, ff_size)
        self.linear2 = nn.Linear(ff_size, hidden_size)       
        self.dropout = nn.Dropout(p=dropout)    
    def forward(self, x):
        x = F.relu(self.linear1(x))
        x = self.dropout(x)
        x = self.linear2(x)
        return x
input_size = 100  
output_size = 10  #  number of classes
num_heads = 4
num_layers = 2
hidden_size = 256
dropout = 0.1
input_sequence = ["our", "cineplasty", "with", "teroxide", "hallowedly", "eyeball"]
word_to_index = {}
for i, word in enumerate(input_sequence):
    word_to_index[word] = i
input_indices = [word_to_index[word] for word in input_sequence]
input_tensor = torch.tensor([input_indices], dtype=torch.long)
model = Transformer(input_size, output_size, num_heads, num_layers, hidden_size, dropout)
output = model(input_tensor)
print(output.shape)

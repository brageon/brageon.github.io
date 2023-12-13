'''
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("tokens/roberta")
vocab = tokenizer.get_vocab()
print(vocab)
'''
from transformers import pipeline
model = pipeline(model="tokens/roberta", task="text-generation")
input_text = ["our, cineplasty, with, teroxide, hallowedly, eyeball",
              "another schochat phthalimide lycanthropy salted cinenchyma",
              "tezkere another cinene discerning hallowedly macaw",
              "another elf could lycanthropize from discarnation"]
output = model(input_text, max_length=50, num_return_sequences=4)
for i, sentence in enumerate(output):
    print(f"Output {i+1}: {sentence['generated_text']}")
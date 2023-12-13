from transformers import pipeline
model = pipeline("text-generation", model="../neo-model")
input_text = "teroxide hallowedly our cineplasty eyeball"
output = model(input_text, max_length=50, num_return_sequences=5)
for i, sentence in enumerate(output):
    print(f"Output {i+1}: {sentence['generated_text']}")
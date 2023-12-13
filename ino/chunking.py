import os, shutil
def chunk_file(input_file, num_chunks, chunk_size):
  output_folder = os.path.splitext(input_file)[0] + "vi"
  os.makedirs(output_folder, exist_ok=True)
  with open(input_file, 'r') as f:
    text = f.read()
  words = text.split()
  chunks = []
  for i in range(0, len(words), chunk_size):
    chunks.append(words[i:i + chunk_size])
  for i, chunk in enumerate(chunks):
    output_file = os.path.join(output_folder, "v" + str(i + 1) + ".txt")
    with open(output_file, 'w') as f:
      f.write(' '.join(chunk))
if __name__ == "__main__":
  input_file = "nu.txt"   
  num_chunks = 32
  chunk_size = 4212
  chunk_file(input_file, num_chunks, chunk_size)

def get_words(file_path, start_index, end_index):
  with open(file_path, "r") as f:
    contents = f.read()
  words = contents.split()
  return words[start_index:end_index]
if __name__ == '__main__':
  file_path = "gui/v9u.txt"
  star, den = 3188, 3206
  words = get_words(file_path, star, den)
  print(words) #TGT JZJ AGA
'''
File: v22u.txt  (2860, 2872) (3754, 3766)
File: v11u.txt  (2974, 2986), (3117, 3129)
File: v9u.txt  (2888, 2900) (3191, 3203)
'''

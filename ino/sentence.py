import os, subprocess
def combine_outputs(output1, output2):
  combined_output = []
  for i in range(len(output1)):
    if i % 2 == 0:
      combined_output.append(output1[i])
    else:
      combined_output.append(output2[i])
  return combined_output
def run_scripts():
  output1 = subprocess.run(["python", "rano.py"], capture_output=True).stdout.decode("utf-8").split("\n")
  output2 = subprocess.run(["python", "gaussian.py"], capture_output=True).stdout.decode("utf-8").split("\n")
  combined_output = combine_outputs(output1, output2)
  #print("Combined output:")
  for line in combined_output:
    print(line)
if __name__ == "__main__":
  run_scripts()

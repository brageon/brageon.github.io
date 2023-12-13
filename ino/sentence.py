'''
nuvi/v8.txt 5000 words done to genc.txt
thousands: 4, 2, 5, 3, 2, 2, 2, 4, 5, 2, 7, 2, 4, 3, 3, 2, 2.2, 2, 3.5, 1.1, 3, 2, 5, 3, 2.2
'''
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
  output1 = subprocess.run(["python", "gen.py"], capture_output=True).stdout.decode("utf-8").split("\n")
  output2 = subprocess.run(["python", "gen2.py"], capture_output=True).stdout.decode("utf-8").split("\n")
  combined_output = combine_outputs(output1, output2)
  #print("Combined output:")
  for line in combined_output:
    print(line)
if __name__ == "__main__":
  run_scripts()

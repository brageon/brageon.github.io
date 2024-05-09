import re, os, cv2, boto3, botocore
yn = True
class botox:
  def __init__(self, bool):
    pass
  def get(self, filename="login/cred"):
    with open(filename, "r") as file:
      for line in file:
        match = re.match(r"(aws_access_key_id|aws_secret_access_key)\s*=\s*(.*)", line.strip())
        if match:
          key, value = match.groups()
          if key == "aws_access_key_id":
            access_key_id = value
          elif key == "aws_secret_access_key":
            secret_access_key = value
          else:
            raise ValueError("Unexpected key found in credentials file")
      return access_key_id, secret_access_key
  def setup(self):
    dex, rex = self.get()
    return boto3.setup_default_session(region_name="eu-north-1", aws_access_key_id=dex, aws_secret_access_key=rex)
if __name__ == "__main__":
  if yn:    
    bot = botox(yn)
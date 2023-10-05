import os

def append_notice(file_path, notice):
  with open(file_path, "r") as f:
    # Check if the file ends with a blank line
    if f.read()[-1] != "\n":
      # Append a blank line to the file
      with open(file_path, "a") as f_append:
        f_append.write("\n")
    # Append the notice to the file
    with open(file_path, "a") as f_append:
      f_append.write(notice)

if __name__ == "__main__":
  notice = """
**CLIFFORDX SOSYAL-MEDYAS**
- My legal bai blog: https://cliffordx.github.io/legalbai/
- Youtube: https://youtube.com/cliffordenoc
- Facebook: https://facebook.com/cliffordx
- Twitter: https://x.com/cliffordx
"""
  for root, dirs, files in os.walk("."):
    for file in files:
      if file.endswith(".txt"):
        file_path = os.path.join(root, file)
        append_notice(file_path, notice)
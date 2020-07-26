from tqdm import tqdm
from odf import opendocument, text, teletype
import glob

FILE_NAME = 'COMPILED_SONGS.txt'

def write_text(text):
  with open(FILE_NAME, "a") as f:
    f.write(text)
    f.write('\n')

with open(FILE_NAME, 'w') as f:
  #initialize to empty file
  f.write('')

# List down all the files
file_list = glob.glob('./*.odp')

for f in tqdm(file_list):
  doc = opendocument.load(f)
  file_content = []
  # get text information
  for item in doc.getElementsByType(text.Span):
      s = teletype.extractText(item)
      file_content.append(s)

  remove = ['', u'\xa0', '<number>', '\t', ' ', '\n']

  for idx, line in enumerate(file_content):
    # if last line of the file, write an additional newline
    if idx == len(file_content) - 1:
      write_text('\n')

    # If it's the 2nd or 3rd line, possibly a blank line after
    # artist name or song name, so write a -------- to symbolize header
    if idx == 1 or idx == 2:
      if line in remove:
        write_text('-------------')
        continue

    # Ignore lines that are mentioned in the remove list
    if line in remove:
      continue

    # Write these lines for lyrics
    write_text(line)

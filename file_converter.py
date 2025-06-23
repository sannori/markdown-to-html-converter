import sys
import markdown

inputfile = sys.argv[2]
outputfile = sys.argv[3]

with open(inputfile) as file:
    md_text = file.read()
    html = markdown.markdown(md_text)
    
with open(outputfile, "w") as file:
    file.write(html)

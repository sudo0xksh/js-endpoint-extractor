import requests
import sys
import re
from urllib.parse import urljoin

print("=========================================")
print("Simple JS Endpoint Extractor\n")

args = sys.argv

if "-u" not in args:
    print("Usage: python js_extract.py -u <url> [-o output.txt]")
    sys.exit(1)

url = args[args.index("-u") + 1]

output_file = None
if "-o" in args:
    output_file = args[args.index("-o") + 1]

response = requests.get(url)
html = response.text

js_files = re.findall(r'<script.*?src=["\'](.*?\.js)["\']', html)

js_urls = []
for js in js_files:
    js_urls.append(urljoin(url, js))

endpoints = set()

for js_url in js_urls:
    try:
        r = requests.get(js_url)
        js_code = r.text

        found = re.findall(r'\/(api|v1|v2)\/[a-zA-Z0-9_\/\-]+', js_code)

        for f in found:
            endpoints.add("/" + f)
    except:
        pass

if output_file:
    with open(output_file, "w") as f:
        for e in endpoints:
            f.write(e + "\n")
    print("Saved endpoints to", output_file)
else:
    print("\nEndpoints found:")
    for e in endpoints:
        print(e)

print("\n=========================================")
print("Done")
print("Developed by sudo_0xksh")

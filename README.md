# Random JSON Generator

Steps:

1. Install dependencies per requirements.txt
2. Run this script : genFakeJson.py

```
Usage:
genFakeJson.py [-h] -d DEPTH -c COUNT -o OUTPUTDIR

arguments:
  -h, --help [Optional]: show this help message and exit
  -d DEPTH, --depth DEPTH : How deeply nested you would like the result JSON to be
  -c COUNT, --count COUNT : How many JSON documents would you like to generate
  -o OUTPUTDIR, --outputDir OUTPUTDIR : An absolute path on local filesystem where the output JSON files will be saved
```

Example :  python3 genFakeJson.py -d 7 -c 20 -o /tmp/json

The above command is going to generate 20 json files, each file with maximum depth of 7 and save all the generated json file to /tmp/json



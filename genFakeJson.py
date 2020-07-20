import sys
import argparse
import os
import random
import simplejson as json
#import json

from jsonGenerator import createNestedObj as c

jsonGenerators = [c.create_top_level_obj, c.create_nested_obj, c.create_nested_array]


def check_path(absPath):
    if(not os.path.isdir(absPath)):
        print("Unable to locate output directory. Please check path and try again : {}".format(absPath))
        sys.exit("EXITING... output directory path not found on filesystem")
    else:
        print("Found output dir : {}".format(absPath))
    return absPath


def generate_json(depth, count, outdir):
    for x in range(count):
        jsonDoc = random.choice(jsonGenerators)(depth)
        jsonFileName = outdir + '/fakeJson' + str(x) + '.json'
        with open(jsonFileName, 'w') as f:
            json.dump(jsonDoc, f, ensure_ascii=False, indent=4)
        #print('Written file {}'.format(jsonFileName))


def main():
    parser = argparse.ArgumentParser(description="Process all command line arguments")
    parser.add_argument('-d', '--depth', type=int, required=True, dest='depth',
                        help='How deeply nested you would like the result JSON to be')
    parser.add_argument('-c', '--count', type=int, required=True, dest='count',
                        help='How many JSON documents would you like to generate')
    parser.add_argument('-o', '--outputDir', type=str, required=True, dest='outputDir',
                        help='An absolute path on local filesystem where the output JSON files will be saved')
    args = parser.parse_args()
    depth = args.depth
    count = args.count
    output_dir = check_path(args.outputDir)
    print("------- Generating {} JSON files with maximum depth of {} . Please wait...".format(count, depth))
    generate_json(depth, count, output_dir)
    #jsonDoc = c.create_nested_obj(depth)
    #print(json.dumps(jsonDoc))
    print("--- All done ---")


if __name__ == '__main__':
    main()

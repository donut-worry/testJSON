import sys
import argparse
import os

from jsonGenerator import createNestedObj as c


def check_path(absPath):
    if(not os.path.isdir(absPath)):
        print("Unable to locate output directory. Please check path and try again : {}".format(absPath))
        sys.exit("EXITING... output directory path not found on filesystem")
    else:
        print("Found output dir : {}".format(absPath))
    return absPath


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
    outputDir = check_path(args.outputDir)

    print(c.create_nested_obj(depth))


if __name__ == '__main__':
    main()

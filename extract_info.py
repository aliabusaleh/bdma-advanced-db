from resume_parser import resumeparse
data_result = []
import json
# import required module
import os
# assign directory

def start_extracting(directory, output_file):
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            data_result.append(resumeparse.read_file(os.path.join(subdir, file)))

    with open(output_file, 'w') as f:
        json.dump(data_result, f+".txt")


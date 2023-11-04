import csv
import glob
import re

with open('test.csv', 'w') as file:
    writer = csv.writer(file)
    fields = ['date', 'P1Name', 'P2Name', 'P1WinProb', 'P2WinProb']
    writer.writerow(fields)
    for file in glob.glob('./out/*.txt'):
        if '.py' in file:
            continue
        print(file)

        filename = file.split('/')[-1]
        date = filename.split('_')[0]
        p1 = filename.split('_')[1]
        p2 = filename.split('_')[3].split('.')[0]

        with open(file) as f:
            input_string = f.read()
            # Define a regular expression pattern to match the probabilities
        pattern = r"\[([\d.]+), ([\d.]+)\]"

        # Use re.search to find the first match in the string
        match = re.search(pattern, input_string)

        # Extract the probabilities as floats
        if match:
            probability = (float(match.group(1)) + float(match.group(2))) / 2
        else:
            print("Probabilities not found in the input string.")

        print(date,p1,p2,probability,1-probability)
        writer.writerow([date,p1,p2,probability,1-probability])
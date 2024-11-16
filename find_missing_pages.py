# read a csv file in data dir
import csv
file = "data/neighborhoods-2024.csv"

# read the csv file, and skip the header row
with open(file, 'r') as f:
    reader = csv.reader(f)
    next(reader)
    # create a list of lists
    data = list(reader)
    hoods: dict = {}
    for row in data:
        # stop if the row is blank
        if row[0] == '':
            break
        # Convert page numbers string to list of integers
        for row in data:
            # if the current row is blank, then break
            if row[2] == '':
                continue
            page_numbers = [int(num.strip()) for num in row[2].split(',')]
            # add the page numbers to the dictionary
            hoods[row[0]] = page_numbers
    # print the dictionary, key and value one key at a time
    # for key, value in hoods.items():
    #     print(key, value)
    
    # in total there should be pages 1 through 38
    # read through the dictionary and find the missing pages
    missing_pages = []  
    for i in range(1, 39):
        found = False
        for key, value in hoods.items():
            if i in value:
                found = True
                break
        if not found:
            missing_pages.append(i)
    # if there are missing pages, print them
    if len(missing_pages) > 0:
        print("Missing pages: ", missing_pages)

    else:
        print("No missing pages")





    

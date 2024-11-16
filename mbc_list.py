import csv, os

with open('adults.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Skip the header row
    next(reader)

    mbc_file = 'mbc_list.csv'

    # if the file exists, delete it
    if os.path.exists(mbc_file):
        os.remove(mbc_file)

    merit_badges_file = 'merit_badges.csv'
    if os.path.exists(merit_badges_file):
        os.remove(merit_badges_file)
    
    for row in reader:
        bsa_id = row['BSA Number'].strip()
        first_name = row['First Name'].strip()
        last_name = row['Last Name'].strip()
        merit_badges = row['Merit Badges'].strip()
        
        if merit_badges:
            merit_badges_list = [badge.strip() for badge in merit_badges.split('|')]
            # print(f"{bsa_id} {first_name} {last_name}, {', '.join(merit_badges_list)}")

            

            # save each item to a new csv file called mbc_list.csv
            
            with open(mbc_file, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([bsa_id, first_name, last_name, ', '.join(merit_badges_list)])

    # read th mbc_file and print all the unique "Merit Badges" values. 
    with open(mbc_file, 'r') as file:
        reader = csv.reader(file)
        merit_badges = []
        for row in reader:
            merit_badges.extend(row[3].split(', '))
        merit_badges = list(set(merit_badges))
        merit_badges.sort()
        print('Merit Badges:')
        for badge in merit_badges:
            print(badge)
            # for each badge, create a list of people with that badge
            people_with_badge = []
            with open(mbc_file, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if badge in row[3].split(', '):
                        people_with_badge.append(f"{row[0]} {row[1]} {row[2]}")
                        print(f"{row[0]} {row[1]} {row[2]}")
            with open(merit_badges_file, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([badge, ', '.join(people_with_badge)])







                

            

            

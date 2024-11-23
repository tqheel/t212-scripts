import pandas as pd

# Read the CSV file
df = pd.read_csv('data/scouts-assigned-mbc.csv')

# Function to clean names by removing parentheses and their contents
def clean_name(value):
    if pd.isna(value):
        return value
    # Remove any text within parentheses (including the parentheses)
    # remove any extra spaces between individual words
    import re
    return re.sub(r'\s+', ' ', re.sub(r'\([^)]*\)', '', value)).strip()
# Clean both the MBC and Merit Badge columns
df['MBC'] = df['MBC'].apply(clean_name)
df['Merit Badge'] = df['Merit Badge'].apply(clean_name)

# Get unique Member ID
unique_scouts = df['Member ID'].unique()

# Create a dictionary to store results
scout_mb_dict = {}

# For each unique scout, create their merit badge dictionary
for scout_id in unique_scouts:
    # Convert numpy.int64 to regular Python int
    scout_id = int(scout_id)
    
    scout_rows = df[df['Member ID'] == scout_id]
    
    # Get scout's first and last name (taking first row since they'll be the same)
    scout_first = scout_rows['Scout First'].iloc[0]
    scout_last = scout_rows['Scout Last'].iloc[0]
    
    # Create dictionary of Merit Badge -> MBC
    mb_dict = dict(zip(scout_rows['Merit Badge'], scout_rows['MBC']))
    
    # Store in main dictionary with scout ID as key
    # Now including a tuple of (first_name, last_name, mb_dict)
    scout_mb_dict[scout_id] = (scout_first, scout_last, mb_dict)

# Example: Print results for one scout
for scout_id in list(scout_mb_dict.keys()):
    first_name, last_name, mb_dict = scout_mb_dict[scout_id]
    print(f"\nScout: {scout_id} {first_name} {last_name}")
    print("Merit Badges and Counselors:")
    for mb, counselor in mb_dict.items():
        print(f"  {mb}: {counselor if pd.notna(counselor) else 'No Counselor Assigned'}")

# Save the dictionary to a json file
import json
with open('data/scouts-mb-counselors.json', 'w') as f:
    #  if file exists, clear all contents before writing
    f.seek(0)
    # modify NaN values to empty string
    for scout_id in scout_mb_dict:
        first_name, last_name, mb_dict = scout_mb_dict[scout_id]
        for mb in mb_dict:
            if pd.isna(mb_dict[mb]):
                mb_dict[mb] = ""
        scout_mb_dict[scout_id] = (first_name, last_name, mb_dict)
    
    json.dump(scout_mb_dict, f)
    print("Dictionary saved to 'data/scouts-mb-counselors.json'")
import json
import pandas as pd

data_file = open("../../dataset/Yelp/yelp_academic_dataset_business.json")
data = []

for line in data_file:
    data.append(json.loads(line))
checkin_df = pd.DataFrame(data)

data_file.close()

print(checkin_df)
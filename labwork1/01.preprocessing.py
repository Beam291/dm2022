import itertools
import json
import pandas as pd

# data_file = open("../../dataset/Yelp/yelp_academic_dataset_review.json")
# data = []

# nb_lines = 3

# df = pd.read_json("../../dataset/Yelp/yelp_academic_dataset_review.json", lines=True, chunksize=1)
# for chunk in df:
#    print(chunk)
   
review_file = open("../../dataset/Yelp/yelp_academic_dataset_review.json")
for line in itertools.islice(f,3):
  line = line.strip()
  if not line: continue
  print(json.loads(line))

review_file.close()

# for line in data_file:
#     data.append(json.loads(line))
# checkin_df = pd.DataFrame(data)

# #close the data_file
# data_file.close()

# column_name = list(checkin_df)

# print(column_name)

# N = 3
# with open("../../dataset/Yelp/yelp_academic_dataset_review.json") as f:
#     for i in range(0, N):
#         data.append(json.loads(i))
#         # print(f.readline(), end = '')
#     f.close
# checkin_df = pd.DataFrame(data)
# print(checkin_df)
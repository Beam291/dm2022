import itertools
import json
import pandas as pd

#open review file
review_file = open("../../dataset/Yelp/yelp_academic_dataset_review.json")
data = []

#Because json file too heavy so only read 3 first lines
for line in itertools.islice(review_file,3):
  line = line.strip()
  if not line: continue
  data.append(json.loads(line))
  
#DataFrame of review_file
review_df = pd.DataFrame(data)

#close the review_file
review_file.close()
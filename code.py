import pandas as p


data1 = p.read_csv("Project139/csv file/shared_articles.csv")

data2 = p.read_csv("Project139/csv file/users_interactions.csv")


data1 = data1[data1['eventType'] == "CONTENT SHARED"]

print(data1.shape)

print(data2.shape)

def totalEvents(data1_row):
  total_likes = data2[(data2["contentId"] == data1_row["contentId"]) & (data2["eventType"] == "LIKE")].shape[0]
  total_views = data2[(data2["contentId"] == data1_row["contentId"]) & (data2["eventType"] == "VIEW")].shape[0]
  total_bookmark = data2[(data2["contentId"] == data1_row["contentId"]) & (data2["eventType"] == "BOOKMARK")].shape[0]
  total_comment = data2[(data2["contentId"] == data1_row["contentId"]) & (data2["eventType"] == "COMMENT CREATED")].shape[0]
  total_follow = data2[(data2["contentId"] == data1_row["contentId"]) & (data2["eventType"] == "FOLLOW")].shape[0]

  return total_likes + total_views + total_bookmark + total_comment + total_follow


data1['total_events']= data1.apply(totalEvents, axis=1)

data1 = data1.sort_values(["total_events"], ascending = False)

print(data1.head())


























import sys
import pandas as pd

# Genres
genres = []
for i in range(1, len(sys.argv)):
    genres.append(sys.argv[i])
print(f"入力されたジャンル: {genres}")

df = pd.read_csv("recommend_data.csv")

result_df = df.copy()
for genre in genres:
    result_df = result_df[result_df["Genres"].str.contains(genre)]
result_df = result_df.sort_values("Score", ascending=False)
result_df = result_df[["Name", "Image_url", "Score"]].reset_index(drop=True)

if len(result_df) > 3:
    result_df = result_df.sample(3).reset_index(drop=True)

result_df.to_csv("recommend_result.csv", index=False)

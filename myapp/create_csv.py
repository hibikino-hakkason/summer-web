import sys
import pandas as pd

def get_movie(genres):
        
    df = pd.read_csv("recommend_data.csv")

    result_df = df.copy()
    for genre in genres:
        result_df = result_df[result_df["Genres"].str.contains(genre)]
    result_df = result_df.sort_values("Score", ascending=False)
    result_df = result_df[["Name", "Image_url", "Score"]].reset_index(drop=True)

    if len(result_df) > 3:
        result_df = result_df.sample(3).reset_index(drop=True)

    result_df.to_csv("recommend_result.csv", index=False)

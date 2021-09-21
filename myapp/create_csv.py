import sys
import pandas as pd

def get_movie(genres):
        
    df = pd.read_csv("recommend_data.csv")

    result_df = df.copy()
    for genre in genres:
        df_ = result_df.copy()
        result_df = result_df[result_df["Genres"].str.contains(genre)]
        if len(result_df) < 3:
            result_df = df_.copy()
            break

    result_df = result_df.sort_values("Score", ascending=False)
    result_df = result_df[["Name", "Image_url", "Score"]].reset_index(drop=True)
    if len(result_df) > 3:
        result_df = result_df.sample(3).reset_index(drop=True)

    print(result_df)
    result_data = []
    for i in range(3):
        result_dict = {'Name': "", 'Image_url': ""}
        result_dict["Name"] = result_df["Name"][i]
        result_dict["Image_url"] = result_df["Image_url"][i]
        result_data.append(result_dict)

    return result_data
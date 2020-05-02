import pandas as pd

def __my_func():
    data = pd.read_csv("data.csv")
    data = data[["DIAM_CIRCLE_IMAGE", "DEPTH_RIMFLOOR_TOPOG","LONGITUDE_CIRCLE_IMAGE","LATITUDE_CIRCLE_IMAGE"]]
    data["SIZE"] = data["DEPTH_RIMFLOOR_TOPOG"]*data["DIAM_CIRCLE_IMAGE"]*data["DIAM_CIRCLE_IMAGE"]
    print(data["SIZE"].value_counts())


if __name__ == "__main__":
    __my_func()
    

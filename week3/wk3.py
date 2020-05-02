import pandas as pd
import numpy as np
def __my_func():
    data = pd.read_csv("data.csv")
    data = data[["DIAM_CIRCLE_IMAGE", "DEPTH_RIMFLOOR_TOPOG","LONGITUDE_CIRCLE_IMAGE","LATITUDE_CIRCLE_IMAGE"]]

    print("depth variable")
    print(data["DEPTH_RIMFLOOR_TOPOG"].value_counts())
    data[data["DEPTH_RIMFLOOR_TOPOG"]==0.00]=0.01
    print("after data management")
    print(data["DEPTH_RIMFLOOR_TOPOG"].value_counts())
    data["SIZE"] = data["DEPTH_RIMFLOOR_TOPOG"]*data["DIAM_CIRCLE_IMAGE"]*data["DIAM_CIRCLE_IMAGE"]
    print("\n new variable")
    print(data["SIZE"].value_counts())
    #for col in data.columns:
        #print(data[col].value_counts())
    

if __name__ == "__main__":
    __my_func()
    

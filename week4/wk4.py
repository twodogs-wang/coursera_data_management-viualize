import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def __latitude_longtitude(data_L, data_R):
    plt.title("coordinates of craters")
    plt.xlabel("latitude")
    plt.ylabel("longtitude")
    plt.scatter(data_L,data_R,s=0.1)
    plt.show()
    

def __size_distribution(data):
    #data.hist()
    data.plot(kind="hist",bins=20,color="steelblue",edgecolor="black")
    plt.title("size distribution")
    plt.xlabel("size")
    plt.ylabel("amount")
    plt.show()
    print("mean",np.mean(data))
    print("median",np.nanmedian(data))




def __relationship(x,y):
    
    plt.title("depth vs diameter")
    plt.xlabel("depth")
    plt.ylabel("size")
    plt.scatter(x,y,s=0.1)
    plt.show()
    


    
def __mean_and_median(data):
    print("mean:")
    print(np.mean(data))
    print("median:")
    print(np.nanmedian(data))
    #print("mode")
    #print(np.mode(data))

    
if __name__ == "__main__":
    data = pd.read_csv("data.csv")
    data = data[["DIAM_CIRCLE_IMAGE", "DEPTH_RIMFLOOR_TOPOG","LONGITUDE_CIRCLE_IMAGE","LATITUDE_CIRCLE_IMAGE"]]
    data[data["DEPTH_RIMFLOOR_TOPOG"]==0.00]=0.1
    data["SIZE"] = data["DEPTH_RIMFLOOR_TOPOG"]*data["DIAM_CIRCLE_IMAGE"]
    for col in data.columns:
        print("------------------------------------------","\n",col)
        __mean_and_median(data[col])
    #__latitude_longtitude(data["LONGITUDE_CIRCLE_IMAGE"],data["LATITUDE_CIRCLE_IMAGE"])
    #__size_distribution(data["SIZE"])
    #print(data["SIZE"].value_counts())
    #__relationship(data["DEPTH_RIMFLOOR_TOPOG"], data["SIZE"])
    

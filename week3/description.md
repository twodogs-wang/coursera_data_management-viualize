# count missing data:

As we can see from figure below: there are no missing data in my selected variables. But there are a lot of 0s in DEPTH, which is no possible. We replace them with 0.01 for further analysis. This is because the unit of depth is kilometer, 0 means a small value but it could never be 0. This action may affect the accuracy of further actions, but we can not set it to nan since the percentage of 0s is really high!

![Xnip2020-05-01_21-15-02.jpg](https://github.com/twodogs-wang/coursera_data_management-viualize/blob/master/week3/figures/Xnip2020-05-01_21-15-02.jpg)

![Xnip2020-05-01_21-14-42.jpg](https://github.com/twodogs-wang/coursera_data_management-viualize/blob/master/week3/figures/Xnip2020-05-01_21-14-42.jpg)

![Xnip2020-05-01_21-22-38.jpg](https://github.com/twodogs-wang/coursera_data_management-viualize/blob/master/week3/figures/Xnip2020-05-01_21-22-38.jpg)

# creating new variables:

A new variable called "size" is created based on the diameter and the depth of craters

![Xnip2020-05-01_21-20-46.jpg](https://github.com/twodogs-wang/coursera_data_management-viualize/blob/master/week3/figures/Xnip2020-05-01_21-20-46.jpg)

# Frequency distribution of new variable:

based on the figure above, we observe that there are many 0s. But the sizes of craters can not be zeroes. The reason for this is there are many 0s in DEPTH column. Obviously, DEPTH can not be 0. 

we have replaced them with 0.01, so the updated will be look like below:

![Xnip2020-05-01_22-02-43.jpg](https://github.com/twodogs-wang/coursera_data_management-viualize/blob/master/week3/figures/Xnip2020-05-01_22-14-06.jpg)

# Code:

```python
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
    
```

# summary:

Frequency distributions are shown below:

![depth.png](https://github.com/twodogs-wang/coursera_data_management-viualize/blob/master/week4/figures/depth.png)

![diameter.png](https://github.com/twodogs-wang/coursera_data_management-viualize/blob/master/week4/figures/diameter.png)

![size.png](https://github.com/twodogs-wang/coursera_data_management-viualize/blob/master/week4/figures/size.png)

![L_R.png](https://github.com/twodogs-wang/coursera_data_management-viualize/blob/master/week4/figures/L_R.png)

As shown above, the craters are spread kind of evenly. In addition, the craters are mostly small size ones. In addition, if we take a look we will find that 80% of depth are 0 since the unit is km. We should replace these 0 values for further analysis.
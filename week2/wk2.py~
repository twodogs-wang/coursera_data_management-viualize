import pandas as pd

def __my_func():
    data = pd.read_csv("data.csv")
    data = data[["DIAM_CIRCLE_IMAGE", "DEPTH_RIMFLOOR_TOPOG","LONGITUDE_CIRCLE_IMAGE","LATITUDE_CIRCLE_IMAGE"]]
    for col in data.columns:
        print(data[col].value_counts())
        temp = data[col].value_counts().rename_axis(col+"unique_values").reset_index(name='counts')
        temp.to_csv(col+"_output.csv")
if __name__ == "__main__":
    __my_func()

"""
output are as follows:
1.01      6298
1.02      6077
1.03      6035
1.04      5941
1.05      5771
          ... 
115.47       1
52.90        1
65.18        1
64.82        1
65.79        1
Name: DIAM_CIRCLE_IMAGE, Length: 6240, dtype: int64

0.00    307529
0.07      2059
0.08      2047
0.09      2008
0.10      1999
         ...  
4.75         1
2.84         1
4.95         1
2.97         1
3.08         1
Name: DEPTH_RIMFLOOR_TOPOG, Length: 296, dtype: int64

-53.500     9
-50.142     8
 73.888     8
-13.731     8
-3.987      8
           ..
 158.260    1
 68.032     1
 150.858    1
-142.442    1
 148.116    1
Name: LONGITUDE_CIRCLE_IMAGE, Length: 231245, dtype: int64

-23.634    17
-2.572     16
-12.970    15
-17.317    15
-3.150     15
           ..
-47.176     1
 38.302     1
-49.988     1
 56.487     1
-63.516     1
Name: LATITUDE_CIRCLE_IMAGE, Length: 129197, dtype: int64
"""



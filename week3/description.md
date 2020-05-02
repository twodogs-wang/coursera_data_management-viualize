# count missing data:

As we can see from figure below: there are no missing data in my selected variables. But there are a lot of 0s in DEPTH, which is no possible. We replace them with nan for further analysis.

![Xnip2020-05-01_21-15-02.jpg](https://github.com/twodogs-wang/coursera_data_management-viualize/blob/master/week3/figures/Xnip2020-05-01_21-15-02.jpg)

![Xnip2020-05-01_21-14-42.jpg](https://github.com/twodogs-wang/coursera_data_management-viualize/blob/master/week3/figures/Xnip2020-05-01_21-14-42.jpg)

# creating new variables:

A new variable called "size" is created based on the diameter and the depth of craters

![Xnip2020-05-01_21-20-46.jpg](https://github.com/twodogs-wang/coursera_data_management-viualize/blob/master/week3/figures/Xnip2020-05-01_21-20-46.jpg)

# Frequency distribution of new variable:

# ![Xnip2020-05-01_21-22-38.jpg](https://github.com/twodogs-wang/coursera_data_management-viualize/blob/master/week3/figures/Xnip2020-05-01_21-22-38.jpg)

based on the figure above, we observe that there are many 0s. But the sizes of craters can not be zeroes. The reason for this is there are many 0s in DEPTH column. Obviously, DEPTH can not be 0. 

we have replaced them with nan, so the updated will be look like below:


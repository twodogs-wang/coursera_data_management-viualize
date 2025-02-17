# Week 4 assignment:

## graphs for each variable:

Mention: Since all my variables are floating numbers, mode number does not make sense.

### diameter:

In terms of diameter, we can observe that most crater are some size ones. The median and the mean of this variable is 0.1 km and 2.29 km respectively.

![diameter.png](https://github.com/twodogs-wang/coursera_data_management-viualize/blob/master/week4/figures/diameter.png)

### depth:

The mean and median of this variable is 0.15 km and 0.1 km respectively.

![depth.png](https://github.com/twodogs-wang/coursera_data_management-viualize/blob/master/week4/figures/depth.png)

Based on figures above, we can observer that the majority of craters are small ones, which is the case.

### latitude and longitude:

We can see from the picture below, craters are spread kind of evenly.

![L_R.png](https://github.com/twodogs-wang/coursera_data_management-viualize/blob/master/week4/figures/L_R.png)

### size:

The size of craters, as mentioned above, most of them are small sizes which means the distribution graph looks like "one bar". But if we look at the frequency distribution data and the relationship picture, we can observe this variable can be used to analysis relative age of mars surfaces. 

explain: since the depth & diameter are always linked together. Larger diameter means bigger meteorolite which generates higher value of depth. Therefore we can use "size" to represent the size of meteorolite.

![size.png](https://github.com/twodogs-wang/coursera_data_management-viualize/blob/master/week4/figures/size.png)

![size_data.png](https://github.com/twodogs-wang/coursera_data_management-viualize/blob/master/week4/figures/size_data.png)

![size_vs_diameter.png](https://github.com/twodogs-wang/coursera_data_management-viualize/blob/master/week4/figures/size_vs_diameter.png)

![depth_vs_diameter.png](https://github.com/twodogs-wang/coursera_data_management-viualize/blob/master/week4/figures/depth_vs_diameter.png)

## center and spread:

Variance is used to estimate the spread level:

![var.png](https://github.com/twodogs-wang/coursera_data_management-viualize/blob/master/week4/figures/var.png)

center:  centers are just medians

## Summary and conclusion:

Based on these data we can estimate the relative age of the surfaces of mars. The method is quite intuition. The surface with more bigger craters and more numbers of crater is likely older than the other surface. 

In details, we can see there is an area with high density craters which tends to be much older than the other areas. 

On the other hand, we can use the data to compare with the craters on the moon. From this comparison we could estimate the absolute age of mars surfaces since the absolute age of the moon we already known, which was achieved by carbon analysis.
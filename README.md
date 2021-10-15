# Amazon_Vine_Analysis. Project 16 of the UofT.
## `-Contents-`	
	
- [Overview of the Amazon_Vine Analysis](#Overview-of-the-Amazon_Vine-Analysis)	
- [Resources](#resources)	
- [The Amazon_Vine Statistical Analysis Result](#The-MechaCar-Statistical-Analysis-Result)
  - [Linear Regression to Predict MPG](#--Linear-Regression-to-Predict-MPG)	
  - [Summary Statistics on Suspension Coils](#--Summary-Statistics-on-Suspension-Coils)
  - [T-Test on Suspension Coils](#--T-Test-on-Suspension-Coils)
  - [Study Design: MechaCar vs Competition](#--Study-Design-MechaCar-vs-Competition)
## `Overview of the Amazon_Vine Analysis`	
	
The purpose for the the project is to perform the ETL process to extract the dataset, transform the data, connect to an AWS RDS instance, and load the transformed data into pgAdmin by using PySpark. Also, to determine if there is any bias toward favorable reviews from Vine members in the dataset by using PySpark, Pandas, SQL.

The analysis consists the following: 
- Perform ETL on Amazon Product Reviews.
- Determine Bias of Vine Reviews.
- A Written Report on the Analysis.

## `Resources`	
The analysis is created using next software: R-Studio 2.14.1, R version 4.1.1 -- "Kick Things".

## `The MechaCar Statistical Analysis Result`	
The RScript result of MechaCar Statistical Analysis can be found in the [MechaCarChallenge](./MechaCarChallenge.R) file
### `- Linear Regression to Predict MPG`	

![image](https://user-images.githubusercontent.com/68247343/136716263-418a7089-9589-40c1-a756-6bf7371808cd.png)

According to our results the variables: Intercept (5.08e-08), vehicle_length (2.60e-12), ground_clearance (5.21e-08) provide a non-random amount of variance to the mpg values in the dataset because of their pr(>|t|)< 0.05. So, they have significant impact on the mpg values.

In addition, the pr(>|t|) of our linear regression analysis is 5.08 x 10-8, which is much smaller than our assumed significance level of 0.05%. Therefore, we can state that there is sufficient evidence to reject our null hypothesis, which means that the slope of our linear model is not zero.

According to the calculated r-squared value as 0.7149 which means that roughly 71%. So, the linear model can be predicted. 

### `- Summary Statistics on Suspension Coils`	

- The total summary table shows below:

![image](https://user-images.githubusercontent.com/68247343/136715702-8d0f65d7-8e4b-4f0a-b3a4-808b797e5c4c.png)

 - The lot_summary dataframe is following:

![image](https://user-images.githubusercontent.com/68247343/136715703-693d70fc-ddba-49c4-82f4-47737787cf68.png)

Additionally, the design specifications for the MechaCar suspension coils dictate that the variance of the suspension coils must not exceed 100 pounds per square inch. So, as the variance is around 62 that means the current manufacturing data meet this design specification for all manufacturing lots in total.

But the variance of lot 3 is about 170 which means it does not meet the design specification. 
### `- T-Test on Suspension Coils`	

T-tests allows to determine if all manufacturing lots and each lot individually are statistically different from the population mean of 1,500 PSI.

According to the calculated p-value of 1 higher than 0.05 for all manufacturing lot. So, it is not right to reject the null hypothesis. The mean is 1498 which is close from the population mean.

![image](https://user-images.githubusercontent.com/68247343/136715709-59b7fcbb-103a-428f-a92c-a07a1a7815f7.png)

For the  manufacturing lot1, p-value of 1.58 x 10-11 is lower than 0.05. So, it is right to reject the null hypothesis. The mean is 1500 which is the same as the population mean.

![image](https://user-images.githubusercontent.com/68247343/136715711-b2a5d4f5-48f0-429b-ae59-e5680cc3f856.png)

For the  manufacturing lot2, p-value of 0.006 is lower than 0.05. So, it is right to reject the null hypothesis. The mean is 1500.02 which is close from the population mean.

![image](https://user-images.githubusercontent.com/68247343/136715716-33d99185-76c1-49fa-b3a4-2c8ec7069c0c.png)

For the  manufacturing lot2, p-value of 0.1589 is higher than 0.05. So, it is not right to reject the null hypothesis. The mean is 1496.14 which is close from the population mean.

![image](https://user-images.githubusercontent.com/68247343/136731523-09cdf315-170c-4f27-a3d0-3c1a7bd46658.png)

### `- Study Design - MechaCar vs Competition`	

A statistical study to compare performance of the MechaCar vehicles against performance of vehicles from other manufacturers is bellow. Consumer would be interest in several metrics as cost, city or highway fuel efficiency, horse power, maintenance cost, or safety rating.

Null hypothesis as there is no difference between the metrics of MechaCar vs competition.
Alternate hypothesis as there is a difference between the metrics of MechaCar vs competition.

To test the hypothesis should use T-test as if the p-value is less than the significance level, then the null hypothesis is rejected.

To run the statistical test needs to use data as cost, city or highway fuel efficiency, horse power, maintenance cost, safety rating. 

# Amazon Vine Analysis. Project 16 of the UofT.
## `-Contents-`	
	
- [Overview of the Amazon Vine Analysis](#Overview-of-the-Amazon-Vine-Analysis)	
- [Resources](#resources)	
- [The Amazon Vine Analysis Result](#The-MechaCar-Statistical-Analysis-Result)
  - [ETL on Amazon Product Reviews](--ETL-on-Amazon-Product-Reviews)
  - [Bias of Vine Reviews](--Bias-of-Vine-Reviews)
- [The Amazon Vine Analysis Summary](#-The-Amazon-Vine-Analysis-Summary)
## `Overview of the Amazon Vine Analysis`	
	
The purpose for the the project is to perform the ETL process to extract the dataset, transform the data, connect to an AWS RDS instance, and load the transformed data into pgAdmin by using PySpark. Also, to determine if there is any bias toward favorable reviews from Vine members in the dataset by using PySpark, Pandas, SQL.

The analysis consists the following: 
- Perform ETL on Amazon Product Reviews.
- Determine Bias of Vine Reviews.
- A Written Report on the Analysis.

## `Resources`	
The analysis is created using next software: Colaboratory (a hosted Jupyter notebook service), Visual Studio Code 1.58.0, PostgreSQL 11.12 and pgAdmin 5.5, AWS S3 and AWS RDS, Spark-3.0.3, Python 3.9.6, Pandas 1.2.4.

## `The Amazon Vine Analysis Result`
### `- ETL on Amazon Product Reviews`	

Using the cloud ETL process, the AWS RDS database with tables in pgAdmin is created and, the dataset amazon_reviews_multilingual_FR from the Amazon Review datasets is picked and extracted into a DataFrame. Also, the DataFrame is transformed into four separate DataFrames that match the table schema in pgAdmin. 

The result of the ETL on Amazon Product Reviews can be found in the [Amazon_Reviews_ETL](./Amazon_Reviews_ETL.ipynb) file.

The transformed data into the appropriate tables in pgAdmin is following:
Screens tables pgAdmin
### `- Bias of Vine Reviews`

The result of the Bias of Vine Reviews can be found in the [Vine_Review_Analysis](./Vine_Review_Analysis.ipynb) file.

According to the result of the Bias of Vine Reviews the number of Vine reviews is 18 and non-Vine reviews is ) 7652.

screen 1


Additionally, "5-star Vine" reviews and How many "5-star non-Vine" reviews are 9 and 4376 respectively.

Screen 2

Also, the percentage of "5 star Vine" reviews is 0.1%. And, the percentage of "5 star non-Vine" reviews is 57.1%.

Screen 3

## `The Amazon Vine Analysis Summary`	

According to the result of the Bias of Vine Reviews there is not any positivity bias for reviews in the Vine program or there is a

The results of the analysis shows small paid part of reviews. 
Additionally, even the count of "5-star paid of all paid" is 50% and that is less then "5-star unpaid of all unpaid" by 7.2% it can be regarded as Bias of Vine Reviews. 

screen 4

But, repeatedly paid reviews are small part of all reviews (0.2%), so there is not any positivity bias for Vine reviews.


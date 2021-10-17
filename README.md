# Amazon Vine Analysis. Project 16 of the UofT.
## `-Contents-`	
	
- [Overview of the Amazon Vine Analysis](#Overview-of-the-Amazon-Vine-Analysis)	
- [Resources](#resources)	
- [The Amazon Vine Analysis Result](#The-Amazon-Vine-Analysis-Result)
  - [ETL on Amazon Product Reviews](#--ETL-on-Amazon-Product-Reviews)
  - [Bias of Vine Reviews](#--Bias-of-Vine-Reviews)
- [The Amazon Vine Analysis Summary](#The-Amazon-Vine-Analysis-Summary)
## `Overview of the Amazon Vine Analysis`	
	
The purpose for the the project is to perform the ETL process to extract the dataset, transform the data, connect to an AWS RDS instance, and load the transformed data into pgAdmin by using PySpark. Also, to determine if there is any bias toward favorable reviews from Vine members in the dataset by using PySpark, Pandas, SQL.

The analysis consists the following: 
- Perform ETL on Amazon Product Reviews.
- Determine Bias of Vine Reviews.
- A Written Report on the Analysis.

## `Resources`	
The analysis is created using next software: Colaboratory (a hosted Jupyter notebook service), Visual Studio Code 1.58.0, PostgreSQL 11.12 and pgAdmin 5.5, AWS S3 and AWS RDS, Spark-3.0.3, Python 3.9.6.

## `The Amazon Vine Analysis Result`
### `- ETL on Amazon Product Reviews`	

Using the cloud ETL process, the AWS RDS database with tables in pgAdmin is created and, the dataset amazon_reviews_multilingual_FR from the Amazon Review datasets is picked and extracted into a DataFrame. Also, the DataFrame is transformed into four separate DataFrames that match the table schema in pgAdmin. 

The result of the ETL process on Amazon Product Reviews can be found in the [Amazon_Reviews_ETL](./Amazon_Reviews_ETL.ipynb) file.

![image](https://user-images.githubusercontent.com/68247343/137625416-ce5f6326-7926-42fb-a5ca-3b1b8c9f99ab.png)
![image](https://user-images.githubusercontent.com/68247343/137624867-cbb900b0-c755-4a7d-852b-d37eee93c3ec.png)
![image](https://user-images.githubusercontent.com/68247343/137624853-37f34836-0c4b-45cb-b926-2ce9eea68d26.png)
![image](https://user-images.githubusercontent.com/68247343/137624859-4bfce7be-05f8-4048-8f86-6aee81f81673.png)

### `- Bias of Vine Reviews`

The result of the Bias of Vine Reviews can be found in the [Vine_Review_Analysis](./Vine_Review_Analysis.ipynb) file.

According to the result of the Bias of Vine Reviews the number of Vine reviews is 18 and non-Vine reviews is 7652.

![image](https://user-images.githubusercontent.com/68247343/137624754-1328a54c-6354-49fa-bc38-c049f4fc6a13.png)

Additionally, "5-star Vine" reviews and "5-star non-Vine" reviews are 9 and 4376 respectively.

![image](https://user-images.githubusercontent.com/68247343/137624766-6f8f595a-612f-4de7-81b8-957e0ae821db.png)

![image](https://user-images.githubusercontent.com/68247343/137624772-c8782c2b-d09f-4928-b632-6f442e40ee6d.png)

Also, the percentage of "5 star Vine" reviews is 0.1%. And, the percentage of "5 star non-Vine" reviews is 57.1%.

![image](https://user-images.githubusercontent.com/68247343/137624785-ba4ec551-127e-47f5-b2f7-a3fd3c46cc38.png)

## `The Amazon Vine Analysis Summary`	

According to the result of the Bias of Vine Reviews there is not any bias toward favorable reviews from Vine members in the amazon_reviews_multilingual_FR dataset.

The results of the analysis shows small paid part of all reviews. 
But, the count of "5-star paid of all paid" is 50% and that is less than "5-star unpaid of all unpaid" by 7.2%. So, it can be regarded as positivity Bias of Vine Reviews. 

![image](https://user-images.githubusercontent.com/68247343/137624803-c5bc6c99-74dd-463c-8d9e-4c1d4c3263cb.png)

However, repeatedly, paid reviews are small part of all reviews (0.2%) so, there is not any positivity bias for Vine reviews from Vine members.

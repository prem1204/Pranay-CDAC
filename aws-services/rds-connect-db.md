# RDS Database Connection
***Here you will learn how to connect a RDS database to local database system***

***For this puprpose we will need the following:-***
1. A database created on RDS

*Note: To learn how to create a new database, click on the [link](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/aws-services/rds-create-database.md)*

2. The data base you want to connect should be up and running

![dbAvailable](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/rds/dbAvailable.PNG)

*We're going to connect RDS database instance to MySQL Workbench which is already installed on local system. Follow the given steps to connect*

1. In the MySQL Workbench Click on Setup new Connection,
2. Give the Connection name and Select the Connection method as Standard TCP/IP,
3. Enter the host name from RDS end point and port as 3306,
4. Enter Mysql user name. 

![setupConn](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/rds/setupConn.PNG)

5. Click on "Store in vault" to add password.

![storeVault](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/rds/storeVault.PNG)

6. Enter the password as given in RDS instance creation, and click "OK"

![pass](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/rds/pass.PNG)

7. Then test the connection and click ok.

![testConn](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/rds/testConn.PNG)

8. If you get a Success message, it means that your connection was successfully established. And click on "Ok"

![success](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/rds/success.PNG)

9.  Click "Ok" and start working with your RDS Database.




# RDS Database Creation
***Here you will learn how to create a new database usind RDS***

*Follow the given steps*

1. First open aws console.
2. Click on RDS service.
3. Choose Create database.
   
   ![createDB](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/rds/createDB.PNG)

4. Choose "Standard Create" and Click on mysql.

    ![mysqlSelect](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/rds/mysqlSelect.PNG)

5. Select version of mysql.
6. In templates click on free tire.

    ![editionTemplate](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/rds/editionTemplate.PNG)

7. Give instance name.
8. Give username and password, this password will be use to connect RDS to mysql.

    ![settings](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/rds/settings.PNG)

9.  Select DB instance type as db.t2 micro only.

    ![type](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/rds/type.PNG)

10. In the Connectivity section, open Additional connectivity configuration and select public accessible yes.

    ![public](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/rds/public.PNG)

11. Choose Create database. Your new DB instance appears in the Databases list with the status Creating.

    ![createDB2](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/rds/createDB2.PNG)

12. Wait for the Status of your new DB instance to show as Available. Then choose the DB instance name to show its details.
13. In the Connectivity & security section, view the Endpoint and Port of the DB instance.
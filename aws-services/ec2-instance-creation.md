# Ec2 Instance Creation
***Here you will learn how to create a new instance in AWS EC2***

*Follow the given steps*

1. Login to AWS console.
2. Select EC2 from Compute under All Services 
   ![selectEC2](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/ec2/selectEC2.PNG)
3. In the next window click on "Launch Instance" button 
   ![clickLaunch](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/ec2/clickLaunch.PNG)
4. Choose an AMI as per your convinience. *For learning purpose it is manadatory to verify that it is "free tier eligible".* Click on Select.
   ![chooseAmi](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/ec2/chooseAmi.PNG)
5. Choose the type of instance you want to create. *For learning purpose it is manadatory to verify that it is "free tier eligible".* So we will choos type as **"t2.micro"**. It has 1 CPU and 1GB memory. Then click on "Next:Configure Instance Details"
   ![chooseType](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/ec2/chooseType.PNG)
6. Next we need to configure some instance details such as subnet, VPC etc. As of now we will leave it as default and click on "Next: Add Storage"
   ![instanceDetails](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/ec2/instanceDetails.PNG)
7. Next, we need to add storage. For linux we have 8gb default and for windows we have 30gb default. We can change the size as per our requirement. Click on "Next: Add Tags"
   ![storage](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/ec2/storage.PNG)
8. Now we will add some tags for our instance. Click on "Add Tag" as shown below
   ![clickAddTag](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/ec2/clickAddTag.PNG)
   Next, we need to give key and value for our tags. Once that is done, we can either click on "Add More Tags" or "Next: Configre Security Group"
   ![AddTag](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/ec2/AddTag.PNG)
9.  Next we will add a new Security group. So we will provide name and description. By default we have type SSH and port 22 as we've selected linux ami. Click on "Review and Launch"
    ![sg](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/ec2/sg.PNG)
10. Now we will review our instance and click "Launch"
    ![review](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/ec2/review.PNG)
11. Now we need to choose a key pair that will be used for accessing our instance. As of now we will create a new key pair. Click on "Download Key Pair". It will download a new keypair. Make sure to keep this key pair in a safe location as it is very important while accessing our instance. 
    *Note: If this key pair is lost we won't be able to access our instance.*
    ![launchFinal](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/ec2/launchFinal.PNG)
12. Here you can view status of your instance. Now click on "View Instance"
    ![status](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/ec2/status.PNG)
13. Now you can see that your instance has been created and running. After clicking on your instance name you will be able to see all the instance details.
    ![instanceCreated](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/ec2/instanceCreated.PNG)

***Conclusion***
*We've learnt to create a new instance on AWS EC2*

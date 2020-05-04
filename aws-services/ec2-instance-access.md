# Ec2 Instance Creation
***Here you will learn how to access an instance in AWS EC2***
***For this puprpose we will need the following:-***
1. An instance created on EC2, up and running. 
   *Note: [Click here](https://github.com/prem1204/Pranay-Assignments/blob/aws-services/ec2-instance-creation.md) to learn how to create a new instance on EC2*
2. Download and install Mobaxterm

*Follow the given steps to access ec2 instance*
1. Login to you AWS account
2. Goto EC2 instances
3. Right click on the instance you want to connect and access
4. Goto instance state -> and click start. 
    [start](https://github.com/prem1204/Pranay-Assignments/blob/images/start/start.PNG)
5. Some time later your instance state will be change from stopped to running. Verify status check has been changed to "2/2 checks passed"
   [chkStatus](https://github.com/prem1204/Pranay-Assignments/blob/images/start/checkStatus.PNG)
6. Copy the IP highlighted in above image. We will use this IP to connect to our instance
7. Open Mobaxterm application (or any other application like mtputty etc)
   1. Click on session to start a new session
   2. A new window will open. Select "SSH" as we intend to connect to a linux OS
   3. Paste the IP address we copied from the instance in "Remote Host"
   4. Tick on the checkbox in front of "Specify Username" and give username as "ec2-user"
   5. Click on "Use Prive Key" checkbox and navigate to the "<filename>.pem" file which we downloaded while creating instance. This file contains private key pair.
   6. Now click on "OK"
   [connect](https://github.com/prem1204/Pranay-Assignments/blob/images/start/connect.PNG)
8. Now, we've connected to our EC2 instance.
   [connected](https://github.com/prem1204/Pranay-Assignments/blob/images/start/connected.PNG)

***Conclusion***
*We've learnt how to access any instance on AWS EC2*
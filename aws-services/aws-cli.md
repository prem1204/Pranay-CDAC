# AWS CLI

***Here you will learn how to manage AWS services using aws-cli***

***For this puprpose we will need the following:-***
1. AWS Services access
2. Policies attached to IAM Roles
3. IAM Roles attached to the services that will be managed by cli
4. AWS-CLI configured on the system

*NOTE:CLick on the [link](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) if you dont know hot to configure AWS-CLI on your system*

***Following are the cli commands we can use***

## EC2

1. Describe instance - Get complete information of given instance id

![describeInstance](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/aws-cli/describeInstance.PNG)

2. Describe instance status - Shows the state of the instance whether running or pending

![describeInstanceStatus](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/aws-cli/describeInstanceStatus.PNG)

3. Start instances - Starts the instance of given instance id. The current state changes to "pending" as shown below. After some time if we check the status again, it will changed to "running" as shown in step 2

![startInstance](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/aws-cli/startInstance.PNG)

4. Stop instances - Stops the instance of given instance id. The current state changes to "stopping" as shown below.

![stopInstance](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/aws-cli/stopInstance.PNG)

5. Describe instance status (of stopped instance)- Shows empty InstanceStatus which means that the instance od given id is in stopped state

![stoppedInstance](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/aws-cli/stoppedInstance.PNG)

6. Run instances - This will create/launch a new instance. We need to pass image id, count, instance-type, key-name and security-groups as these are mandatory for creating new instance. You will see the following output. After some time repeat step 2 and pass the instance id generated in image below to check whether the instance is running or not.

![runInstance](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/aws-cli/runInstance.PNG)

## S3

1. S3 mb - Cretes a new bucket on S3

![mb](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/aws-cli/mb.PNG)

2. S3 ls - List of all the buckets in S3.

![lsBucket](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/aws-cli/lsBucket.PNG)

3. S3 ls recursive - List of all the files and folders in S3 in a recursive manner

![lsBucketRec](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/aws-cli/lsBucketRec.PNG)

4. S3 cp - Copies files from local system and uploads it to the S3 bucket

![cp](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/aws-cli/cp.PNG)

5. S3 rm - Remove file from S3 bucket

![rm](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/aws-cli/rm.PNG)

6. S3 sync - Synchronises the S3 bucket with/in local directory

![sync](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/aws-cli/sync.PNG)

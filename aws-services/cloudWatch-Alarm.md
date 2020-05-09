# Amazon Cloud Watch

## Here you will learn how to create Amazon Cloud Watch Alarm

1. Login to AWS console 
2. Click services and select CloudWatch
3. Click on Alarm and select "Create Alarm"
4. Select Metric as "EC2" or any other service you want
5. Now select Instance name, and the name of the metric you want to publish and click "Select Metric"

![selectMetric](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/cloudwatch/Alarm/selectMetric.PNG)

6. Specify the condition as shown and click "Next"

![condition](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/cloudwatch/Alarm/condition.PNG)

7. Configure Notification and select SNS Topic you've created and click "Next" 

![notification](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/cloudwatch/Alarm/notification.PNG)

*Note: To know how to create an SNS topic click [here](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/aws-services/createSNS.md)*

8. Now give name and description and click "Next"

![nameDesc](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/cloudwatch/Alarm/nameDesc.PNG)

9. Check the Preview and click "Create ALarm" and your alarm should be created.
10. Once the alarm status is changed to Alarm state you will receive an email that you've subscribed  with while creating SNS Topic
11. You can even choose what you intend to do with the instance when an ALarm is triggered. E.g stop the instance, teminate the intance etc
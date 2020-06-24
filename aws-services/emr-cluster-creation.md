# EMR Cluster Creation
***Here you will learn how to create a new cluster in AWS EMR*** 

*Follow the given steps*

1. Login to AWS console.
2. Click on Services and search for EMR. Select EMR and click on 'Create Cluster'.
3. In Cluster configuration, we need to provide name of our cluster, Application that we'll be using (Core in our case). In Hardware Configuration we will select type of instance as m4.large, and No. of Instances as 1. In Security Access, we'll select a key pair to ssh into the emr instance. Finally we will click on *Create Cluster*
   ![clusterConfig](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/emr/cluster_configuration.PNG)

4. Cluster creation will take approx 10 minutes to get into running state.
5. Once the cluster is in Waiting state, this means that the cluster is now ready to use. 
   ![waiting](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/emr/waiting.PNG)
6. Now click on Hardware to get our instance details and copy your public ip to access you Master Node. 
7. Add SSH rule to Master security group in case you are unable to ssh.
   ![waiting](https://github.com/prem1204/Pranay-Assignments/blob/aws-cloud/images/emr/ssh.PNG)
   

***Conclusion***
*We've learnt to create a new cluster in AWS EMR and logging into Master Node*
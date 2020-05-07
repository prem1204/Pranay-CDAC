# AWS Assignment Lambda

***Q1.*** *What is AWS Lambda?*

**Ans:**

AWS Lambda is an Amazon serverless computing system that runs code and automatically manages the underlying computing resources. It lets a person automatically run code in response to many types of events, such as HTTP requests from Amazon API gateway, table updates in Amazon DynamoDB, and state transitions. It also enables the person to extend to other AWS services with custom logic, and even create its own back-end services.

**Q2.*** What are the advantages of AWS Lambda?

**Ans:**

1. It doesn’t require the user to manage any servers: Since AWS Lambda automatically runs user’s code, there’s no need for the user to manage the server. Simply write the code and upload it to Lambda.

2. It empowers the user to easily scale: AWS Lambda runs code in response to each trigger, so user’s application is automatically scaled. The code also runs in parallel processes, each triggered individually, so scaling is done precisely with the size of the workload.

3. It’s affordable: With AWS Lambda, one doesn’t pay anything when code isn’t running. The user has to only be charged for every 100ms of code execution and the number of times his code is actually triggered.
# LAB 1 -> Using HDFS Commands

***Objective -> To become familiar with how files are added to and removed from HDFS and how to view files in HDFS.***

***Pre-requisites -> Hadoop cluster on EMR should be up and running***

Following are the steps to be performed in this lab:-

1. View the hdfs dfs Command
   ![dfs](https://github.com/prem1204/Pranay-Assignments/blob/Big-Data/images/emr/hdfs/dfs.PNG)

2. Create a Directory in HDFS
   
   1. Run the -ls command to list content of root HDFS folder
        ![dfs_ls](https://github.com/prem1204/Pranay-Assignments/blob/Big-Data/images/emr/hdfs/dfs_ls.PNG)

   2. Create a directory named test in HDFS
        ![dfs_create](https://github.com/prem1204/Pranay-Assignments/blob/Big-Data/images/emr/hdfs/dfs_create.PNG)

   3. Verify that the folder was created successfully 
        ![dfs_ls_test](https://github.com/prem1204/Pranay-Assignments/blob/Big-Data/images/emr/hdfs/dfs_ls_test.PNG)

   4. Create a couple of subdirectories for test 
        ![dfs_create_sub](https://github.com/prem1204/Pranay-Assignments/blob/Big-Data/images/emr/hdfs/dfs_create_sub.PNG)

   5. To recursively view the contents of a folder, use -ls -R
        ![dfs_ls_sub](https://github.com/prem1204/Pranay-Assignments/blob/Big-Data/images/emr/hdfs/dfs_ls_sub.PNG)

3. Delete a Directory
   
   1. Delete the test2 folder (and recursively, its subcontents) using the -rm -R command
        ![dfs_rm](https://github.com/prem1204/Pranay-Assignments/blob/Big-Data/images/emr/hdfs/dfs_rm.PNG)

   2. Now run the -ls -R command
        ![dfs_ls_rm](https://github.com/prem1204/Pranay-Assignments/blob/Big-Data/images/emr/hdfs/dfs_ls_rm.PNG)

4. Upload a File to HDFS
   
   1. Change directories to /home/hadoop/labs/Lab2.1
        ![cd](https://github.com/prem1204/Pranay-Assignments/blob/Big-Data/images/emr/hdfs/cd.PNG)

   2. Notice this folder contains a file named data.txt
        ![tail](https://github.com/prem1204/Pranay-Assignments/blob/Big-Data/images/emr/hdfs/tail.PNG)

   3. Run the following -put command to copy data.txt into the test folder in HDFS
        ![dfs_put](https://github.com/prem1204/Pranay-Assignments/blob/Big-Data/images/emr/hdfs/dfs_put.PNG)

   4. Verify that the file is in HDFS by listing the contents of test
        ![dfs_ls_put](https://github.com/prem1204/Pranay-Assignments/blob/Big-Data/images/emr/hdfs/dfs_ls_put.PNG)

5. Copy a file in hdfs
   
   1. Now copy the data.txt file in test to another folder in HDFS using the -cp command
        ![dfs_cp](https://github.com/prem1204/Pranay-Assignments/blob/Big-Data/images/emr/hdfs/dfs_cp.PNG)

   2. Verify that the file is in both places by using the -ls -R command on test
        ![dfs_ls_cp](https://github.com/prem1204/Pranay-Assignments/blob/Big-Data/images/emr/hdfs/dfs_ls_cp.PNG)

   3. Now delete the data2.txt file using the -rm command
        ![dfs_rm_data2](https://github.com/prem1204/Pranay-Assignments/blob/Big-Data/images/emr/hdfs/dfs_rm_data2.PNG)

6. View the Contents of a File in HDFS
   
   1. You can use the -cat command to view text files in HDFS
        ![dfs_cat](https://github.com/prem1204/Pranay-Assignments/blob/Big-Data/images/emr/hdfs/dfs_cat.PNG)

   2. You can also use the ‐tail command to view the end of a file
        ![dfs_tail_data](https://github.com/prem1204/Pranay-Assignments/blob/Big-Data/images/emr/hdfs/dfs_tail_data.PNG)

7. Getting a File from HDFS
   
   1. use the get command to copy test/data.txt from HDFS into local /tmp folder
        ![dfs_get](https://github.com/prem1204/Pranay-Assignments/blob/Big-Data/images/emr/hdfs/dfs_get.PNG)

8. The *getmerge* Command
   
   1. Put the file /root/devph/labs/demos/small_blocks.txt into the test folder in HDFS. You should now save two files in test: data.txt and small_blocks.txt
        ![dfs_put_small_blocks](https://github.com/prem1204/Pranay-Assignments/blob/Big-Data/images/emr/hdfs/dfs_put_small_blocks.PNG)

   2. Run the following getmerge command
        ![dfs_getmerge](https://github.com/prem1204/Pranay-Assignments/blob/Big-Data/images/emr/hdfs/dfs_getmerge.PNG)

   3. What did the previous command do? Did you open the file merged.txt to see what happened?

        **Answer:** The two files that were in the test folder in HDFS were merged into a single file and stored on the local file system.

9. Specify the Block Size and Replication Factor
   1.  Put /root/devph/labs/Lab2.1/data.txt into /user/root in HDFS, giving it a blocksize of 1,048,576 bytes. 
   
    **Hint** The blocksize is defined using the dfs.blocksize property on the command line.
    
    **Answer:**
        ![dfs_blocksize](https://github.com/prem1204/Pranay-Assignments/blob/Big-Data/images/emr/hdfs/dfs_blocksize.PNG)

   2. Run the following fsck command on data.txt
        ![dfs_fsck](https://github.com/prem1204/Pranay-Assignments/blob/Big-Data/images/emr/hdfs/dfs_fsck.PNG)

   3. How many blocks are there for this file?

        **Answer:** The file should be broken down into two blocks.



***Result -> You should now be comfortable with executing the various HDFS commands, including creating directories, putting files into HDFS, copying files out of HDFS, and deleting files and folders.***
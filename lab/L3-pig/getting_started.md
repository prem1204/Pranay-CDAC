# LAB -> Getting Started with Pig

***Objective -> Use Pig to navigate through HDFS and explore a dataset.***

***Pre-requisites -> Hadoop cluster on EMR should be up and running***

Following are the steps to be performed in this lab:-

1. View Raw Data
   1. SSH to your EMR cluster
   2. Unzip whitehouse_visits.zip

    ![unzip](../../images/pig/getting_started/unzip.PNG)

   3. View contents of this file

    ![tail](../../images/pig/getting_started/tail.PNG)

2. Load data into HDFS
    1. Start grunt shell

    ![start_grunt](../../images/pig/getting_started/start_grunt.PNG)

    2. Create new directory named whitehouse

    ![mkdir_whitehouse](../../images/pig/getting_started/mkdir_whitehouse.PNG)

    3. Copy whitehouse_visits.txt file to this directory

    ![copyFromLocal](../../images/pig/getting_started/copyFromLocal.PNG)

    4. Use ls command to verify whether file was successfully uplaoded

    ![ls_whitehouse](../../images/pig/getting_started/ls_whitehouse.PNG)

3. Define a Relation
    1. Use TextLoader to load visits.txt file. Define a LOAD relation 

    ![load](../../images/pig/getting_started/load.PNG)

    2. Use 'Describe A'. You will notice that there is no schema present in A

    ![describe_a_unknown](../../images/pig/getting_started/describe_a_unknown.PNG)

    3. Use LIMIT operator to define a new relation named A_limit that is limited to 10 records of A

    ![a_limit](../../images/pig/getting_started/a_limit.PNG)

    4. Use DUMP operator to view A_limit relation

    ![dump_a_limit](../../images/pig/getting_started/dump_a_limit.PNG)

4. Define a Schema
    1. Load whitehouse data again, but this time we use PigStorage loader and define a partial schema 

    ![load_b](../../images/pig/getting_started/load_b.PNG)

    2. Use 'Describe B' to view the schema

    ![describe_b](../../images/pig/getting_started/describe_b.PNG)

5. The STORE command
    1. Use STORE command, which stores the B relation into a folder named whouse_tab and seperates the fields of each record with tabs 

    ![store_b](../../images/pig/getting_started/store_b.PNG)

    ![store_b_success](../../images/pig/getting_started/store_b_success.PNG)

    2. Verify that whouse_tab folder was created. You should see 2 mapped output files.

    ![ls_whouse_tab](../../images/pig/getting_started/ls_whouse_tab.PNG)

    3. View one of the output files to veriy they contain the B relation in a tab-delimited format

    ![fs_tail_whouse_tab_part_0000](../../images/pig/getting_started/fs_tail_whouse_tab_part_0000.PNG)

    4. Each record should contain seven fields. What happened to the rest of the fields from the raw data that was loaded from whitehouse/visits.txt?

        ***Answer***: They were simply ignored when each record was read in from HDFS.

6. Use a different Storer
    1. In the previous step, you stored a relation using PigStorage with a tab delimiter. Enter the following command, which stores the same relation but in a JSON format: 

    ![store_b_json](../../images/pig/getting_started/store_b_json.PNG)

    ![store_b_json_success](../../images/pig/getting_started/store_b_json_success.PNG)

    2. Verify that whouse_json folder was created

    ![ls_whouse_json](../../images/pig/getting_started/ls_whouse_json.PNG)

    3. View one of the output files

    ![fs_tail_whouse_json_part_0000](../../images/pig/getting_started/fs_tail_whouse_json_part_0000.PNG)


***Result -> You have now seen how to execute some basic Pig commands, load data into a relation, and store a relation into a folder in HDFS using different formats.***

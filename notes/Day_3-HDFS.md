# DAY 3 -> HADOOP DISTRIBUTED FILE SYSTEM (HDFS)

## Hadoop Distributed File System (HDFS)

The Hadoop Distributed File System (HDFS) is a distributed file system designed to run on commodity hardware. It has many similarities with existing distributed file systems. However, the differences from other distributed file systems are significant. HDFS is highly fault-tolerant and is designed to be deployed on low-cost hardware. HDFS provides high throughput access to application data and is suitable for applications that have large data sets. HDFS relaxes a few POSIX requirements to enable streaming access to file system data. HDFS was originally built as infrastructure for the Apache Nutch web search engine project. HDFS is now an Apache Hadoop subproject.

## HDFS Architecture

HDFS has a master/slave architecture. An HDFS cluster consists of a single NameNode, a master server that manages the file system namespace and regulates access to files by clients. In addition, there are a number of DataNodes, usually one per node in the cluster, which manage storage attached to the nodes that they run on. HDFS exposes a file system namespace and allows user data to be stored in files. 

Internally, a file is split into one or more blocks and these blocks are stored in a set of DataNodes. The NameNode executes file system namespace operations like opening, closing, and renaming files and directories. It also determines the mapping of blocks to DataNodes. 

The DataNodes are responsible for serving read and write requests from the file system’s clients. 

The DataNodes also perform block creation, deletion, and replication upon instruction from the NameNode.

   ![hdfs](images/hdfsarchitecture.gif)

The NameNode and DataNode are pieces of software designed to run on commodity machines. These machines typically run a GNU/Linux operating system (OS). HDFS is built using the Java language; any machine that supports Java can run the NameNode or the DataNode software. Usage of the highly portable Java language means that HDFS can be deployed on a wide range of machines. A typical deployment has a dedicated machine that runs only the NameNode software. Each of the other machines in the cluster runs one instance of the DataNode software. The architecture does not preclude running multiple DataNodes on the same machine but in a real deployment that is rarely the case.

The existence of a single NameNode in a cluster greatly simplifies the architecture of the system. The NameNode is the arbitrator and repository for all HDFS metadata. The system is designed in such a way that user data never flows through the NameNode.


## Anatomy of writing and reading file in HDFS

HDFS – Hadoop Distributed File System is the storage layer of Hadoop. It is most reliable storage system. HDFS works in master-slave fashion, NameNode is the master daemon which runs on the master node, DataNode is the slave daemon which runs on the slave node.

HDFS follow Write once Read many models. So we cannot edit files already stored in HDFS, but we can append data by reopening the file. In Read-Write operation client first, interact with the NameNode. NameNode provides privileges so, the client can easily read and write data blocks into/from the respective datanodes.

### Hadoop HDFS Data Write Operation

1. The HDFS client sends a create request on DistributedFileSystem APIs.
2. DistributedFileSystem makes an RPC call to the namenode to create a new file in the file system’s namespace.
3. The DistributedFileSystem returns a FSDataOutputStream for the client to start writing data to. As the client writes data, DFSOutputStream splits it into packets, which it writes to an internal queue, called the data queue. The data queue is consumed by the DataStreamer, which is responsible for asking the namenode to allocate new blocks by picking a list of suitable datanodes to store the replicas.
4. The list of datanodes form a pipeline, and here we’ll assume the replication level is three, so there are three nodes in the pipeline. The DataStreamer streams the packets to the first datanode in the pipeline, which stores the packet and forwards it to the second datanode in the pipeline. Similarly, the second datanode stores the packet and forwards it to the third (and last) datanode in the pipeline.
5. DFSOutputStream also maintains an internal queue of packets that are waiting to be acknowledged by datanodes, called the ack queue. A packet is removed from the ack queue only when it has been acknowledged by the datanodes in the pipeline. Datanode sends the acknowledgment once required replicas are created (3 by default). Similarly, all the blocks are stored and replicated on the different datanodes, the data blocks are copied in parallel.
6. When the client has finished writing data, it calls close() on the stream.
7. This action flushes all the remaining packets to the datanode pipeline and waits for acknowledgments before contacting the namenode to signal that the file is complete.

![Data-Write-Mechanism-in-HDFS](images/Data-Write-Mechanism-in-HDFS.gif)

### HDFS File Read Workflow

1. Client opens the file it wishes to read by calling open() on the FileSystem object, which for HDFS is an instance of DistributedFileSystem.
2. DistributedFileSystem calls the namenode using RPC to determine the locations of the blocks for the first few blocks in the file. For each block, the namenode returns the addresses of the datanodes that have a copy of that block and datanode are sorted according to their proximity to the client.
3. DistributedFileSystem returns a FSDataInputStream to the client for it to read data from. FSDataInputStream, thus, wraps the DFSInputStream which manages the datanode and namenode I/O. Client calls read() on the stream. DFSInputStream which has stored the datanode addresses then connects to the closest datanode for the first block in the file.
4. Data is streamed from the datanode back to the client, as a result client can call read() repeatedly on the stream. When the block ends, DFSInputStream will close the connection to the datanode and then finds the best datanode for the next block.
5. If the DFSInputStream encounters an error while communicating with a datanode, it will try the next closest one for that block. It will also remember datanodes that have failed so that it doesn’t needlessly retry them for later blocks. The DFSInputStream also verifies checksums for the data transferred to it from the datanode. If it finds a corrupt block, it reports this to the namenode before the DFSInputStream attempts to read a replica of the block from another datanode.vi) When the client has finished reading the data, it calls close() on the stream.

![Data-Read-Mechanism-in-HDFS](images/Data-Read-Mechanism-in-HDFS.gif)
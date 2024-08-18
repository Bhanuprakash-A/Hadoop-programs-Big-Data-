Hadoop Programs

This repository contains the lab programs developed as part of the coursework for Hadoop during the semester. The programs demonstrate the core concepts of MapReduce using Hadoop’s ecosystem, with specific examples of mapper and reducer implementations.

Repository Structure


mapper.py: Python script for the Mapper phase of the MapReduce job.

reducer.py: Python script for the Reducer phase of the MapReduce job.

dataset/: Folder containing the input dataset used for MapReduce processing.

outputfile/: Directory where the output of the MapReduce job is stored after execution.

commands.md: File containing the Hadoop commands needed to run the MapReduce jobs on Hadoop Distributed File System (HDFS).


How to Run the Programs
1. Start Hadoop and HDFS
To start Hadoop services, follow these steps:

Format the NameNode (this is required only once when setting up Hadoop for the first time):

cd C:\hadoop-2.8.0\bin
hdfs namenode -format

Start the Hadoop Distributed File System (HDFS):

cd C:\hadoop-2.8.0\sbin
start-dfs.cmd

Start YARN (Yet Another Resource Negotiator):

start-yarn.cmd

Verify that all necessary processes are running:
Use the following command to check if NameNode, DataNode, Resource Manager, and Node Manager are running:

jps
You should see output listing NameNode, DataNode, ResourceManager, and NodeManager.

2. Upload the Dataset to HDFS
Once Hadoop services are running, upload your dataset to HDFS:

3. Run the Hadoop MapReduce Job

4. View the Output
After the MapReduce job completes, you can view the results stored in HDFS:

HDFS (Hadoop Distributed File System)
HDFS is a distributed file system designed for large-scale data storage and processing. It breaks large files into blocks and distributes them across a cluster of nodes, providing:

Fault Tolerance: Data is automatically replicated across multiple nodes to ensure redundancy.

Scalability: HDFS is highly scalable and can handle vast amounts of data by adding more nodes to the cluster.

High Throughput: It is optimized for handling large datasets, making it ideal for big data applications.


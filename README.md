# Data-Pipeline-using-AirFlow
Design and Implementation of Data Pipeline using AirFlow (Using S3 , RedShift, PostGresSql)


Introduction
  -- My responsibilities as a Data Engineer involved automating and monitoring the data warehouse ETL pipelines at Sparkify.
  -- Delivered a dynamic and high grade data pipeline, which allowed for scheduled backfilling 
  -- The automated ETL processes, analyses were executed on top of the data warehouse with Data Quality Checks

Resources:-
  -- The source data resides in S3 and needed to be processed in Sparkify's data warehouse in Amazon Redshift.
  -- The source datasets consist of CSV logs that tell about user activity in the application
  -- JSON metadata about the songs the users listen to.

Process Steps
  -- Automating the ETL pipelines through Airflow involved extracting data from S3, loading data into staging tables and transforming the data into a star schema stored in Amazon Redshift. 
  -- The data warehouse were then validated using custom analyses to detect any discrepancies in the databases. 
  -- Transformed data from various sources into a star schema optimized for the analytics team's use cases.
  -- Writing custom operators to perform tasks such as staging data, filling the data warehouse, and validation through data quality checks.
  -- Redshift Clusters, Airflow Connections.
  
Dag-Script :-
    -- The primary file in this repo is the udac_example_dag.py, which generates the DAG with all necessary tasks to read in files from S3 buckets, load into staging tables and transform into a star schema which is stored in Redshift.
    
Operators :- 
  <1> Staging Operator: 
      Using Airflow's PostgreSQL & S3 hooks, data is read and copied to staging tables in redshift.

  <2> Fact & Dimension Operators: 
      Using Airflow's PostgreSQL hook and variable SQL statements, staging data is transformed into a star schema database and stored in appropriate tables in redshift.

  <3> Data Quality Operator: 
      Using Airflow's PostgreSQL hook to access the newly transformed data, custom SQL commands are run against the tables to detect discrepancies within the newly formed data warehouse.
      
Schema ::

Fact Table  
  songplays -
      records in log data associated with song plays i.e. records with page NextSong
      songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
  
Dimension Tables
  users - 
    users in the app
    user_id, first_name, last_name, gender, level

  songs - 
    songs in music database
    song_id, title, artist_id, year, duration

  artists - 
    artists in music database
    artist_id, name, location, lattitude, longitude

  time - 
    timestamps of records in songplays broken down into specific units
    start_time, hour, day, week, month, year, weekday

# BDMA Advanced Database project
<hr>

This project is done under the BDMA first semester at Université Libre de Bruxelles

## Overview
<hr>

The project aims to understand the difference between using 
different tools for same Database technology and why we
should use one technology over another one 
when designing our database. <br>
Our application will be about matching Job postings with Job seekers.

This project is done by: <br />
* <b>Ali AbuSaleh
* Muhammad Rizwan Khalid 
* Sayyor Yusupov</b> <br/>

 Under supervision of professor <b>Esteban Zimanyi</b>


## Technology and tools used in this project
<hr>

we selected <b>Search Engines</b> 
Database technology and <b> Elasticsearch </b> and <b>OpenSearch</b>
as tools. <br> 


# Setup and Tools

<hr>

## Tools setup 
 <hr> 

### Elasticsearch setup
In order to run this project, you need to install [Elasticsearch](https://www.elastic.co/downloads/elasticsearch) 
and also [Kibana](https://www.elastic.co/downloads/kibana) on your machine, more info about running Elasticsearch on [Windows](https://www.elastic.co/guide/en/kibana/current/windows.html) or [Linux/macOS](https://www.elastic.co/guide/en/kibana/current/targz.html).

<sub>**_Note_**:  Kibana is just for visualising the data in elasticsearch <br> </sub>


### Opensearch Setup 
[//]: <> (please fill this Rizwan)


### PostgreSQL Setup
[//]: <> (please fill this Sayyor)

<hr> 

## Scripts Description
* extract data: 
in the file  [extract_info.py](extract_info.py) file, you will be able to 
extract the info from the resumes by passing 2 variables into the function
<br> &nbsp; 1. Root path directory ( the resumes' dataset)
     <br> &nbsp; 2. Output file name
 <br>
* Elasticsearch loader: 
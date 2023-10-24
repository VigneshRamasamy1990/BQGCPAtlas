## Pre-Request Instructions
   Make sure you have Mongodb cluster with defined Database and Collection that has to be used in the Kafka connector in confluent

   Make sure to create Confluent account.

   Also Create the GCP account

## Steps to create Mongodb Atlas Source
  Create the Default Environment and give clustername once you have created confluent account

  Click on the "Connectors" in the search bar type "MongoDB Atlas Source connector" then click on the connector will follow thw below steps to create the connector

    - Give topic Name then click continue
    - In Kafka credentials click "Generate API key credential"
    - In Authentication 
        * Give Mongodb Host name
        * Give username
        * Give DB password
        * Give DB name
        * Give collectionName
        * Then click on continue
    - In Configuration 
        * Output Kafka record value format : Select "AVRO"
        * In advance Configuration update : "Publish full document only" with "true"
        * Then click continue
    - In Sizing click Continue
    - In Review and launch Give the Connector_name : check same name is reflected in the JSON below then click "continue" will launch the connector

  <img width="452" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/a8161dc9-7b93-4f4e-b5f3-265e15080a5a">

  ## Steps to create Google BigQuery Sink connector

  With the created cluster in the confluent 
  
  Click on "Add Connector" button in search bar "Google BigQuery Sink connector" 

    - In Topic selection
        * Select the topic we created before then click continue
    - In Kafka credentials
        * Click on Generate Api credentials
    - In Authentication
        * Upload the GCP credential file (follow the steps of GCP credential file download)
        * Give GCP project id
        * GCP dataset
        * Click continue
    - In Configuration
        * Select "Input Kafka record value format" as "Avro"
        * In Advance configuration
            Input Kafka record key format : Avro
            Auto create tables : true
        * Click continue
    - In Sizing click continue
    - In Review and Launch Give the connector name : check same name is reflected in the json below then click "continue" will launch the soink connector

  <img width="452" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/7bfdda1d-f8ae-41bd-a4b2-8f08db43c98a">

  ## Steps to validate the Mongodb Kafka connector to sink GCP bigquery.

  Insert new record to the Mongodb Collection to which we have created the Kafka connector in confluent

  Message will be seen in the Kafka connector in Confluent

  <img width="452" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/7bfdda1d-f8ae-41bd-a4b2-8f08db43c98a">

  After three document insertion

  <img width="1510" alt="Screenshot 2023-10-24 at 12 24 44" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/223d366f-64f4-46d0-b4c8-0a9990bff502">

  Sink connector 

  <img width="1510" alt="Screenshot 2023-10-24 at 12 24 26" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/cede8b9d-57e5-4369-b6db-c77342e09e20">

  



 
      
      

          

## Pre-Request
   Mongodb cluster with defined Database and Collection that must be used in the Kafka connector in confluent.

   Confluent account.

   GCP account

   Create a Service Account:
   - Open the Google Cloud Console.
   - Select or create a GCP project.
   - In the navigation menu, go to "IAM & Admin" > "Service accounts."
   - Click the "Create Service Account" button.
   - Fill in the required information for the service account, including a name and description.
   - Choose the role(s) you want to grant to the service account (e.g., Editor, Storage Admin, etc.).
   - Click "Continue."
   - Optional: You can add users to this service account later to grant them access.
 
 Generate a Key File:
   - After creating the service account, on the "Service accounts" page, find the service account you created.
   - In the "Actions" column, click on the three vertical dots (⋮) and select "Create Key."
   - Choose the key format: JSON is recommended.
   - Click "Create" to generate the key file.
   - The JSON key file will be downloaded to your local machine

## Steps to create Mongodb Atlas Source
  Create the Default Environment and give clustername once you have created confluent account

  Click on the "Connectors" in the search bar type "MongoDB Atlas Source connector" then click on the connector will follow the below steps to create the connector.

- Give topic Name then click continue
- In Kafka credentials click "Generate API key credential."
- In Authentication 
  * Give Mongodb Host name
  * Give username
  * Give DB password
  * Give DB name
  * Give collectionName
  * Then click on continue
- In Configuration 
  * Output Kafka record value format: Select "AVRO"
  * In advance Configuration update: "Publish full document only" with "true"
  * Then click continue
- In Sizing click Continue
- In Review and launch Give the Connector name : check same name is reflected in the JSON below then click "continue" will launch the connector

<img width="452" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/a8161dc9-7b93-4f4e-b5f3-265e15080a5a">
  
  ## Steps to create Google BigQuery Sink connector

  With the created cluster in the confluent 
  
  Click on "Add Connector" button in search bar "Google BigQuery Sink connector.” 

 - In Topic selection
     * Select the topic we created before then click continue
 - In Kafka credentials
     * Click on Generate Api credentials
 - In Authentication
     * Upload the GCP credential file (GCP credential file downloaded with pre request)
     * Give GCP project id
     * GCP dataset
     * Click continue
 - In Configuration
     * Select "Input Kafka record value format" as "Avro."
     * In Advance configuration
         Input Kafka record key format: Avro
         Auto create tables: true
     * Click continue
 - In Sizing click continue
 - In Review and Launch Give the connector name: check same name is reflected in the json below then click "continue" will launch the sink connector

<img width="452" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/7bfdda1d-f8ae-41bd-a4b2-8f08db43c98a">

  ## Steps to validate the Mongodb Kafka connector to sink GCP bigquery.

  - Insert new record to the Mongodb Collection to which we have created the Kafka connector in confluent

  - Message will be seen in the Kafka connector in Confluent

     <img width="452" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/7bfdda1d-f8ae-41bd-a4b2-8f08db43c98a">

  - After three document insertion

  - Sink connector 

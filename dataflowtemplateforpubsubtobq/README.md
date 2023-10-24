## Step 1: Set Up Google Cloud Project and Enable Dataflow
  If you haven't already, sign in to your Google Cloud Console.
  
  Create a new Google Cloud project or select an existing one where you want to create the Dataflow resources.

## Step 2: Create PUB/SUB Topic
  In the Google Cloud Console, navigate to "Pub/Sub" from the left-side menu.
  
  Click on the "Topics" tab.

  Click the "Create a topic" button.

  Give your topic a name, e.g., "my-topic," and click "Create."

  Click on the use a schema option to accept the data in defined schema

  <img width="378" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/7e092f7d-178a-4da6-b8ff-39c82d033cc7">

## Step 3: - Table creation
  Table creation for the schema defined in Bigquery

  <img width="362" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/3abc3b11-f1a6-4fd0-8ebb-9a57c84422eb">

## Step 4: Create GCP Bucket
  Click on the cloud storage in the left panel

  Click on Buckets then click Create Button

  Give "Name to your bucket" then click Continue

  Choose where to store your data : Multi-region : us (multiple regions in United States) then Click on Continue

  Choose a storage class for your data : Select radio button "Set a default class" then select "Standard" radio button then click on Continue

  Choose how to control access to objects : select the check box "Enforce public access prevention on this bucket" then select "uniform" under Access control then click "Continue"

  Choose how to protect object data : Select "None" under Protection tools then click "create"

  <img width="452" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/51dc1308-918e-4906-9253-ae53f8ff2083">
  
## Step 5: Create Dataflow Job Template
  In the navigation panel in the left panel Click on Dataflow
  
  Then click Jobs
  
  Provide Job Name
  
  Provide Regional endpoint
  
  In Dataflow Template dropdown select the pubsub_subscription_to_bigquery
  
  In the required parameter feilds
   
    - inputSubscription : Give Pub/Sub input Subscription Name/Id
    - Bigquery destination table : select the table created before
    - Select the created bucket in the dropdown of the gs://temporary location or create bucket with step : 4
    - click on Run Job
    - check the Job Status it should be running

    <img width="452" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/57aa94d1-f40a-40a3-8586-f0df25df965d">


## Response of Dataflow template for PUB/Sub to BQ

Publish the data to the PUB/Sub topic will reflect in the Job graph.

<img width="452" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/4bcc49a0-525c-4280-b0c7-b4b61066242e">

Once after publish graph will reflect in the Dataflow job created as below

<img width="452" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/96880d32-6f05-408f-b736-8796f8c1dddf">

Published message will get reflected in the BigQuery destination table

<img width="452" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/0365fdc3-3dc1-4830-82e5-9b88d91de613">








  
    
  

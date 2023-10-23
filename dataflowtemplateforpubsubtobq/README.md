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

## Step 4: Create Dataflow Job Template
  In the navigation panel in the left panel Click on Dataflow
  
  Then click Jobs
  
  Provide Job Name
  
  Provide Reginad endpoint
  
  In Dataflow Template dropdown select the MongoDb to Bigquery option
  
  In the required parameter feilds
   
    - Give mongodb connection String
    - MongoDb database
    - MongoDb Collection
    - Bigquery destination table : select the table created before
    - User Option NONE
    - inputTopic : select the topic created above with schema defined
    - click on Run Job
    - check the Job Status it should be running

<img width="452" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/7d72bef2-f01f-4383-b02b-ee6e5b89d9f0">

## Response of Dataflow template for PUB/Sub to BQ

<img width="452" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/7864805a-d793-473d-b72c-7a3ed9d17d03">

Publish the data to the PUB/Sub topic will reflect in the Job graph.

<img width="452" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/d2a6b63e-c4a5-4996-946f-64ac90939e05">





  
    
  

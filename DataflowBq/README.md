## Pre-requisite
- **Create PUB/SUB Topic:**
  * In the Google Cloud Console, navigate to "Pub/Sub" from the left-side menu.
  * Click on the "Topics" tab.
  * Click the "Create a topic" button.
  * Give your topic a name, e.g., "my-topic," and click "Create."
  * Click on the use a schema option to accept the data in defined schema.
  
  ![Create PUB/SUB Topic](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/7e092f7d-178a-4da6-b8ff-39c82d033cc7)

- **Table Creation:**
  * Create a table for the schema defined in Bigquery.
  
  ![Table Creation](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/3abc3b11-f1a6-4fd0-8ebb-9a57c84422eb)

- **Create GCP Bucket:**
  * Enable it to Multi-region and set public access prevention on the bucket.
  
  ![Create GCP Bucket](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/51dc1308-918e-4906-9253-ae53f8ff2083)
  
## Create Dataflow Job Template
- In the navigation panel, click on "Dataflow" in the left panel.
- Click on "Jobs".
- Provide a Job Name.
- Select the Region.
- In the "Dataflow Template" dropdown, select "pubsub_subscription_to_bigquery".
- In the required parameter fields:
  * InputSubscription: Give Pub/Sub input Subscription Name/Id.
  * Bigquery destination table: select the table created before.
  * Select the created bucket in the dropdown of the "gs://temporary location" or create a bucket with step 4.
  * Click on "Run Job".
  * Check the Job Status; it should be running.
  
  ![Create Dataflow Job Template](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/57aa94d1-f40a-40a3-8586-f0df25df965d)

## Dataflow Template for PUB/Sub to BQ
- Publishing the data to the PUB/Sub topic will reflect in the Job graph.
  
  ![Dataflow Template for PUB/Sub to BQ](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/4bcc49a0-525c-4280-b0c7-b4b61066242e)

- Once after publishing, the graph will reflect in the Dataflow job created as below.
  
  ![Dataflow Job Graph](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/96880d32-6f05-408f-b736-8796f8c1dddf)

- Published messages will get reflected in the BigQuery destination table.
  
  ![BigQuery Destination Table](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/0365fdc3-3dc1-4830-82e5-9b88d91de613)

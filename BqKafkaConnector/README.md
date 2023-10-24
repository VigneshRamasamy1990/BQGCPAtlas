## Pre-Request

- A MongoDB cluster with a defined Database and Collection that must be used in the Kafka connector in Confluent.
- A Confluent account.
- A Google Cloud Platform (GCP) account.

### Create a Service Account:
- Open the Google Cloud Console.
- Select or create a GCP project.
- In the navigation menu, go to "IAM & Admin" > "Service accounts."
- Click the "Create Service Account" button.
- Fill in the required information for the service account, including a name and description.
- Choose the role(s) you want to grant to the service account (e.g., Editor, Storage Admin, etc.).
- Click "Continue."
- Optional: You can add users to this service account later to grant them access.

### Generate a Key File:
- After creating the service account, on the "Service accounts" page, find the service account you created.
- In the "Actions" column, click on the three vertical dots (⋮) and select "Create Key."
- Choose the key format: JSON is recommended.
- Click "Create" to generate the key file.
- The JSON key file will be downloaded to your local machine.

## Steps to Create MongoDB Atlas Source Connector

- Create the default environment and give a cluster name once you have created a Confluent account.
- Click on the "Connectors" tab.
- In the search bar, type "MongoDB Atlas Source connector," then click on the connector.
- Follow the below steps to create the connector:
  1. Give a topic name, then click continue.
  2. In Kafka credentials, click "Generate API key credential."
  3. In Authentication:
     - Provide the MongoDB Host name.
     - Provide the username.
     - Provide the DB password.
     - Provide the DB name.
     - Provide the collection name.
     - Then click continue.
  4. In Configuration:
     - Output Kafka record value format: Select "AVRO."
     - In advanced Configuration, update "Publish full document only" with "true."
     - Then click continue.
  5. In Sizing, click continue.
  6. In Review and launch, give the connector name. Check the same name is reflected in the JSON below, then click "continue" to launch the connector.

![MongoDB Atlas Source Connector](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/a8161dc9-7b93-4f4e-b5f3-265e15080a5a)

## Steps to Create Google BigQuery Sink Connector

- With the created cluster in Confluent, click on the "Add Connector" button.
- In the search bar, type "Google BigQuery Sink connector."
- Follow the below steps to create the connector:
  1. In Topic selection, select the topic we created before, then click continue.
  2. In Kafka credentials, click on "Generate API credentials."
  3. In Authentication:
     - Upload the GCP credential file (downloaded in the pre-request).
     - Provide the GCP project ID.
     - Provide the GCP dataset.
     - Click continue.
  4. In Configuration:
     - Select "Input Kafka record value format" as "Avro."
     - In Advanced configuration, update:
       - Input Kafka record key format: Avro.
       - Auto-create tables: true.
     - Click continue.
  5. In Sizing, click continue.
  6. In Review and Launch, give the connector name. Check the same name is reflected in the JSON below, then click "continue" to launch the sink connector.

![Google BigQuery Sink Connector](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/7bfdda1d-f8ae-41bd-a4b2-8f08db43c98a)

## Steps to Validate the MongoDB Kafka Connector to Sink GCP BigQuery

- Insert a new record into the MongoDB Collection to which we have created the Kafka connector in Confluent.
- The message will be seen in the Kafka connector in Confluent.

![Message in Kafka Connector](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/7bfdda1d-f8ae-41bd-a4b2-8f08db43c98a)

- After three document insertions, check the sink connector in Confluent.

## Pre-Requests
- Create a Pub/Sub Topic
  * In the Google Cloud Console, navigate to "Pub/Sub" from the left-side menu.
  * Click on the "Topics" tab.
  * Click the "Create a topic" button.
  * Give your topic a name, e.g., "my-topic," and click "Create."
  * Click on the use a schema option to accept the data in defined schema

  <img width="378" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/7e092f7d-178a-4da6-b8ff-39c82d033cc7">

- Create PUB/SUB Schema
   * Click PUB/SUB from left Panel
   * Click Schema
   * Click on Create Schema
   * Provide Schema Id (e.g : my_schema)
   * Select Schema type Avro
   * In the Text area define your schema (e.g)

        ``` bash
        {
         "type" : "record",
         "name" : "Avro",
         "fields" : [
           {
             "name" : "StringField",
             "type" : "string"
           },
           {
             "name" : "FloatField",
             "type" : "float"
           },
           {
             "name" : "BooleanField",
             "type" : "boolean"
           }
         ]
        }
        ```

        * Click create (to create schema)

        <img width="452" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/edde0645-f4c0-43a2-a57c-8b22041f3b3a">


- Create DataSet
     * Select BigQuery from the Left panel 
     * Click on create Subscription 
     * Provide a name for your subscription (e.g., "my-subscription"). 
     * Select Delivery type (Write to BigQuery) 
     * Then click on the Dataset Dropdown
     * Click create a new Dataset
     * In the opened pop-up provide unique dataset name  
     * Select the region
     * Click create

  <img width="380" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/686850e2-ba3c-4ea3-aca8-8f7a1a83c459">

- Table creation
     * Table creation for the schema defined in Bigquery
  <img width="362" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/3abc3b11-f1a6-4fd0-8ebb-9a57c84422eb">


## Step 3: Create a Pub/Sub Subscription
- From the "Topics" tab, select the topic you just created (e.g., "my-topic").

- Click on the "Create subscription" button.

- Provide a name for your subscription (e.g., "my-subscription").

- select Delivery type (Write to BigQuery)
  * Select the project
  * Select the dataset that we created before
  * Give the table Name that we created before
  * Select the Use topic schema

- Click the Create to create the subscription

<img width="438" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/1902f905-cc2f-4764-a860-2b5d10224941">

- Bigquery table

<img width="393" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/142e4dc9-5ca6-4b52-985b-4173a5fe488b">





### Create a Pub/Sub Topic
- In the Google Cloud Console, navigate to "Pub/Sub" from the left-side menu.
- Click on the "Topics" tab.
- Click the "Create a topic" button.
- Give your topic a name, e.g., "my-topic," and click "Create."
- Click on the "Use a schema" option to accept the data in a defined schema.

  ![Create a Pub/Sub Topic](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/7e092f7d-178a-4da6-b8ff-39c82d033cc7)

### Create PUB/SUB Schema
- Click "PUB/SUB" from the left panel.
- Click "Schema."
- Click "Create Schema."
- Provide Schema Id (e.g., "my_schema").
- Select Schema type "Avro."
- In the text area, define your schema.
- Click "Create" to create the schema.

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

  ![Create PUB/SUB Schema](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/edde0645-f4c0-43a2-a57c-8b22041f3b3a)

### Create DataSet
- Select "BigQuery" from the left panel.
- Click "Create Subscription."
- Provide a name for your subscription (e.g., "my-subscription").
- Select "Delivery type" as "Write to BigQuery."
- Click on the "Dataset" dropdown and click "Create a new Dataset."
- In the opened pop-up, provide a unique dataset name.
- Select the region.
- Click "Create."

  ![Create DataSet](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/686850e2-ba3c-4ea3-aca8-8f7a1a83c459)

### Table Creation
- Create a table for the schema defined in BigQuery.

  ![Table Creation](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/3abc3b11-f1a6-4fd0-8ebb-9a57c84422eb)

### Create a Pub/Sub Subscription
- From the "Topics" tab, select the topic you just created (e.g., "my-topic").
- Click on the "Create subscription" button.
- Provide a name for your subscription (e.g., "my-subscription").
- Select "Delivery type" as "Write to BigQuery."
- Select the project.
- Select the dataset you created earlier.
- Enter the table name you created earlier.
- Select "Use topic schema."
- Click "Create."

  ![Create a Pub/Sub Subscription](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/1902f905-cc2f-4764-a860-2b5d10224941)

### BigQuery Table

  ![BigQuery Table](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/142e4dc9-5ca6-4b52-985b-4173a5fe488b)




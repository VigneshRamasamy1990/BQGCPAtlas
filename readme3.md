## Step 1: Set Up Google Cloud Project and Enable Pub/Sub
If you haven't already, sign in to your Google Cloud Console.

Create a new Google Cloud project or select an existing one where you want to create the Pub/Sub resources.

## Step 2: Create a Pub/Sub Topic
In the Google Cloud Console, navigate to "Pub/Sub" from the left-side menu.

Click on the "Topics" tab.

Click the "Create a topic" button.

Give your topic a name, e.g., "my-topic," and click "Create."

## Pre-Request before creating the Subscription

## Create PUB/SUB Schema
Click PUB/SUB from left Panel

Click Schema

Click on Create Schema

Provide SchemaId (e.g : my_schema)

Select Schema type Avro

In the Text area define your schema (e.g)

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

click create (to create schema)

## Create DataSet

Select BigQuery from the Left panel



## Step 3: Create a Pub/Sub Subscription
From the "Topics" tab, select the topic you just created (e.g., "my-topic").

Click on the "Create subscription" button.

Provide a name for your subscription (e.g., "my-subscription").

select Delivery type (Write to BigQuery)
  ```bash
  Select the project
  Select the dataset
  Give the table Name
  Select the Use topic schema
```
Click the Create to create the subscription

  





## Step 1: Set Up Google Cloud Project and Enable Pub/Sub
  If you haven't already, sign in to your Google Cloud Console.
  
  Create a new Google Cloud project or select an existing one where you want to create the Pub/Sub resources.
## Step 2: Create a Pub/Sub Topic
  In the Google Cloud Console, navigate to "Pub/Sub" from the left-side menu.
  
  Click on the "Topics" tab.
  
  Click the "Create a topic" button.
  
  Give your topic a name, e.g., "my-topic," and click "Create."

## Step 3: Create a Pub/Sub Subscription
  From the "Topics" tab, select the topic you just created (e.g., "my-topic").
  
  Click on the "Create subscription" button.
  
  Provide a name for your subscription (e.g., "my-subscription").
  
  Configure other settings, such as acknowledging mode and delivery type, as per your requirements.
  
  Click "Create" to create the subscription.

## Step 4: Application uses Pub/Sub in listening Collection level change stream document
  A collection-level change stream in MongoDB allows you to monitor and capture changes occurring in a specific collection. You can use this feature to track changes to documents within that collection.

  Format the message that has to be published to the PUB/SUB which we created with above steps in GCP


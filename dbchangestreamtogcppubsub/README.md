## Steps to Run Application
    1. Follow the common readme file to install all the required softwares
    2. Update all required feilds in the .env file with the respective details of your's
    3. Open the terminal in the respective project folder and give "python main.py"
    
## Step 1: Set Up Google Cloud Project and Enable Pub/Sub
  If you haven't already, sign in to your Google Cloud Console.
  
  Create a new Google Cloud project or select an existing one where you want to create the Pub/Sub resources.
## Step 2: Create a Pub/Sub Topic
  In the Google Cloud Console, navigate to "Pub/Sub" from the left-side menu.
  
  Click on the "Topics" tab.
  
  Click the "Create a topic" button.
  
  Give your topic a name, e.g., "my-topic," and 
  click "Create."

  <img width="378" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/48faec53-39c2-4411-a0c9-9b0ff6d93f24">


## Step 3: Create a Pub/Sub Subscription
  From the "Topics" tab, select the topic you just created (e.g., "my-topic").
  
  Click on the "Create subscription" button.
  
  Provide a name for your subscription (e.g., "my-subscription").
  
  Configure other settings, such as acknowledging mode and delivery type, as per your requirements.
  
  Click "Create" to create the subscription.

  <img width="389" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/c997b4a0-c836-47f9-8b16-1a625acf8fdd">

  <img width="384" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/cb0a6cdf-1a8f-4e33-8784-fec8dfbda77e">


## Step 4: Application uses Pub/Sub in listening database level change stream document
  A database level changestream definition allows you to monitor and capture changes occurring at the database level in a MongoDB database. You can use this feature to track changes to documents within any collection in the database.

  Format the message that has to be published to the PUB/SUB which we created with above steps in GCP

  <img width="452" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/820a03fd-0669-4e7d-beb0-3e92e12460f1">



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
  
  Give your topic a name, e.g., "my-topic," and click "Create."

  <img width="378" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/90228a4e-e735-4b12-a5b7-672c76980c15">

  

## Step 3: Create a Pub/Sub Subscription
  From the "Topics" tab, select the topic you just created (e.g., "my-topic").
  
  Click on the "Create subscription" button.
  
  Provide a name for your subscription (e.g., "my-subscription").
  
  Configure other settings, such as acknowledging mode and delivery type, as per your requirements.
  
  Click "Create" to create the subscription.

  <img width="389" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/b56a07f0-a7c3-42a4-8899-518992077e86">

  <img width="384" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/c79f6e03-a421-45cf-9cff-86111c35327b">



## Step 4: Application uses Pub/Sub in listening Collection level change stream document
  A collection-level change stream in MongoDB allows you to monitor and capture changes occurring in a specific collection. You can use this feature to track changes to documents within that collection.

  Format the message that has to be published to the PUB/SUB which we created with above steps in GCP

  <img width="452" alt="image" src="https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/04271301-e466-4061-b114-242e2142249d">



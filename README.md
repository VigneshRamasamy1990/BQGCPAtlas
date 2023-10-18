# BQGCPAtlas

# Pre-Request Instructions

Before you start using this application, ensure that you have the necessary software and libraries installed. Follow these steps to set up your development environment. 

Execute the below commands before running each projects

## 1. Poetry setup
To run the application 1st initiate the poetry in you root directory

```bash
poetry init
```
will asks for the below details 

```bash
Package name [bqgcpatlas]:  bqgcpatlas
Version [0.1.0]:  
Description []:  
Author [TSowbaranika <109083730+TSowbaranika@users.noreply.github.com>, n to skip]:  
License []:  
Compatible Python versions [^3.10]:  

Would you like to define your main dependencies interactively? (yes/no) [yes] yes
Package to add or search for (leave blank to skip): 

Would you like to define your development dependencies interactively? (yes/no) [yes] yes
Package to add or search for (leave blank to skip):
Do you confirm generation? (yes/no) [yes] yes

```
- Install poetry to the application

```bash
poetry install
```


## 2. Python

Make sure you have Python installed on your system. If not, you can use the following command to install Python 3 using Homebrew (Mac users):

```bash
brew install python3
```

## 3. PyMongo
To work with MongoDB databases, you'll need to install the PyMongo library. Use the following command to install it:

```bash
pip install pymongo
```

## 4. python-dotenv
For managing environment variables and configuration settings in your Python application, you'll need the python-dotenv library. Install it with the following command:

```bash
pip install python-dotenv
```

## 5. Google Cloud Pub/Sub
If your application interacts with Google Cloud Pub/Sub for messaging, install the google-cloud-pubsub library with the following command:

```bash
pip install google-cloud-pubsub
```

## 6. Certifi
To provide a certificate bundle for secure communication over HTTPS and SSL/TLS-encrypted protocols, install the certifi library:

```bash
pip install certifi
```

Ensure that you have Python and pip installed on your system before running these commands. These libraries and tools are essential for the proper functioning of the application.

Now, you're all set to use the application with the required dependencies in place.

## 7. Steps to create MongoDb Cluster with Database and Collections

- Create an Account:

  * If you don't already have one, create an account with your MongoDB cloud service provider. For this example, we'll use MongoDB Atlas.

  * Log In:

  * Log in to your MongoDB cloud account.

- Create a New Cluster:

  * In MongoDB Atlas, click "Clusters" in the left sidebar.
  * Click the "Build a New Cluster" button.
  * Choose your cloud provider (e.g., AWS, Azure, Google Cloud).
  * Select your preferred region and settings for your cluster, such as the instance size, storage, and backup options.
  * Click "Create Cluster."

- Configure Security:

  * In MongoDB Atlas, click "Database Access" in the left sidebar.
  * Click "Add New Database User" to create a new user and assign the necessary privileges.
  * You may also need to configure the IP Whitelist to allow network access to your cluster. You can add your IP address or a range of IP addresses for security.

- Connect to Your Cluster:

  * In MongoDB Atlas, click "Clusters" and then select your newly created cluster.
  * Click the "Connect" button and select "Connect using MongoDB Compass."
  * Follow the instructions to download and install MongoDB Compass if you don't have it already.
  * Use the provided connection string in MongoDB Compass to connect to your cluster.

- Create a Database:

  * In MongoDB Compass, connect to your cluster.
  * In the Compass interface, click the "Create Database" button.
  * Provide a name for your database and create it.

- Create Collections and Documents:

  * After creating a database, you can create collections within it.
  * In MongoDB Compass, select your database and create collections.
  * You can start inserting documents into these collections.

## Steps to run each Projects

For Each Project run the main.py in its respective folder.

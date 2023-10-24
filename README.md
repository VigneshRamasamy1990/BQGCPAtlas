# Pre-Request

## Create MongoDb Cluster with Database and Collections
- Create an Account:
  * If you don't already have one, create an account with your MongoDB cloud service provider. For this example, we'll use MongoDB Atlas.
- Login to the Mongodb Atlas with exsisting account credential
- Create Cluster with whitelisting the required Ip's to be accessed
- Create the Database and the collection in the cluster created

## Create GCP account
- Create an Account:
  * If you don't already have one, create an account with your GCP provider.
- Log-in to the account with the credentials
- Click on the API's and Service in left panel then Enable the API's services

## Create Confluent Account
- Create an Account:
  * If you don't already have one, create an account with your Confluent provider.
- Log-in to the account with the credentials
- Click on the Environment and select "Default" then Select cluster create cluster with specific name.

## Software to be installed to run the application
- Before you start using this application, ensure that you have the necessary software and libraries installed. Follow these steps to set up your development environment. 

- Execute the below commands before running each project
## 1. Poetry setup
To run the application 1st initiate the poetry in you root directory

```bash
poetry init
```
Install poetry to the application.

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

## Steps to run each Projects

For Each Project run the main.py in its respective folder.

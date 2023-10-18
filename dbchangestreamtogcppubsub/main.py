from changestreamtogcptopic  import ChangeStreamToGCPTopic

def main():

    dbchangestream_to_gcp = ChangeStreamToGCPTopic()
    dbchangestream_to_gcp.to_perform_mongo_changestream_to_gcp_topics()
          
    print("change stream to gcp topics is completed")


#calling the main method
main()
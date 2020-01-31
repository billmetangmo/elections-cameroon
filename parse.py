"""
Your module description
"""

import os
import json
from collections import Counter

def read_lines_as_json(path):

        if os.path.exists(path):
            # warning if remote filesystem this means nothing but we assume there a local posix filesystem
            data = []
            if os.access(path, os.R_OK):
                with open(path, 'r') as fd:
                    for line in fd:
                        data.append(json.loads(line))
                return data
            else:
                raise ValueError("Bad rights when trying to read data from file"+path+".")


if __name__ == "__main__":
    
    tweets = read_lines_as_json("/home/ec2-user/environment/out/b87780713a7144fd82b2d6939f1053a8-20180830150537023-00000-hjoxp4lb.json")
    #users = [ tweet["user"]["name"] for tweet in tweets ]
    #print (Counter(users))
    
    users=[]
    for tweet in tweets:
        if tweet.get("extended_entities") is not None:
            if tweet.get("extended_entities").get("media") is not None:
                if len(tweet["extended_entities"]["media"]) == 1:
                    # photo, video, and animated_gif
                    if tweet["extended_entities"]["media"][0]["type"] == "photo":
                        users.append(tweet["user"]["name"])
                else:
                    #pass
                    for i in range(0,len(tweet["extended_entities"]["media"])-1):
                        if tweet["extended_entities"]["media"][i]["type"] == "photo":
                            users.append(tweet["user"]["name"])
                
    print (Counter(users))
    
    
    

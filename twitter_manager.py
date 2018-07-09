"""
Twitter Manager
"""

__author__ = "?"
__version__ = "0.1.0"
__license__ = "CC-A-NC-SA 4.0"


from credentials import *
import tweepy


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def main():
    """
    main manager app
    
    fucntion: follow all people following me
    
    function: unfollow non-reciprocal follows
        list non-reciprocal follows
        Check to see if followed are following
            add non-reciprocal to list
        For person in non-reciprocal list:
            get date I followed a person
            if followed do not follow back in X days since date I followed them:
                unfollow followed person
    
    
    """
    pass


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()

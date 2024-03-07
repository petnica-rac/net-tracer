from datetime import datetime, timedelta
import sys

def combined_unix_to_datetime(combined_unix):

    unix_seconds = int(combined_unix)
    microseconds = int((combined_unix - unix_seconds) * 1e6)  


    dt = datetime.utcfromtimestamp(unix_seconds)

    dt_with_microseconds = dt + timedelta(microseconds=microseconds)

    return dt_with_microseconds

if __name__ == "__main__":
    #combined_unix = 1709832820.799745547
    #combined_unix = sys.argv[0]
    print (combined_unix_to_datetime(combined_unix))
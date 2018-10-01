import operator

nvalue=int(input("Enter n value : "))
#file=open("fashion.txt", "r",encoding="utf-8");
lines = []
with open("./fashion.txt", encoding="utf-8") as file:
    for line in file:
        lines.append(line)

    #print(lines)

    users={}
    for data in lines:
        tempval = data.split()
        #print(tempval)
        if tempval[0] in users:
            users[tempval[0]] += 1
            #print(users)
        else:
            users[tempval[0]] = 1
    users = sorted(users.items(), key=operator.itemgetter(1), reverse=True)
    most_tweets_timeline = open("most_tweets_timeline.txt", "w", encoding="utf-8")

    for x in range(0, nvalue):
        most_tweets_timeline.write(users[x][0] + " tweeted " + str(users[x][1]) + " times" + "\n")
        most_tweets_timeline.flush()

    hours={}
    time=[]
    for data in lines:
        tempval = data.split()
        tempval2=tempval[1].split(":")
        hourval=tempval2[1]
        tempobj=tempval[0]+ " " + hourval
        if tempobj in hours:
            hours[tempobj]+=1
        else:
            hours[tempobj]=1
    hours = sorted(hours.items(), key=lambda x:(x[1]), reverse=True)
    most_tweets_hour = open("most_tweets_hour.txt", "w", encoding="utf-8")

    for x in range(0, nvalue):
        most_tweets_hour.write(hours[x][0] + "\n")
        most_tweets_hour.flush()

    followers={}
    for data1 in lines:
        tempval1 = data1.split()
        cfol = (len(tempval1) - 2)
        if tempval1[0] not in followers:
            followers[tempval1[0]] = int(tempval1[cfol])
    followers = sorted(followers.items(), key= lambda x:(x[1]),reverse=True)

    max_followers = open("max_followers.txt", "w", encoding="utf-8")

    for x in range(0, nvalue):
        max_followers.write("User: "+followers[x][0] + " -> Number of Followers: " + str(followers[x][1]) + "\n")
        max_followers.flush()


    tweets={}
    for data in lines:

        tempval1 = data.split()
        ran = len(tempval1) - 2
        sval = "\""
        for nd in range(3, ran):
            sval += tempval1[nd] + " "
        if sval not in tweets:
            tweets[sval] = tempval1[len(tempval1) - 1]
    tweets = sorted(tweets.items(),key=lambda x:(x[1]), reverse= True)
    print(tweets)
    max_tweets = open("max_tweets.txt", "w", encoding="utf-8")

    for x in range(0, nvalue):
        max_tweets.write("User: "+ tweets[x][0] + " -> Number of Tweets: " + str(tweets[x][1]) + "\n")
        max_tweets.flush()


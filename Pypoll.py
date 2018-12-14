import csv

voter_ID =[]
candidates=[]
votes=[]
percents=[]
candidates=[]
count = 0
filepath = "Resources_pypoll/election_data.csv"
with open(filepath, 'r') as polldata:
    pollreader=csv.reader(polldata, delimiter=',')
    pollheader=next(pollreader)
    for row in pollreader:
        voter_ID.append(row[0])
        if row[2] not in candidates:
                candidates.append(row[2])
    row_count = len(voter_ID)
    polldata.seek(0)
    for candidate in candidates:
        for i in pollreader:
            if i[2] == candidate:
                    count += 1
        polldata.seek(0)
        percent=round(count/row_count,2)
        votes.append(count)    
        percents.append(percent)
        count=0
final_votes=zip(candidates, percents, votes)
winner = candidates[percents.index(max(percents))]
print("Election Results")
print("-------------------------")
print("Total Votes:", row_count)
print("-------------------------")
for final_vote in final_votes:
    print(final_vote[0]+ ":" + "{:.3%}".format(final_vote[1]) + "(" + str(final_vote[2])+")")
print("-------------------------")
print("Winner:" + winner)


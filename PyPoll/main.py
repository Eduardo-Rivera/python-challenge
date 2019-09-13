import csv
import collections

#importing csv file
with open ("election_data.csv", "r") as election_file:
    poll = csv.reader(election_file)

     #skip header row
    next(poll)

    votes_counter = 0
    candidates = []
    candidates_votes = collections.Counter()

   #sum of votes and sum for each candidate 
    for i in poll:
        votes_counter += 1
        candidates_votes[i[2]] += 1
        
 #print results
    print("Election Results")
    print("-----------------------")
    print(f'Total Votes: {votes_counter}')
    print("-----------------------")

    for k,v in candidates_votes.items():
        percent = (v/votes_counter)*100
        print (f'{k} : {round(percent,3)}% ({v})')
    
    winner = max(candidates_votes, key=candidates_votes.get)
    print("-----------------------")
    print (f'Winner: {winner}')
    print("-----------------------")
   
#Export to txt file
output = (
    "Election Results\n"
    "-----------------------\n"
    f'Total Votes: {votes_counter}\n'
    f"-----------------------\n"
    f"{k} : {round(percent,3)}% ({v})\n"
    f"Winner: {winner}\n"
    "-----------------------")

with open ("output2.txt", "w") as the_file:
    the_file.write(output)
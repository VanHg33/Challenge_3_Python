
import os
import csv


csvpath= os.path.join("Resources", "election_data.csv")
export_file = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_name_list = []
candidate_vote_count = {}
percent_vote = {}
highest_percentage = 0
winner = " "

    
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    
    for row in csvreader: 
        total_votes = total_votes + 1 
        current_candidate = row[2]
        if current_candidate not in candidate_name_list: 
            candidate_name_list.append(current_candidate)
            candidate_vote_count[current_candidate] = 0
        candidate_vote_count[current_candidate] = candidate_vote_count[current_candidate] + 1
        
        
with open(export_file, "w") as text_file:

    output1 = (f"Election Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes}\n"
            f"-------------------------\n")
    print(output1)
    text_file.write(output1)


    for candidate in candidate_vote_count:
        votes = candidate_vote_count.get(candidate)
        percent_vote = float(votes)/ float(total_votes) * 100
      
        if (votes > highest_percentage):
            highest_percentage = votes
            winner = candidate

        output2 = f"{candidate}: {percent_vote:.3f}% ({votes})\n"
        print(output2)
        text_file.write(output2)

    output3 = (f"-------------------------\n"
            f"Winner: {winner}\n"
            f"-------------------------\n")
    print(output3)
    text_file.write(output3)

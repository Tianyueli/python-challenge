from pathlib import Path
import os
import csv

election_path = os.path.join("Assignments", "Module_3_Assignment", "python-challenge", "PyPoll", "Resources", "election_data.csv")

with open(election_path) as election_data:
    reader = csv.reader(election_data, delimiter = ',')
    total_candidates = 0
    row_count = 0
    candidate_list = set()
    candidate_votes = 0

    for row in reader:
        row_count += 1
        candidate_list.add(row[2])
        # if candidate_list(row_count) == candidate_list(row_count+1):
        #     candidate_votes += candidate_list(row_count)
        # elif candidate_list(row_count) != candidate_list(row_count+1):
        #     print(candidate_list, ": ", candidate_votes)
        #     candidate_votes = 0


    total_votes = row_count - 1
    print("Total votes: ", total_votes)
    print(candidate_list)
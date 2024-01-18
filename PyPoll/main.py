from pathlib import Path
import os
import csv

election_path = os.path.join("Assignments", "Module_3_Assignment", "python-challenge", "PyPoll", "Resources", "election_data.csv")
election_data = csv.reader(election_path, delimiter = ",")

with open(election_path) as election_data:

    total_candidates = 0
    row_count = 0

    for row in election_data:
        row_count += 1
        candidate_list = set(row[2])
        def f(row):
            print(list(set(row)))
    total_votes = row_count - 1
    print(total_votes)
    # print(candidate_list)


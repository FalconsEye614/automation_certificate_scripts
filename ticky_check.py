#!/usr/bin/env python3
import re
import operator
import csv

error_log = r" ERROR ([\w' ]*) "
user_log = r" ([A-Z]*) [\w \[\]#0-9']* \(([\w.]*)\)"

error_dict = {}
user_info_dict = {}
user_error_dict = {}

with open("syslog.log", 'r') as f:
    for line in f:
        error = re.findall(error_log, line)
        user = re.findall(user_log, line)
        if len(error) > 0:
            error_dict[error[0]] = error_dict.get(error[0], 0) + 1
        if user[0][0] == 'INFO':
            user_info_dict[user[0][1]] = user_info_dict.get(user[0][1], 0) + 1
            user_error_dict[user[0][1]] = user_error_dict.get(user[0][1], 0)
        else:
            user_info_dict[user[0][1]] = user_info_dict.get(user[0][1], 0)
            user_error_dict[user[0][1]] = user_error_dict.get(user[0][1], 0) + 1
    f.close()

per_user = []
for user, number in user_info_dict.items():
    per_user.append((user, user_info_dict[user], user_error_dict[user]))

sorted_error = sorted(error_dict.items(), key=operator.itemgetter(1), reverse=True)
sorted_error.insert(0, ("Error", "Count"))
sorted_user = sorted(per_user)
sorted_user.insert(0, ("Username", "INFO", "ERROR"))

with open("error_message.csv", "w+", newline='') as error_file:
    error_csv = csv.writer(error_file)
    error_csv.writerows(sorted_error)

with open("user_statistics.csv", "w+", newline='') as user_file:
    user_csv = csv.writer(user_file)
    user_csv.writerows(sorted_user)

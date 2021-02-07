import datetime, requests, csv
from datetime import datetime

#stamp = datetime.now()
#print(stamp.strftime("%Y-%m-%d-%H%M%S"))

# GitHub secret
# https://github.com/settings/tokens
token = ""
auth = ("headers={'Authorization': " + token + "}")

# Repositry lists file
repolist = open("repolist.txt", "r")
# Set csv header fields
with open("repodata.csv", "w", newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
    writer.writerow(["name","clone_url","commit_author", "commit_date"])
file.close()
#Read lines from repository file
for line in repolist:
    #split words
    fields = line.rstrip('\n').split("/")
    orgs = fields[0]
    repo = fields[1]
    # Based on file list generate url for github api
    # Basic repository informations
    basic_link = ('https://api.github.com/repos/' + orgs + '/' + str.rstrip(repo))
    # Commits repository informations
    commits_link = ('https://api.github.com/repos/' + orgs + '/' + str.rstrip(repo) + '/commits?per_page=1')
    # Query github API
    if token == "":
        basic_query = requests.get(basic_link)
        commits_query = requests.get(commits_link)
    else:
        basic_query = requests.get(basic_link, auth)
        commits_query = requests.get(commits_link, auth)
    # If reposity found then proceed
    if basic_query.status_code == 200:
        # Getting repository informations
        basic_queryjson = basic_query.json()
        # Get data
        basic_name = basic_queryjson["name"]
        basic_clone = basic_queryjson["clone_url"]
        commits_queryjson = commits_query.json()
        commits_login = commits_queryjson[0]["author"]["login"]
        commits_author = commits_queryjson[0]["commit"]["author"]["name"]
        commits_date = datetime.strptime(commits_queryjson[0]["commit"]["author"]["date"], "%Y-%m-%dT%H:%M:%SZ")
        #commits_dateconvert = commits_date.strftime('%A %b %d, %Y at %H:%M GMT')
        # Save data
        row_list = [[basic_name, basic_clone, commits_author, commits_date] ]
        with open("repodata.csv", 'a', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
            writer.writerows(row_list)
    # Show response from API when failed
    else:
        print(repo + " request failed (" + str(basic_query.status_code) + ")" + basic_query.text)
#Close file
file.close()
repolist.close()
Hello again everyone,

New and improved version of the tictactoe game, and thanks to Ras for his valuabale feedback.

Below are the modifications made to the initial version that was created via Jupyter notebook with limited features:

1. Used list comprehension in the display_board function instead of conventional printing of the list items row-by-row
2. Better function calling and argument passing i.e. excluding global variables and incorporating inline functions
3. Added game_on function to determine if the players want to continue playing or end the game.

Again, your feedback is precious and appreciated!

[30th July 2025] New addition to the repository are as follows:

1. Python script to create PagerDuty Services extracting service name and escalation policy id's from a CSV file, passed as arguments.
2. Sample CSV file that can be used for the script above.
3. Another python script to list the PagerDuty services relavant to the API Key and From Email Address passed as an argument.

[4th August 2025] New addition to the repository as follows:

1. Python script named "snow-admin-login.py" automates the login to the ServiceNow Dev Instance using the specific URL, username, and password supplied in the json file named "url_and_creds.json"
2. Idea is to call this python script via a Runbook job, scheduled to run atleast once a week to keep the instance(s) alive.

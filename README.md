# metrics_scraper

# Description

This program crawls the given instagram usernames, stores their post and followers count, and writes the result to specified google sheet. 

# Setup

- Clone the repo found here:
- In order to use the Google Sheets API you must first create a Google Workspace account a project. The steps can be found here: [Google Developers Python Quickstart](https://developers.google.com/sheets/api/quickstart/python) (stop before the heading “**Configure the sample**”)
- Replace the following variables with the required values:
    - handles_string = "REPLACE WITH HANDLES” ex: “test1_account account_test2 test3”
    - spreadsheetId ="YOUR SPREADSHEET ID” : Spreadsheet ID you want to write to, found after /d/ in the spreadsheet link
    - range ="YOUR SPREADSHEET DATA RANGE” : Rang to write data to. ex: If you have 30 accounts your range is Sheet 1!A1:B30
    

# Execute

- Run the program by executing >> python3 metrics_scraper.py

# Troubleshooting

- [Troubleshoot Authentication Issues](https://developers.google.com/sheets/api/troubleshoot-authentication-authorization)
- The Instaloader class only supports 199 handles per instance. If you have more accounts, uncomment lines 69-76 and replace the handles variable with the other half of your list
- If continual login errors occur, instagram’s new api may have flagged your IP address as suspicious. This can be remedied by changing your local network or using a vpn

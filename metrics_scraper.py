import instaloader
import time
import os.path
import datetime
from datetime import date
import schedule
import pandas as pd
import csv
import gspread
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload
from oauth2client.service_account import ServiceAccountCredentials

def ScrapeInsta():

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    spreadsheetID = "YOUR SPREADSHEET ID"
    range = "YOUR SPREADSHEET DATA RANGE"
    handles_string = "REPLACE WITH HANDLES"

    # create or authenticate credentials
    creds = None
    # config token
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())


    # Creating an instance of the Instaloader class
    bot = instaloader.Instaloader()

    # array of handles - formated as a string with spaces between handles
    handles = handles_string.split()


    # init list and enter date + header
    values = []
    today = date.today()
    today = today.strftime("%d/%m/%Y")
    date = [today, '']
    headers = ["Posts", "Followers"]
    values.append(date)
    values.append(headers)

    # pull only posts and followers and append to list
    for handle in handles:
        temp_list = []
        profile = instaloader.Profile.from_username(bot.context, handle)
        temp_list.append(profile.mediacount)
        temp_list.append(profile.followers)
        values.append(temp_list)

    # Secondary list for other handles
    # bot = instaloader.Instaloader()
    # handle = "REPLACE WITH OTHER HANDLES"
    # for handle in handles:
    #     temp_list = []
    #     profile = instaloader.Profile.from_username(bot.context, handle)
    #     temp_list.append(profile.mediacount)
    #     temp_list.append(profile.followers)
    #     values.append(temp_list)


    body = {
        'values': values
    }

    # open and write to google sheet
    service = build('sheets', 'v4', credentials=creds)
    result = service.spreadsheets().values().update(
        spreadsheetId=spreadsheetID,
        range=range,
        valueInputOption="RAW", body=body).execute()


# Scheduled for every dat 8 am
schedule.every().day.at("08:00").do(ScrapeInsta)


while True:
    schedule.run_pending()
    time.sleep(10,000)

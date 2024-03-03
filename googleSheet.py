import os

import httplib2
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build

SHEET_ID = "1tkbil1VcysRJKN-l1g6OpY3C_FahImzt7nFIHUx-9As"


def get_service_sacc():
    creds_json = os.path.dirname(__file__) + "\\sap-rss-feed-c67865562590.json"
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)


def get_data():
    resp = get_service_sacc().spreadsheets().values().get(spreadsheetId=SHEET_ID,
                                                          range="Useful links!A1:N999").execute()
    return resp

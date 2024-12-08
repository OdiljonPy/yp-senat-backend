# from googleapiclient.discovery import build
# from google.oauth2.service_account import Credentials
# from django.conf import settings
#
#
# def get_google_sheet_data(spreadsheet_id):
#     creds = Credentials.from_service_account_file(
#         settings.GOOGLE_APPLICATION_CREDENTIALS,
#         scopes=['https://www.googleapis.com/auth/spreadsheets.readonly']
#     )
#
#     service = build('sheets', 'v4', credentials=creds)
#     sheet = service.spreadsheets()
#
#     sheet_metadata = sheet.get(spreadsheetId=spreadsheet_id).execute()
#     sheet_title = sheet_metadata['sheets'][0]['properties']['title']
#     range_name = f'{sheet_title}'
#
#     result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
#     return result.get('values', [])
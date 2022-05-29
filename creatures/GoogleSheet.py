from metaclasses.Singleton import SingletonMetaClass
from utils.ConfigManager import ConfigManager
from googleapiclient.discovery import build
from google.oauth2 import service_account


class GoogleSheet(metaclass=SingletonMetaClass):

    __CREDENTIALS = service_account.Credentials.from_service_account_file(
        ConfigManager().get_from_google_config("service_account_file"),
        scopes=[ConfigManager().get_from_google_config("scopes")]
    )

    __SERVICE = build('sheets', 'v4', credentials=__CREDENTIALS)
    __SHEET = __SERVICE.spreadsheets()
    __SAMPLE_SPREADSHEET_ID = ConfigManager().get_from_google_config(
        "spreadsheet_id")

    def get_values_from_table(self, table_range="List1!A1:B39"):
        res = self.__SHEET.values().get(
            spreadsheetId=self.__SAMPLE_SPREADSHEET_ID,
            range=table_range
        ).execute()

        return res.get('values')

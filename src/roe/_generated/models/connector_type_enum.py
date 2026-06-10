from enum import Enum

class ConnectorTypeEnum(str, Enum):
    CHECKOUT_COM = "checkout_com"
    CUSTOM_API = "custom_api"
    GOOGLE_DRIVE = "google_drive"
    INTERCOM = "intercom"
    LEXIS_NEXIS = "lexis_nexis"
    PLAID = "plaid"
    S3 = "s3"
    SALESFORCE = "salesforce"
    SARDINE = "sardine"
    SHAREPOINT = "sharepoint"
    SNOWFLAKE = "snowflake"
    SOCURE = "socure"
    STRIPE = "stripe"
    WEB_APPLICATION = "web_application"
    ZENDESK = "zendesk"

    def __str__(self) -> str:
        return str(self.value)

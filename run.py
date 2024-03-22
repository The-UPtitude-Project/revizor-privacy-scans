import base64, requests, json
from config import OUTPUT_PATH, OUTPUT_FILE, COMPANY_NAME, HOST, PORT, FILE_PATH, HOMEPAGE_ONLY, NEW_URL_STARTING_ROW
from list_urls import init_driver, main
from credentials import BREVO_API_KEY

if __name__ == '__main__':

    driver = init_driver()
    main(FILE_PATH, OUTPUT_FILE, driver, homepage_only=HOMEPAGE_ONLY, start=NEW_URL_STARTING_ROW)

    print("\nDone!")

excel_path = OUTPUT_PATH + f"output.xlsx"
data = open(excel_path, 'rb').read()
base64_encoded = base64.b64encode(data).decode('UTF-8')
data = {
        "sender":{
            "name":"Team Kestral",
            "email":"no-reply@kestral.co.uk"
        },
        "to":[
            {
                "email":"a.goyal@uptitude.cloud",
                "name":"Anushka Goyal"
            }
        ],
        "subject":f"Privacy scan completed for {COMPANY_NAME}",
        "htmlContent":f"<html><head></head><body><h3>Hello,</h3><p>The privacy scan is completed for {COMPANY_NAME}</p><p>Find the output at - {HOST}:{PORT}/scanner/download/{COMPANY_NAME}/privacy-scans</p></body></html>",
        "attachmentContent": base64_encoded
    }
headers = {
    'accept': 'application/json',
    'api-key': BREVO_API_KEY,
    'content-type': 'application/json'
}
url = 'https://api.brevo.com/v3/smtp/email'
requests.post(url=url, data=json.dumps(data), headers=headers)
import imaplib
import email
from datetime import datetime, timedelta
import pandas as pd
import re
ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "abishaikanhiramkalayil" + ORG_EMAIL
FROM_PWD = "barbdgunbyjuewdq"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993
TARGET_SUBJECT = 'Security alert'
def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL, FROM_PWD)
        mail.select('inbox')
        desired_sender = 'esfb-alerts@equitasbank.com'
        start_date = (datetime.now() - timedelta(days=30)).strftime('%d-%b-%Y')
        end_date = datetime.now().strftime('%d-%b-%Y')
        date_criteria = f'(SINCE "{start_date}" BEFORE "{end_date}")'
        sender_criteria = f'FROM "{desired_sender}"'
        search_criteria = f'{date_criteria} {sender_criteria}'
        data = mail.search(None, search_criteria)
        mail_ids = data[1][0].split()
        email_data = {'Subject': [], 'Body': []}
        for mail_id in mail_ids:
            data = mail.fetch(mail_id, '(RFC822)')
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    try:
                        msg = email.message_from_bytes(arr[1])
                        email_from = msg['from']
                        if desired_sender.lower() in email_from.lower():
                            email_subject = msg['subject']
                            if msg.is_multipart():
                                for part in msg.walk():
                                    if part.get_content_type() == "text/plain":
                                        body = part.get_payload(decode=True)
                                        email_data['Subject'].append(email_subject)
                                        email_data['Body'].append(body.decode('utf-8'))
                                        break
                            else:
                                body = msg.get_payload(decode=True)
                                email_data['Subject'].append(email_subject)
                                email_data['Body'].append(body.decode('utf-8'))
                    except UnicodeDecodeError:
                        print("Unable to decode the email content. Raw bytes:", arr[1])
    except Exception as e:
        print(str(e))
    finally:
        mail.logout()
    return pd.DataFrame(email_data)
def extract_transaction_data(body):
    amount_pattern = re.compile(r'Amount of INR (\d+\.\d+)')
    transaction_type_pattern = re.compile(r'has been (\w+) from')
    amount = 'N/A'
    transaction_type = 'N/A'
    match_amount = amount_pattern.search(body)
    match_transaction_type = transaction_type_pattern.search(body)
    if match_amount:
        amount = match_amount.group(1)
    if match_transaction_type:
        transaction_type = match_transaction_type.group(1).lower()
    return amount, transaction_type
def calculate_total_amount(df):
    total = 0
    for body in df['Body']:
        amount, _ = extract_transaction_data(body)
        try:
            total += float(amount)
        except ValueError:
            pass
    return total

def get_amount():

    email_df = read_email_from_gmail()
    return calculate_total_amount(email_df)

import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_company_share(code):
    url = f'https://www.google.com/finance/quote/{code}:NASDAQ?sa=X&ved=2ahUKEwjp85aG96CDAxVzYfUHHbSzD_kQ3ecFegQILhAh'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    elem = soup.find('div',{'class':'YMlKec fxKbKc'})
    return elem.text


def get_share():
    dict={}
    companies=['AAPL','MSFT','GOOGL','AMZN','TSLA']
    for company in companies:
        dict[company]=get_company_share(company)
    return dict

if __name__ == '__main__':

    print(f'Total of numeric values in the "Amount" column: {get_amount()}')
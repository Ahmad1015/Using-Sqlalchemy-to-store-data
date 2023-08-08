import re
from itertools import chain

# Task 1
with open('fradulent_emails.txt', 'r') as file:
    filelines = file.read()


def regular_python_on_emails_names(flag=True):
    python_code_name = []
    for line in filelines.strip().split("\n"):
        if line.startswith("From:"):
            for count in range(len(line)):
                if line[count] == "<":
                    break
            string_slicing = line[7:count - 2]
            python_code_name.append((string_slicing))
    if flag:
        return python_code_name
    for name in python_code_name:
        print(name)





def regrex_python_on_names(filetemp, flag=False):
    python_regrex = re.findall(r'From: "(.*?)" <', filetemp)
    for name in python_regrex:

        if flag:
            return name
        print(name)




def python_regrex_on_emails(filetemp, temp,flag=False):
    global python_regrex_emails
    if temp == "Sender":
        python_regrex_emails = re.findall(r'Return-Path: <(.*?)>', filetemp)
    else:
        python_regrex_emails = re.findall(r'(?<=\nTo: ).*?(?=\n\S)', filetemp, re.DOTALL)
    python_regrex_emails = list(set(python_regrex_emails))
    if flag:
        return python_regrex_emails
    for name in python_regrex_emails:
        print(name)





def first_part_of_email():
    first_part = [re.findall(r'(.*?)\@', email) for email in python_regrex_emails]
    first_part = list(chain(*first_part))
    for name in first_part:
        print(name)





def second_part_of_email():
    second_part = [re.findall(r'@(.*)', email) for email in python_regrex_emails]
    second_part = list(chain(*second_part))
    for name in second_part:
        print(name)





def email_date(filetemp,flag=False):
    lines = filetemp.split('\n')
    if flag:
        return lines[0]
    print("Date: " + lines[0])


def email_subject(filetemp,flag=False):
    subjects = re.findall(r'(?<=\nSubject: ).*?(?=\n\S)', filetemp, re.DOTALL)
    if isinstance(subjects, list):
        if subjects:
            if flag:
                return subjects[0]
            else:
                print("Subject: " + subjects[0])
    elif isinstance(subjects, str):
        if flag:
            return subjects
        else:
            print("Subject: " + subjects)



def body_email(filetemp, flag2 = False):
    flag = False
    tempstr = ""
    for line in filetemp.split("\n"):
        if flag:
            tempstr +=line
        if line.startswith("Status:"):
            flag = True
    if flag2:
        return tempstr
    else:
        print(tempstr)


emails = filelines.split("From r")[1:]

def Task6():
    global emails
    for i, email in enumerate(emails, 1):
        print(f"\nEmail {i}:")
        print("Sender Name: ", end="")
        sender_name = regrex_python_on_names(email.strip(), True)
        print("Sender Address: ", end="")
        sender_address = python_regrex_on_emails(email.strip(), "Sender")
        print("Recipient Address: ", end="")
        recipient_address = python_regrex_on_emails(email.strip(), "recipient_address")
        date_sent = email_date(email.strip(),False)
        subject = email_subject(email.strip(),False)
        print("email Body: ", end="")
        email_body = body_email(email.strip(),False)


def main():
    global emails
    # Task 2 getting names without regrex
    print("\nTask 2 answers:\n")
    regular_python_on_emails_names(False)

    # Task 3 Getting names using Regrex
    print("\nTask 3 answers:\n")
    regrex_python_on_names(filelines)

    # Task 4 getting emails using Regrex
    print("\nTask 4 answers:\n")
    python_regrex_on_emails(filelines, "Sender",False)

    # Task 5 extracting the first part of the email address
    print("\nTask 5 answers:\n")
    first_part_of_email()

    # Task 5 extracting the second part of the email address
    print("\nTask 5 answers:\n")
    second_part_of_email()

    # Task 6 Sorting
    print("\nTask 6 answers:\n")
    Task6()







if __name__ == "__main__":
    main()

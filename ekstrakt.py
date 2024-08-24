import re

def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.findall(email_pattern, text)

with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()

emails = extract_emails(text)

with open('used.txt', 'r', encoding='utf-8') as file:
    used_emails = set(file.read().splitlines())

new_emails = [email for email in emails if email not in used_emails]

# Write the new email addresses to a new file
with open('emails.csv', 'w', encoding='utf-8') as file:
    file.write("email" + '\n')

    for email in new_emails:
        file.write(email + '\n')

print("New email addresses have been extracted and saved to emails.csv")

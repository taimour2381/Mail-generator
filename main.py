placeholder = "[name]"

names = []
with open("./Input/recipients.txt") as recipient_names:
    recipients = recipient_names.readlines()
    print(recipients)

with open("./Input/starting_email.txt") as email_to_send:
    email = email_to_send.read()
    for name in recipients:
        stripped_name = name.strip()
        ready_email = email.replace(placeholder, name)
        with open(f"./Email_to_{stripped_name}.txt", mode="w") as ready_emails:
            ready_emails.write(ready_email)
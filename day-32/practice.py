import smtplib

# ✅ App Password
# Steps:
# 1. Turn on 2-Step Verification
# 2. Go to Google Account → Security
# 3. Open App Passwords
# 4. Generate password for “Mail”
# 5. Use that generated password in code

my_email = "YOUR EMAIL"         # Add your email id
password = "YOUR PASSWORD"      # Add your password

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()   # VERY IMPORTANT
# connection.login(my_email, password)
# connection.sendmail(
#     from_addr=my_email, 
#     to_addrs="ADD THE EMAIL OF RECEPIENT", 
#     msg="Subject: Testing Python script for SMTP\n\nHello, this is me.")
# connection.close()

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="ADD THE EMAIL OF RECEPIENT",
        msg="Subject: Hello from the other side\n\nHiiiii"
    )

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month

print(now)
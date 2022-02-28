import random
import smtplib
import unicodedata

#My email auth

my_email = "[Your email]"
password = "[Your email password]"

#TODO 1 - Read kindle hightlights.txt

with open(file="My Clippings.txt", mode='r') as kindle_highlights:
    highlights_content = kindle_highlights.read()

# print(highlights_content)

#TODO 2 - Split all highlighs on the highlights.txt

highlights = highlights_content.split("==========")

# Highlights without new line string

# pure_highlights = []
#
#
# for highlight in highlights:
#
#     pure_highlights.append(highlight.replace('\n',""))
#
# print(pure_highlights)

#TODO 3 - Random choose one highlight

random_highlight = random.choice(highlights)

# print(random_highlight.encode("ascii"))

message = f"Subject: Daily kindle highlight \n\n{random_highlight}"


#TODO 4 - Send the highlight to email

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="[to address email]",
    msg=message.encode("utf-8"),

)
connection.close()

#TODO 5 - Repeat the task everyday



# Import the necessary libraries
import mailbox
import pandas as pd

# Open the mbox file
mbox = mailbox.mbox('sample.mbox')

# Create a list of dictionaries, where each dictionary represents a message
# in the mbox file
messages = []
for message in mbox:
  messages.append({
    'subject': message['Subject'],
    'from': message['From'],
    'date': message['Date'],
    'body': message.get_payload()
  })

# Convert the list of dictionaries to a Pandas DataFrame
df = pd.DataFrame(messages)
print(df)
df['email']=df['body'].str.findall('(\S+@\S+)')
# Save the DataFrame to an Excel spreadsheet
df.to_excel('my_excel_file.xlsx', encoding="utf-8")
df.to_csv('my_excel_file.csv')


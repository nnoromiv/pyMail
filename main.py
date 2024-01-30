import os
import smtplib
import time
from dotenv import load_dotenv
import json

class Mail:
    
    # Load The Environment
    load_dotenv()
    
    # Initialize the Class call
    def __init__(self) -> None:
        while True:
            user_input = input("Running Program.... 🏃‍♂️🏃‍♂️🏃‍♂️ \n Press s to START: \n Press q to QUIT: \n\n ")
            
            if user_input.lower() == 'q':
                print("Quitting Program... 👋")
                break
            elif user_input.lower() == 's':
                print("Started Program... 🦌🦌")
                self.handle_mail()
            else:
                print(f"{user_input} Not a recognized command try 'q' or 's' \n\n")
                   
    # Connects the Server 
    def connect_smtp(self, subject, message, to):
        
        # Constructor Init
        self.subject = subject
        self.message = message
        self.to = to
        
        # Call SMTP variables from the Environment
        server = os.getenv("SERVER")
        port = os.getenv("PORT")
        email = os.getenv("EMAIL")
        password=os.getenv("PASSWORD")
        
        # Sender Name for Message
        sender_name = os.getenv("SENDER_NAME")
        
        # Carbon Copy Email address
        cc_email = os.getenv("CARBON_COPY") 
        
        # SMTP Server Configuration 
        smtp_server = server
        smtp_port = port
        sender_email = email
        sender_password = password
        
        # Composed Mail
        mail = f"Subject: {self.subject}\n\n"\
                f"Dear sir/ma,\n\n"\
                f"{self.message}\n\n"\
                f"Regards, {sender_name}"

        
        # Connect to the Server
        with smtplib.SMTP(smtp_server,smtp_port) as server:
            # Log Into Account
            server.starttls()
            server.login(sender_email,sender_password)
            
            server.sendmail(sender_email, [self.to, cc_email], mail)
        
        
    # Handles Mail Sending
    def handle_mail(self) -> str:
        # Call Recipient Email from the Environment
        recipient = os.getenv("RECIPIENT")
        
        # Message Array
        with open('messages.json', 'r') as file:
            messages = json.load(file)   
        
        # Who receives the mail
        recipient_email = recipient
        
        # Loops through the array messages 
        for index, message in enumerate(messages):
            if message["recipient"] == "":
                # Sends Each Message to default recipient
                self.connect_smtp(message["subject"], message["body"], recipient_email)
                print(f"Message {index + 1} Sent.. ✅ \n Going to sleep... 😴💤 \n Building for Message {index + 2}... 👷‍♂️👷")
                print(f"Use 'CTRL + c' to stop program. \n\n")
            else:
                self.connect_smtp(message["subject"], message["body"], message["recipient"])
                print(f"Message {index + 1} Sent.. ✅ \n Going to sleep... 😴💤 \n Building for Message {index + 2}... 👷‍♂️👷")
                print(f"Use 'CTRL + c' to stop program. \n\n")
                
            # Sets a timeout after one message sends
            time.sleep(180)
    
        print("Successfully Sent All 💯💯")   
        
        
if __name__ == "__main__":
    mail_instance = Mail()
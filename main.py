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
        self.handle_mail()
        
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
        
        # SMTP Server Configuration 
        smtp_server = server
        smtp_port = port
        sender_email = email
        sender_password = password
        
        # Composed Mail
        mail = f"Subject: {self.subject}\n\n{self.message}"
        
        # Connect to the Server
        with smtplib.SMTP(smtp_server,smtp_port) as server:
            # Log Into Account
            server.starttls()
            server.login(sender_email,sender_password)
            
            server.sendmail(sender_email, self.to, mail)
        
        
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
        for message in messages:
            if message["recipient"] == "":
                # Sends Each Message to default recipient
                self.connect_smtp(message["subject"], message["body"], recipient_email)
            else:
                self.connect_smtp(message["subject"], message["body"], message["recipient"])
                
            # Sets a timeout after one message sends
            time.sleep(10)
    
        print("Successful")   
        
        
if __name__ == "__main__":
    mail_instance = Mail()
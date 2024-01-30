import os
import smtplib
import time
from dotenv import load_dotenv

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
        # Message Array
        messages = [
            {
                "subject": "General",
                "body": "Nnorom"
            },
            {
                "subject": "Special",
                "body": "Christian"
            }
        ] 
        
        # Who receives the mail
        recipient_email = "nnorom.peace44@gmail.com"
        
        # Loops through the array messages 
        for message in messages:
            # Sends Each Message
            self.connect_smtp(message["subject"], message["body"], recipient_email)
            # Sets a timeout after one message sends
            time.sleep(10)
    
        print("Successful")   
        
        
if __name__ == "__main__":
    mail_instance = Mail()
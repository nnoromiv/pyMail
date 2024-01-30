# Python Auto Send Mail

- Author: **NNOROM CHRISTIAN**
- Github: **[NNOROMIV](https://github.com/nnoromiv)**

This is a google integrated mail sender, The bot uses google App Password connected to users account to send mails with a timeout of 3 minutes.
Timeout can be adjusted.

## Functionalities

- Messages are read from the `messages.json` file
- Sends Mails to Requested Recipient else falls to default Recipient.
- Sends the mail one after the other in respect to the time out set.
- Kills the system when all is sent.
  
## Usage

Clone repository

```bash
    git clone https://github.com/nnoromiv/pyMail.git
```

Install Requirements

```bash
    pip install -r requirements.txt
```

Create `.env` file in the directory and populate with data similar to

```env
    SERVER=smtp.gmail.com
    PORT=587
    EMAIL=**YOUR_EMAIL**
    PASSWORD=**GOOGLE_MAIL_APP_PASSWORD**
    RECIPIENT=**RECIPIENT_EMAIL**
    SENDER_NAME=**YOUR_NAME**
    CARBON_COPY=**SPECIFIC_MAIL_TO_COPY_TO OR CAN_BE_EMPTY**
```

Populate your `messages.json` file with required information. If is recipient the bot send the mail to the given general mail in the `.env`

```json
    [
        {
            "subject": "YOUR_MAIL_SUBJECT",
            "body": "YOUR_MAIL_BODY",
            "recipient": "SPECIFIC_MAIL OR CAN_BE_EMPTY"
        },
    ]
```

Run the program

```bash
    python main.py
```

## Contribution

You can make pull request to the system.

## License

This program adopts the MIT [License](./LICENSE)

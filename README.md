<p align="center"><img src="https://github.com/Liammkr/WSTMAIL/blob/main/WSTLOGO.png"height="200"></p>



[![Deploy to Heroku](https://binbashbanana.github.io/deploy-buttons/buttons/remade/heroku.svg)](https://heroku.com/deploy/?template=https://github.com/Liammkr/WSTMAIL)
[![Run on Replit](https://binbashbanana.github.io/deploy-buttons/buttons/remade/replit.svg)](https://replit.com/github/Liammkr/WSTMAIL)
[![Deploy on Railway](https://binbashbanana.github.io/deploy-buttons/buttons/remade/railway.svg)](https://railway.app/new/template?template=https://github.com/Liammkr/WSTMAIL)
[![Remix on Glitch](https://binbashbanana.github.io/deploy-buttons/buttons/remade/glitch.svg)](https://glitch.com/edit/#!/import/github/Liammkr/WSTMAIL)
[![Deploy to Koyeb](https://binbashbanana.github.io/deploy-buttons/buttons/remade/koyeb.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/Liammkr/WSTMAIL&branch=main&name=WSTMAIL)

<a href='https://github.com/Liammkr/WSTMAIL'>View Source</a>

WSTMAIL is a Python script designed to automate the sending of multiple emails through Simple Mail Transfer Protocol (SMTP). It provides a simple command-line interface for users to input sender details, recipient information, and email content, enabling the rapid dispatch of emails for various purposes such as notifications, alerts, or announcements.

Features:
- Customizable Email Content: Users can input the subject and body of the email, allowing for personalized messages tailored to the recipient.
- Multiple Recipients: Although this version of the script currently supports sending emails to a single recipient, it can be easily extended to handle multiple recipients by modifying the code accordingly.
- Error Handling: Basic error handling is implemented to handle authentication errors and connection issues with the SMTP server.
- Colored Output: The script utilizes the colorama library to provide colorful output, enhancing user experience and making the process more visually appealing.

Requirements:
- Python 3.x: The script is written in Python 3 and requires a compatible interpreter to run.
- smtplib Library: This standard library module provides functionality for sending emails via SMTP.
- email.message Module: Used for creating email message objects with specified content and metadata.
- colorama Library: Utilized for colorful console output, enhancing readability and user interaction.

Usage:
1. Clone the Repository: Begin by cloning the Email-Spammer repository to your local machine using Git.
   ```
   git clone https://github.com/Liammkr/WSTMAIL.git
   ```

3. Install Dependencies: Navigate to the project directory and install the required dependencies using pip.
   ```
   cd Downloads/WSTMAIL-main 
   pip install -r requirements.txt
   ```

3. Run the Script: Execute the Python script to start the email-spamming process. Follow the prompts to provide the necessary information, including sender email, sender app password (for Gmail), recipient email, subject, body, and the number of emails to send.
   ```
   python WSTMAIL.py
   ```

5. Sit Back and Relax: Once the script is running, it will send the specified number of emails with the provided details. Monitor the console output for progress updates and status messages.

Configuration:
- Sender Email and Password: Ensure that you have the correct sender email and password (app password for Gmail) configured in the script. For Gmail users, it is recommended to enable "less secure app access" or use app passwords for authentication.
- SMTP Server Configuration: By default, the script uses the SMTP server provided by Gmail (smtp.gmail.com), but you can modify this to use a different SMTP server if required.

Disclaimer:
This script is intended for educational purposes and should be used responsibly and ethically. Sending unsolicited or spam emails is against the terms of service of most email providers and may result in penalties or account suspension. Always obtain consent from recipients before sending emails and comply with relevant laws and regulations governing email communications.

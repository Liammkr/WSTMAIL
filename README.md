<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email-Spammer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 0 20px;
        }

        h1 {
            color: #007bff;
        }

        h2 {
            color: #28a745;
        }

        p {
            margin-bottom: 15px;
        }

        code {
            background-color: #f8f9fa;
            padding: 2px 6px;
            border-radius: 4px;
        }

        pre {
            background-color: #f8f9fa;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>Email-Spammer</h1>
        <p>Email-Spammer is a Python script designed to automate the sending of multiple emails through Simple Mail Transfer Protocol (SMTP). It provides a simple command-line interface for users to input sender details, recipient information, and email content, enabling the rapid dispatch of emails for various purposes such as notifications, alerts, or announcements.</p>

        <h2>Features</h2>
        <ul>
            <li><strong>Customizable Email Content:</strong> Users can input the subject and body of the email, allowing for personalized messages tailored to the recipient.</li>
            <li><strong>Multiple Recipients:</strong> Although this version of the script currently supports sending emails to a single recipient, it can be easily extended to handle multiple recipients by modifying the code accordingly.</li>
            <li><strong>Error Handling:</strong> Basic error handling is implemented to handle authentication errors and connection issues with the SMTP server.</li>
            <li><strong>Colored Output:</strong> The script utilizes the <code>colorama</code> library to provide colorful output, enhancing user experience and making the process more visually appealing.</li>
        </ul>

        <h2>Requirements</h2>
        <ul>
            <li><strong>Python 3.x:</strong> The script is written in Python 3 and requires a compatible interpreter to run.</li>
            <li><strong>smtplib Library:</strong> This standard library module provides functionality for sending emails via SMTP.</li>
            <li><strong>email.message Module:</strong> Used for creating email message objects with specified content and metadata.</li>
            <li><strong>colorama Library:</strong> Utilized for colorful console output, enhancing readability and user interaction.</li>
        </ul>

        <h2>Usage</h2>
        <ol>
            <li><strong>Clone the Repository:</strong> Begin by cloning the Email-Spammer repository to your local machine using Git.</li>
            <pre>git clone https://github.com/yourusername/email-spammer.git</pre>
            <li><strong>Install Dependencies:</strong> Navigate to the project directory and install the required dependencies using pip.</li>
            <pre>cd email-spammer<br>pip install -r requirements.txt</pre>
            <li><strong>Run the Script:</strong> Execute the Python script to start the email-spamming process. Follow the prompts to provide the necessary information, including sender email, sender app password (for Gmail), recipient email, subject, body, and the number of emails to send.</li>
            <pre>python email_spammer.py</pre>
            <li><strong>Sit Back and Relax:</strong> Once the script is running, it will send the specified number of emails with the provided details. Monitor the console output for progress updates and status messages.</li>
        </ol>

        <h2>Configuration</h2>
        <ul>
            <li><strong>Sender Email and Password:</strong> Ensure that you have the correct sender email and password (app password for Gmail) configured in the script. For Gmail users, it is recommended to enable "less secure app access" or use app passwords for authentication.</li>
            <li><strong>SMTP Server Configuration:</strong> By default, the script uses the SMTP server provided by Gmail (<code>smtp.gmail.com</code>), but you can modify this to use a different SMTP server if required.</li>
        </ul>

        <h2>Disclaimer</h2>
        <p>This script is intended for educational purposes and should be used responsibly and ethically. Sending unsolicited or spam emails is against the terms of service of most email providers and may result in penalties or account suspension. Always obtain consent from recipients before sending emails and comply with relevant laws and regulations governing email communications.</p>
    </div>
</body>

</html>

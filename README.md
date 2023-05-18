# TwilioMessage
This basic Python script demonstrates how to use the Twilio API to send an SMS message.

## Prerequisites

Before running this script, make sure you have the following:

- Python installed on your machine
- The `twilio` library installed (`pip install twilio`)

## Configuration

Before running the script, you need to provide your Twilio account credentials. Follow these steps:

1. Sign up for a Twilio account at https://www.twilio.com/ if you haven't already.
2. Retrieve your Account SID and Auth Token from the Twilio console.
3. Open the `main.py` file and locate the following lines:

    ```
    account_sid = "sid here"
    auth_token = "auth here"
    ```

4. Replace `"sid here"` with your Twilio Account SID and `"auth here"` with your Twilio Auth Token.

## Usage

To send an SMS message using this script, follow these steps:

1. Open the terminal or command prompt.
2. Navigate to the directory where the `main.py` file is located.
3. Run the script by executing the following command:

    ```
    python main.py
    ```

4. The script will send an SMS message with the content "hello world" to the specified phone number. Replace `"number here"` in the script with the recipient's phone number, including the country code.

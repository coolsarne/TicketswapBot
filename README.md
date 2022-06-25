# Ticketswap Bot
Bot for ticketswap.be that allows users to reserve tickets for festivals,...  
Bot automatically checks for tickets  
Bot sends notification when ticket is reserved  
Bot doesn't auto checkout  
Bot doesn't confirm email address for login by itself

## Requirements
- Python 3
- Google Chrome
- ChromeDriver

## Usage
1. Clone the project:
   ```
   $ git clone https://github.com/coolsarne/TicketswapBot.git
   ```

2. Install dependencies:
    ```
    $ cd TicketswapBot
    $ pip3 install -r requirements.txt   
    ```

3. Download [ChromDriver](https://chromedriver.chromium.org/downloads) for your version of Google Chrome, extract the executable, and place it in the root directory:

    ```
    TicketswapBot/
    ├── bot.py
    ├── ...
    ├── chromedriver
    ```

4. Fill in the `settings.json`:

    ```  
    {
        "ticket": {
            "eventLink": "",                 -- link to ticket overview page of event
            "otherCategory": "",             -- if ticket is not in default list, but in 'others' or 'overig', fill 
                                                this category in here, if not, leave empty
            "ticketName": "",                -- full name of ticket as shown in overview page
            "amount": 1                      -- preffered amount of tickets to buy (at least 1)
        },
        "login": {
            "email": "",                     -- email address used to login, make sure its already registered
        },
        "notification": {
            "email": "",                     -- email address to send notification to when ticket is reserved
            "phone": ""                      -- phone number to call when ticket is reserved
        }
    }
    ```

5. Run the bot:
   ```
   $ python3 main.py
   ```
   \* To avoid accidental charges, payment info needs to be filled in **manually**

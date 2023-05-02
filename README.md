# kko_nabor

## Prerequisites

1. [Python](https://python.org/) version 3.8 or later
2. pip or pip3
3. Bot [token](https://dev.vk.com/api/bots/getting-started#%D0%9F%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BA%D0%BB%D1%8E%D1%87%D0%B0%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%B0) for VK API
4. Service account for google API with [Google Sheets API](https://developers.google.com/sheets/api/quickstart/python) enabled 


## Build locally
### Installing requirements
1. Clone this repo 

    ```shell
    git clone https://github.com/TechDepSut/kko_nabor.git
    ```
2. Create virtual environment 
    
    - For Windows:

        ```Powershell
        python -m venv .venv
        ```

    - For Linux, MacOS:
    
        ```shell
        python3 -m venv .venv
        ```

3. Activate virtual environment

    - For Windows:
    
        ```Powershell
        .\.venv\Scripts\activate
        ```

    - For Linux, MacOS:

        ```shell
        source ./.venv/bin/activate
        ```

4. Install requirements

    - For Windows:

        ```shell
        pip install -r requirements.txt
        ```

    - For Linux, MacOS:
    
        ```shell
        pip3 install -r requirements.txt
        ```

1. Setting environment variables

    - For Windows:

        + Powershell:

            ```Powershell
            $env:TOKEN="TOKEN_TO_YOUR_BOT";
            ```
            ```Powershell
            $env:service_file="SERVICE_FILE_FOR_GOOGLE_API";
            ```
        
        + cmd:

            ```cmd
            set TOKEN=TOKEN_TO_YOUR_BOT
            ```
            ```cmd
            set service_file="SERVICE_FILE_FOR_GOOGLE_API"
            ```

    - For Linux, MacOS:

        + Bash:

            ```shell
            export TOKEN="TOKEN_TO_YOUR_BOT"
            ```
            ```shell
            export service_file="SERVICE_FILE_FOR_GOOGLE_API"
            ```

6. Run bot

    - For Windows:

        ```shell
        python .\src\bot.py
        ```

    - For Linux, MacOS:
    
        ```shell
        python3 ./src/bot.py
        ```
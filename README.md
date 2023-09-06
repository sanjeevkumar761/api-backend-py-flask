
https://www.geeksforgeeks.org/python-build-a-rest-api-using-flask/  

Install git  
      Based on your OS, install git  

Install SQLite  
1. Depending upon your OS, download zip file from https://www.sqlite.org/download.html  
2. Unzio the contents and add sqlite3 DLL to PATH  
3. Restart VS Code
4. Run command "cat SAPTables.sql | sqlite3 SAPDatabase.db"  
5. Make sure the file "SAPDatabase.db" is created  

Setup app  
1. Install Python 3.10.11  
2. Install VCRuntime from this link https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022  
3. Install Python 3.8 and create python virtual enviornment (details https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/  )   
      pip install virtualenv  
      python -m venv backendenv  
4. Activate virtual environment  
      source backendenv/Scripts/activate    
5. Install packages  
    pip install -r requirements.txt  
6. Create a file ".env" and enter following key value pairs  
      FLASK_APP=app
      OPENAI_API_KEY=<Your OPENAI API key>
7. Run the app with command "flask run"  



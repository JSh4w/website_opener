## Simple Website Opener
Given a set of URL's will open them in a window
Can save the list of URL's as a JSON and load them
If you have a series of websites you open up often this can be handy, quicker than opening chrome and opening a group. 

## Building the Application

To build the application and create the executable, follow these steps for Windows:

1. **Install Required Packages**:
   Make sure you have `pyinstaller` installed:
   ```bash
   pip install pyinstaller
   ```

2. **Navigate to Your Project Directory**:
   Open your terminal or command prompt and navigate to the directory where `website_launcher.py` is located:
   ```bash
   cd path/to/your/project
   ```

3. **Build the Executable**:
   Run the following command to create the executable:
   ```bash
   pyinstaller --onefile website_launcher.py
   ```

4. **Locate the Executable**:
   After the build process completes, find the executable in the `dist` folder:
   ```
   your-project-name/
   ├── build/
   ├── dist/
   │   └── website_launcher.exe
   ├── website_launcher.py
   ├── requirements.txt
   └── README.md
   ```

5. **Test the Executable**:
   Navigate to the `dist` folder and run the executable to ensure it works:
   ```bash
   cd dist
   ./website_launcher.exe  # On Windows
   ```

6. **Shortcut to exectuable**:
    From file explorer right click and make a shortcut to the executable

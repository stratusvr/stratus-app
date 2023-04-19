## Installing Python and Git

Before starting, make sure you have Python and Git installed on your computer. If you don't, follow the instructions below to install them:

### Windows

#### Installing Python

1. Visit the Python downloads page: https://www.python.org/downloads/windows/
2. Download the latest Python installer for Windows by clicking on the "Download Windows x86-64 executable installer" link.
3. Run the installer, making sure to check the box that says "Add Python to PATH" before clicking "Install Now."

#### Installing Git

1. Visit the Git downloads page: https://git-scm.com/download/win
2. The download should start automatically. If it doesn't, click on the "Click here to download manually" link.
3. Run the installer and follow the prompts, accepting the default options.

### Mac

#### Installing Python

1. Visit the Python downloads page: https://www.python.org/downloads/mac-osx/
2. Download the latest Python installer for Mac by clicking on the "Download macOS 64-bit Intel installer" link.
3. Run the installer and follow the prompts.

#### Installing Git

1. Open Terminal (search for "Terminal" in Spotlight).
2. Enter the following command and press Enter: `xcode-select --install`
3. A pop-up window will appear, click "Install" to install the command line developer tools, which includes Git.

## Running the Application

Now that Python and Git are installed, follow these steps to run the application:

### Windows

1. Press the Windows key, type "cmd," and press Enter to open the Command Prompt.
2. Enter the following command to clone the repository and press Enter:

<code>git clone https://github.com/stratusvr/stratus-app</code>

3. Change to the newly created directory with this command:

<code>cd stratus-app</code>

4. Install the required packages by running:

<code>pip install -r requirements.txt</code>

5. Start the application with this command:

<code>python main.py</code>



### Mac

1. Open Terminal (search for "Terminal" in Spotlight).
2. Enter the following command to clone the repository and press Enter:

<code>git clone https://github.com/stratusvr/stratus-app</code>

3. Change to the newly created directory with this command:

<code>cd stratus-app</code>

4. Install the required packages by running:

<code>pip3 install -r requirements.txt</code>

5. Start the application with this command:

<code>python3 main.py</code>

The application should now be running. If you encounter any issues, make sure you have the latest versions of Python and Git installed, and carefully review the steps above.

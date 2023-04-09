# Stratus VR
![alt text](logo.png)

Thank you for your interest in Stratus! We're hard at work building out our platform, but we wanted to invite a select few users to be the some of the first to try it out. 

Please note that this beta test is an early-stage build of our platform and may not reflect what the final product will look like or function. You may encounter bugs or technical issues during this beta test, this is to be expected. We ask that you let us know of any issues you encounter through this form. 

## Pre-requisites:
1. A Meta Quest or Meta Quest 2 Headset (and a USB-C cord)
2. A PC/Mac/Linux Computer installed with Python and Android Device Bridge (https://www.vrtourviewer.com/docs/adb/)
3. An internet speed of 50+ Mbps 

## Installation Instructions:
1. Please ensure that you have Python and Android Device Bridge installed on your computer and that your headset is plugged in
2. Clone this repository
<code>git clone https://github.com/stratusvr/stratus-app</code>
3. Enter the directory and install the required packages
<code>pip install -r requirements.txt</code>
4. Run the application
<code>python main.py</code>

## Usage Instructions:
1. Navigate to https://main.d3vh7zst60d70i.amplifyapp.com/
2. Sign up for an account, login, and proceed to the dashboard
3. Start your Stratus session by clicking the <code>Launch Session</code> button
4. Make note of the IP address you are given (it can be retrieved with the <code>Retrieve IP Address</code> button)
5. Go to your running Stratus desktop application
6. Install the Stratus VR application to your headset my clicking the <code>Install Application</code> button
7. Type the IP address from the website into the text box, then click the <code>Push to Headset</code> button
8. Launch the CloudXR application on your headset (It will be in the "Unidentified Developers" section of your library)
9. Please note, the application will likely crash on its first launch, please try launching the application again to connect to your Stratus session
10. Once connected, you will see the SteamVR 'Void'
11. While in the 'Void', open the SteamVR menu (left menu button)
12. Launch Adventure Climb VR and start playing
13. Your session will automatically be terminated after 30 minutes

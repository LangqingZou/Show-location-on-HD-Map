# Show-location-on-HD-Map
## Table of contents
* [General info](#general-info)
* [Setup](#Setup)
* [How to run it](#How-to-run-it)

## General info
This project involves displaying your laptop's address on the Ottawa HD Map via the OpenHDMaps platform. <br>
The application will get the location of laptop via this website https://www.itilog.com/en/where-am-i.<br>
<img width="700" alt="图片" src="https://user-images.githubusercontent.com/55254825/162124151-ef32919b-b68b-45b7-8e48-e157588627fc.png"><br>
Then, the location will be showed on the Ottawa HD Map in OpenHDMaps platform.<br>
<img width="700" alt="图片" src="https://user-images.githubusercontent.com/55254825/162124420-9083deec-28da-49e3-994b-924bda63b85f.png">

	
## Setup
### Environment
1. Make sure you have Chrome.
2. If you are using MAC OS system, go to System Preferences.
3. In Security & Privacy, allow Google Chrome to determine your location.
### Technologies
Project is created with:<br>
**Language:**<br>
Python version: 3.9<br>
**Modules need to be imported:**<br>
If you are using MAC OS system, install modules by these commands:
1. Selenium<br>
> pip install Selenium
2. ChromeDriverManager<br>
> pip install ChromeDriverManager


## How to run it
There are two methods to run this project:
### The first method - easy one
1. Download the file named *HD Map Application*
2. Find the file named *dist*
3. There are two files in *dist*. The first one is an exe file, and the second one is openHDMaps.app. If you are using MAC OS system, feel free to right click any one of them. If you are using Windows, right click the second one.<br>
   <img width="249" alt="图片" src="https://user-images.githubusercontent.com/55254825/162119295-0fb3ec4c-0914-4cb5-8eb0-18a08663a9bb.png">

### The second method
1. Go though the setup part and install all modules needed
2. Download the file named *HD Map Application*
3. Open the *HD Map Application* with any IDE. Here, I suggest Visual Studio Code.
4. Run the python script named *openHDMaps.py*

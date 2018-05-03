## IOTBit 3G HAT Configuration and Driver Installation

### Driver Compatibility
Trial | Operating System | Kernel Version | Release Date | Does it work? (PASS/FAIL) | Install Notes
------|------------------|----------------|--------------|---------------------------|--------------
1 | Raspbian Jessie | Kernel 4.14 | Release 2018-04-18 | FAIL | GCC does not recognize version, no clue how the drivers work
2 | IOTBITQMI Modified Raspbian Jessie | Kernel 4.9 | Release 2017-08-17 | FAIL | Module does not load. "exec" format issue.
3 | Ubuntu Mate 16.04.2 | Kernel 4.4 | Release 2016-04-21 | FAIL | Driver loads. Device is not functional. Finally starting to understand how the driver works.
4 | Raspbian Jessie | Kernel 4.4 | Release 2016-11-29 | PASS | Driver loads. Device is functional and connects to the internet! Finally mastered the install process.

Overall Driver Installation Experience - :dizzy_face: / 10 

### IOTBit 3G HAT Driver Installation and Setup Procedure
Company - "Altitude-Tech"
Repo - "IOTBit_Install"
Device - IOTBit 3G HAT

1. Flash your SD card with the following image: (Raspbian Jessie - K4.4 - 2016-11-29)[http://downloads.raspberrypi.org/raspbian/images/raspbian-2016-11-29/2016-11-25-raspbian-jessie.zip]
2. Boot into Raspbian on the Pi and open up terminal.
3. Type `lsusb | grep Qualcomm`, you should see a red highlighted text with Qualcomm. If not, please reconnect the board with better USB cables. If problem persists, please contact Altitude Tech.
4. Clone the repo: `git clone https://github.com/Altitude-Tech/IOTBit_Install`
5. Change directory to driver folder: `cd IOTBit_Install`
6. Edit driver script: `sudo nano IOTBit_Install.sh`
  - In line 9, change `rpi-source` to `rpi-source --skip-gcc`
  - Save changes: `Ctrl-O and Enter`
  - Exit nano: `Ctrl-X`
7. Change driver permissions: `sudo chmod IOTBit_Install.sh`
8. Install the driver: `sudo ./IOTBit_Install.sh` This will take a a few minutes, depending on your internet speed.
9. Reboot the pi: `sudo reboot`
10. Check if driver is installed properly: `lsmod | grep GobiSerial`
  - If driver is installed properly, the command should show two lines with RED highlighted text
  - If driver isn't installed properly, no response is produced and cursor moves to next line. Repeat steps 1-11 to re-install drivers properly.
11. Change directory to driver folder: `cd IOTBit_Install`
12. Edit WVDial Configuration File : `sudo nano wvdial.config`
  - On line 2, remove `S0=0`.
  - On line 3, change `YOUR.SIMCARD_APN.HERE` to your Carrier's APN. 
  - For our project, this is `pda.bell.ca`
  - Save changes: `Ctrl-O and Enter`
  - Exit nano: `Ctrl-X`
13. Backup a copy of System's wvdial.config file: `sudo mv /etc/wvdial.conf /etc/wvdial.conf.bak`
14. Move edited WVDial Configuration file to system directory: `sudo mv /home/pi/IOTBit_Install/wvdial.conf /etc/wvdial.conf`
15. Reconfigure the WVDial Configuration file to system requirements: `sudo wvdialconfig /etc/wvdial.conf`
16. Dial to the carrier network: `sudo wvdial`
  - You should see the following lines as the command executes.
    - `CONNECT 115200`
    - `--> Carrier detected. Starting PPP immediately.`
17. Open another terminal window or tab.
18. Add ppp0 network interface as default in routing table: `sudo route add default ppp0`
19. Open a browser and type `google.com`. 
20. Voila. Setup Complete! :clap::clap::clap::clap:
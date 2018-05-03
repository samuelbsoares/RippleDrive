## Project Ripple Drive
Creating a diagnostic and performance tool for measuring wave-height and piston pressure for a Wave Energy Converter called Bob.

### Project To-dos
- [ ] Create a Setup.sh bash script to install all the drivers.
  - [ ] Install i2c-tools using a bash script.
  - [ ] Create a 3G HAT driver install script.
  - [ ] Create a FT-232H driver install script.
  - [ ] Create diagnostic toolkit that checks all crucial devices
      - [ ] FT-232H
      - [ ] ADS 1115
      - [ ] MPU 6050 and MPU 9250
      - [ ] 3G HAT
      - [ ] The Pi itself
        - [ ] Network issues
        - [ ] O.S. issues
        - [ ] SD card space (low space warning)
- [ ] Test Setup.sh
- [ ] Create a wave recording file (More info on this soon). 
- [ ] Create PCB designs
  - [ ] Create PCB design for Raspberry Pi's gyroscope (MPU-9250)
  - [ ] Create PCB design for Power Management (ADS 1115)
  - [ ] Create PCB design for the extended gyroscope (FT-232H and MPU-6050)
- [ ] Send PCB designs to manufacturers



### Update May 2nd, 2018
- Altitude Tech's IOTBit 3G HAT finally works! [Good News :+1:]
- Mahen has added the [driver compatibility and install instructions](https://github.com/samuelsoares/RippleDrive/blob/master/3G_HAT/readme.md) for the 3G HAT. [Good News :+1:]
- ADS 1115 is not working. Maybe the chip is fried? [Bad News :-1:]
- More people could work on the designing PCBs [Suggestion :star:]

### Project Contributors
* @samuelbsoares - Samuel B. Soares
* @gpfenniger - Griffin Pfenniger
* @mahkrish - Mahen Krishnakumar
* @marcelogaia - Marcelo Gaia
* @Chris-Horan - Chris Horan

### Sensor Documentation
- [FT-232H Documentation](http://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT232H.pdf)

- MPU-9250
  - [Datasheet](https://www.invensense.com/wp-content/uploads/2015/02/PS-MPU-9250A-01-v1.1.pdf)
  - [Register Maps](http://www.invensense.com/wp-content/uploads/2017/11/RM-MPU-9250A-00-v1.6.pdf)
  
- MPU-6050
  - [Datasheet](https://www.invensense.com/wp-content/uploads/2015/02/MPU-6000-Datasheet1.pdf)
  - [Register Maps](https://www.invensense.com/wp-content/uploads/2015/02/MPU-6000-Register-Map1.pdf)
  
- ADS 1115
  - [Datasheet](http://www.ti.com/lit/ds/symlink/ads1115.pdf)

### Languages and Open Source Libraries in use
- Python 2.7
- [Adafruit Python GPIO Library](https://github.com/adafruit/Adafruit_Python_GPIO)
- [libusb](https://github.com/libusb/libusb)
- [libftdi](https://www.intra2net.com/en/developer/libftdi/)

### [Langara Software Developers Club](https://www.facebook.com/langarasdc)

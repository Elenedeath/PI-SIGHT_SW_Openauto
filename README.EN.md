# PI-SIGHT SW - Openauto

'Openauto' allows [PI-SIGHT](https://github.com/younsj97/PI-SIGHT_Helmet_HUD) to be used as an Android Auto head unit, and is created by modifying the [Crankshaft](https://github.com/opencardev/crankshaft) software to suit PI-SIGHT.


## function

 - When you connect to an Android smartphone via PI-SIGHT’s hotspot, you can see the Android Auto screen through the prism display in front of you.
 - The rear camera supports loop recording, which continuously records and automatically deletes the oldest video when the memory is full. The rear camera video can also be output to the display, allowing you to view the rear in real time while driving.
 - You can use Google Assistant through the built-in microphone and perform various actions such as setting destinations, playing music, and making calls using your voice.
 - Basically, you need a Bluetooth audio device like Sena to listen to your smartphone inside the helmet, but if you connect the PI-SIGHT external Bluetooth audio module, you can integrate it into a single device without a separate Bluetooth audio device.
 - For more information, please visit the [VUDEV website](https://sites.google.com/vudev.net/vudevnet/openauto-info) or download the [manual](https://github.com/younsj97/PI-SIGHT_SW_Openauto/blob/main/PI-SIGHT%20%EC%82%AC%EC%9A%A9%EC%84%A4%EB%AA%85%EC%84%9C-3%20(%EC%98%A4%ED%94%88%EC%98%A4%ED%86%A0).pdf).


## installation

 1. Download and install the [Raspberry Pi imager](https://www.raspberrypi.com/software/) app.
 2. After downloading all [split compressed software files](http://naver.me/IxscSsEt), unzip them to create the Openauto-16GB-yymmdd.img file.
 3. Run the Raspberry Pi imager, connect the MicroSD to the PC, and select Erase to format the memory.
 4. Once the format is complete, select Use Custom and select the Openauto-16GB-yymmdd.img file. (Do not use any custom settings including SSH.)


## caution

 - _Currently, Openauto only works on Android Auto versions lower than 12.7. Until the issue is resolved, please uninstall Android Auto updates from the Play Store on your phone, disable automatic app updates, and download and install the [12.6 version apk file](https://www.apkmirror.com/apk/google-inc/android-auto/android-auto-12-6-6432-release/android-auto-12-6-643254-release-android-apk-download/)._
 - _Openauto-16GB-yymmdd.img firmware can be installed on a 16GB microSD memory._
 - If you want to increase the storage period of the rear camera video by using a memory card larger than 32GB, first install the 16GB firmware, then [increase the boot partition size using GParted.](https://learn.adafruit.com/resizing-raspberry-pi-boot-partition/edit-partitions)_


## Customizing

 - For system configuration and details, see the [Crankshaft Wiki](https://github.com/opencardev/crankshaft/wiki/Getting-started-with-Crankshaft).
 - If you want to apply PI-SIGHT Openauto customizations from the basic Crakshaft Openauto system, please refer to the [setup instructions](https://vudev.notion.site/Openauto-1872b35c59624c85a099c0787b978a32?pvs=4).
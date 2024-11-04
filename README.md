# PI-SIGHT SW - Openauto

'Openauto'는 [PI-SIGHT](https://github.com/younsj97/PI-SIGHT_Helmet_HUD)를 안드로이드 오토 헤드 유닛으로 사용할 수 있도록 하며, [Crankshaft](https://github.com/opencardev/crankshaft) 소프트웨어를 PI-SIGHT에 적합하게 수정하여 만들어졌습니다.


## 기능

 - PI-SIGHT의 핫스팟을 통해 안드로이드 스마트폰과 연결하면, 눈앞의 프리즘 디스플레이를 통해 안드로이드 오토 화면을 볼 수 있습니다.
 - 후방 카메라는 상시 녹화되고 메모리가 가득 차면 자동으로 가장 오래된 영상을 지우는 루프 레코딩 기능을 지원하며, 후방카메라 영상을 디스플레이에 출력해 주행 중 실시간으로 뒤를 볼 수도 있습니다. 
 - 내장 마이크를 통해 구글 어시스턴스를 사용할 수 있고, 목적지 설정, 음악 재생, 전화 걸기 등 다양한 동작을 음성으로 실행할 수 있습니다.
 - 기본적으로 헬멧 안에서 스마트폰의 소리를 듣기 위해 세나 같은 블루투스 오디오 장치가 필요하지만, PI-SIGHT 외장 블루투스 오디오 모듈을 연결하면 별도의 블루투스 오디오 장치 없이 하나의 디바이스로 통합할 수 있습니다.
 - 자세한 내용은 [VUDEV 웹사이트](https://sites.google.com/vudev.net/vudevnet/openauto-info) 또는 [설명서](https://github.com/younsj97/PI-SIGHT_SW_Openauto/blob/main/PI-SIGHT%20%EC%82%AC%EC%9A%A9%EC%84%A4%EB%AA%85%EC%84%9C-3%20(%EC%98%A4%ED%94%88%EC%98%A4%ED%86%A0).pdf)를 다운로드하여 확인하세요


## 설치

 1. [라즈베리파이 imager](https://www.raspberrypi.com/software/) 앱을 다운로드하고 설치하세요
 2. [분할압축된 소프트웨어 파일](http://naver.me/IxscSsEt)을 모두 다운로드한 후, 압축을 해제하여 Openauto-16GB-yymmdd.img 파일을 만드세요.
 3. 라즈베리파이 imager를 실행하고, MicroSD를 PC에 연결한 뒤, Erase를 선택하여 메모리를 포맷하세요.
 4. 포맷이 완료되면, Use Custom을 선택하여 Openauto-16GB-yymmdd.img 파일을 선택하세요. (SSH를 비롯한 커스텀 세팅은 사용하지 마세요.)


## 주의사항

 - _현재 Openauto는 안드로이드 오토 12.7 미만의 버전에서만 정상 작동합니다. 문제가 해결되기 전까지는 스마트폰의 플레이스토어에서 안드로이드 오토 업데이트를 삭제하고 앱 자동 업데이트를 비활성한 뒤, [12.6 버전의 apk 파일](https://www.apkmirror.com/apk/google-inc/android-auto/android-auto-12-6-6432-release/android-auto-12-6-643254-release-android-apk-download/)을 다운로드하고 설치해 사용하세요._
 - _Openauto-16GB-yymmdd.img 펌웨어는 16GB microSD 메모리에 설치할 수 있습니다._
 - _32GB 이상의 메모리 카드를 사용해 후방카메라 영상의 저장 기간을 늘리고 싶은 경우, 우선 16GB 펌웨어를 설치한 뒤, [GParted를 통해 boot 파티션 크기를 늘리세요.](https://learn.adafruit.com/resizing-raspberry-pi-boot-partition/edit-partitions)_


## 커스터마이징

 - 시스템 구성 및 세부 정보는 [Crankshaft Wiki](https://github.com/opencardev/crankshaft/wiki/Getting-started-with-Crankshaft)를 확인하세요.
 - 기본 Crakshaft Openauto 시스템으로부터 PI-SIGHT Openauto 커스터마이징을 적용하고 싶은 경우, [설정 방법](https://vudev.notion.site/Openauto-1872b35c59624c85a099c0787b978a32?pvs=4)을 참고하세요.

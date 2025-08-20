name: Build APK

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          sudo apt update
          sudo apt install -y python3-pip python3-setuptools git zip unzip openjdk-17-jdk wget
          pip install cython==0.29.36 buildozer==1.5.0

      - name: Install Android SDK & NDK
        run: |
          sudo mkdir -p /usr/lib/android-sdk/cmdline-tools
          cd /usr/lib/android-sdk/cmdline-tools
          wget https://dl.google.com/android/repository/commandlinetools-linux-9477386_latest.zip -O cmdtools.zip
          unzip cmdtools.zip -d latest
          yes | latest/bin/sdkmanager --sdk_root=/usr/lib/android-sdk --licenses
          yes | latest/bin/sdkmanager --sdk_root=/usr/lib/android-sdk \
            "platform-tools" \
            "platforms;android-31" \
            "build-tools;31.0.0" \
            "ndk;23.1.7779620"

      - name: Build APK
        env:
          ANDROIDSDK: /usr/lib/android-sdk
          ANDROIDNDK: /usr/lib/android-sdk/ndk/23.1.7779620
        run: |
          buildozer -v android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: my-app-apk
          path: bin/*.apk

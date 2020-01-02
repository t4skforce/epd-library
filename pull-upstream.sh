#!/bin/sh
set -e
# pip install --upgrade autopep8

patch_lib () {
  local SOURCE="$1"
  local NAME="$2"
  cp .upstream/${SOURCE}/raspberrypi/python/main.py ./$NAME/__main__.py
  cp .upstream/${SOURCE}/raspberrypi/python/${NAME}.py ./$NAME/__init__.py
  cp .upstream/${SOURCE}/raspberrypi/python/epdif.py ./$NAME/epdif.py
  sed -i "s/^import epdif/from $NAME import epdif/g" ./$NAME/__init__.py
  sed -i 's/\r$//' ./${NAME}/*.py
  autopep8 --in-place --list-fixes --max-line-length 999 -a -a -r ./${NAME}
}

git clone --depth 1 https://github.com/soonuse/epd-library-python.git .upstream

patch_lib "1.54inch_e-paper" "epd1in54"
patch_lib "1.54inch_e-paper_b" "epd1in54b"
patch_lib "1.54inch_e-paper_c" "epd1in54c"
patch_lib "2.13inch_e-paper" "epd2in13"
patch_lib "2.13inch_e-paper_b" "epd2in13b"
patch_lib "2.7inch_e-paper" "epd2in7"
patch_lib "2.7inch_e-paper_b" "epd2in7b"
patch_lib "2.9inch_e-paper" "epd2in9"
patch_lib "2.9inch_e-paper_b" "epd2in9b"
patch_lib "4.2inch_e-paper" "epd4in2"
patch_lib "4.2inch_e-paper_b" "epd4in2b"
patch_lib "7.5inch_e-paper" "epd7in5"
patch_lib "7.5inch_e-paper_b" "epd7in5b"

rm -rf .upstream

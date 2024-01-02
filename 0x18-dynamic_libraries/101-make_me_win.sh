#!/bin/bash
wget -P /tmp https://github.com/abdullahomg77/alx-low_level_programming/raw/master/0x018-dynamic_libbaries/libgiga.so
export LD_PRELOAD=/tmp/libgiga.so

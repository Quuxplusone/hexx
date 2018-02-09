#!/bin/bash

/Applications/DOSBox.app/Contents/MacOS/DOSBox \
    -fullscreen \
    -c 'config -set "cpu cycles=max"' \
    -c "mount c $(pwd)" \
    -c "c:" \
    -c "hexx"

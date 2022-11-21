mkdir /pyboard/lib/

//cp ../adafruit/Adafruit_Blinka/src/rainbowio.py ../adafruit/Adafruit_Blinka/src/digitalio.py /pyboard/lib/

//rsync -m ../adafruit/Adafruit_Blinka/src/adafruit_blinka/ /pyboard/lib/adafruit_blinka/
//rsync -m ../adafruit/Adafruit_CircuitPython_BusDevice/adafruit_bus_device/ /pyboard/lib/adafruit_bus_device/
//rsync -m ../adafruit/Adafruit_CircuitPython_NeoKey/adafruit_neokey/ /pyboard/lib/adafruit_neokey/
//rsync -m ../adafruit/Adafruit_CircuitPython_seesaw/adafruit_seesaw/ /pyboard/lib/adafruit_seesaw/
//cp ../adafruit/Adafruit_CircuitPython_Pixelbuf/adafruit_pixelbuf.py /pyboard/lib/

cp ./typing.py ./socket.py /pyboard/lib/
rsync -m ./badger_ui/badger_ui/ /pyboard/lib/badger_ui/

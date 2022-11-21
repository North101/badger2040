rsync -m ./ahlcg2040/ahlcg2040/ /pyboard/ahlcg2040/
rsync -m ./badger_launcher/badger_launcher/ /pyboard/badger_launcher/
rsync -m ./blaseball2040/blaseball2040/ /pyboard/blaseball2040/
rsync -m ./lotrlcg2040/lotrlcg2040/ /pyboard/lotrlcg2040/
rsync -m ./mahjong2040/mahjong2040/ /pyboard/mahjong2040/
rsync -m ./netrunner2040/netrunner2040/ /pyboard/netrunner2040/
//cp ./device_test.py /pyboard/device_test.py
cp ./main.py /pyboard/main.py

run main.py
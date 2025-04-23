BASE_FILES=main.py
ALL_FILES=$(BASE_FILES) \
		config.py
#		logging \
#		codenerix_lib \

DEVICE=/dev/ttyACM0
SRC=src
MICROPYTHON_IMAGE=bin/PYBV11-20240222-v1.22.2.dfu

FILES = $(shell . ./env/bin/activate && ampy --port $(DEVICE) ls)

default:
	make clean_base
	make upload_base
	make run

all:
	make clean_all
	make upload_all
	make run

clean_base:
	# === Uploading === ======================================================
	$(foreach FILE, $(BASE_FILES), \
		echo "Cleaning $(FILE)..."; \
		. ./env/bin/activate && ampy --port $(DEVICE) rm $(FILE) 2>/dev/null || ampy --port $(DEVICE) rmdir $(FILE); \
	)

clean_all:
	# === Cleaning === =======================================================
	$(foreach FILE, $(FILES), \
		echo "Cleaning $(FILE)..."; \
		. ./env/bin/activate && ampy --port $(DEVICE) rm $(FILE) 2>/dev/null || ampy --port $(DEVICE) rmdir $(FILE); \
	)

upload_base:
	# === Uploading === ======================================================
	$(foreach FILE, $(BASE_FILES), \
		echo "Uploading $(FILE)..."; \
		. ./env/bin/activate && ampy --port $(DEVICE) put $(SRC)/$(FILE); \
	)

upload_all:
	# === Uploading === ======================================================
	$(foreach FILE, $(ALL_FILES), \
		echo "Uploading $(FILE)..."; \
		. ./env/bin/activate && ampy --port $(DEVICE) put $(SRC)/$(FILE); \
	)

run:
	# === Executing === ======================================================
	. ./env/bin/activate && ampy --port $(DEVICE) run $(SRC)/main.py

monitor:
	# === Monitoring === =====================================================
	screen $(DEVICE) 115200

stubs:
	pip install -U  micropython-esp32-stubs --target ./typings --no-user

env:
	virtualenv -p python3 env
	(. ./env/bin/activate && pip install -r requirements.txt)

flash:
	# === Flashing MicroPython === ===========================================
	# Flashing MicroPython into MicroPython board
	(. ./env/bin/activate && dfu-util --alt 0 -s :mass-erase:force -d $(DEVICE) -D $(MICROPYTHON_IMAGE) )

set_flash_voltage:
	-#
	-# === WARNING =============================================================== WARNING ===
	-#
	-# Setting Board Flash Memory Voltage to 3.3V ---> THIS IS FOREVER AND CAN NOT BE UNDONE
	-#
	-# === WARNING =============================================================== WARNING ===
	-#
	-# This will be done in 10 seconds
	sleep 5
	-# This will be done in 5 seconds
	sleep 2
	-# This will be done in 3 seconds
	sleep 1
	-# This will be done in 2 seconds
	sleep 1
	-# This will be done in 1 seconds
	sleep 1
	-# GO
	(. ./env/bin/activate && espefuse.py set_flash_voltage 3.3V)

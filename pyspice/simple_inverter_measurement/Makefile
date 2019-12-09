PROJECT=simple_inverter
SHELL := /bin/bash

mkvenv:
	. `which virtualenvwrapper.sh` && mkvirtualenv -p python3 $(PROJECT)

freeze:
	pip freeze > requirements.txt

install_env:
	pip install -r requirements.txt


autocomplete:
	_QMSCLI_COMPLETE=source ./qmscli > qmscli-complete-bash.sh
	_QMSCLI_COMPLETE=source_zsh  qmscli > qmscli-complete-zsh.sh

pyinstaller_linux:
	pyinstaller --hidden-import=gitlab.v4 --hidden-import=gitlab.v4.objects  --noconfirm --distpath ./dist/linux64 $(PROJECT).py

pyinstaller_win64:
	pyinstaller --hidden-import=gitlab.v4 --hidden-import=gitlab.v4.objects  --noconfirm --distpath ./dist/win64 $(PROJECT).py

pyinstaller_osx:
	pyinstaller --hidden-import=coloredlogs --hidden-import=gitlab.v4 --hidden-import=gitlab.v4.objects  --noconfirm --distpath ./dist/osx $(PROJECT).py

pyinstaller_linux_dbg:
	pyinstaller --hidden-import=gitlab.v4 --debug=imports --distpath ./dist/linux64 $(PROJECT).py

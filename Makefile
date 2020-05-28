# Brew installs or upgrades a package based on what version is installed already if any
define install_or_upgrade
	HOMEBREW_NO_AUTO_UPDATE=1 brew `brew ls --versions "$(1)" | wc -l | xargs expr | sed 's/0/install/' | sed 's/1/upgrade/'` "$(1)"
endef

dev:
	$(call install_or_upgrade,pre-commit)
	$(call install_or_upgrade,awk)

pip:
	pip install -r requirements.txt

init: dev pip
	pip install --upgrade pip
	pip install -r dev-requirements.txt
	pip install -r test-requirements.txt
	pre-commit install

isort:
	isort --recursive .

lint:
	pycodestyle . && isort --check-only --recursive .

test: lint
	coverage run -m unittest discover -p "*_test.py"
	coverage report -m
	coverage xml
all:
	./build

init:
	@mkdir -p database
	./application initdb

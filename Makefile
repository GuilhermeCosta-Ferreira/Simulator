.PHONY: format diagram dev

diagram:
	plantuml -tpng docs/class.puml

format:
	docformatter --in-place --recursive --wrap-summaries 88 --wrap-descriptions 88 src/simulator
	black src/simulator/

dev: diagram format

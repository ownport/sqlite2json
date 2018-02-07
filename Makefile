PYTHON ?= /usr/bin/env python3
PROJECT_NAME ?= sqlite2json
PROJECT_NAME_SRC ?= src 
PROJECT_VERSION ?= 0.1.1

clean:
	@ echo "[INFO] Cleaning directory:" $(shell pwd)/target
	@ rm -rf $(shell pwd)/target
	@ echo "[INFO] Cleaning files: *.pyc"
	@ find . -name "*.pyc" -delete
	@ echo "[INFO] Cleaning files: .coverage"
	@ rm -rf $(shell pwd)/.coverage

compile: clean
	@ echo "[INFO] Compiling to binary, $(PROJECT_NAME)"
	@ mkdir -p $(shell pwd)/target
	@ cd $(shell pwd)/$(PROJECT_NAME_SRC)/; zip --quiet -r ../target/$(PROJECT_NAME) *
	@ echo '#!$(PYTHON)' > target/$(PROJECT_NAME) && \
		cat target/$(PROJECT_NAME).zip >> target/$(PROJECT_NAME) && \
		rm target/$(PROJECT_NAME).zip && \
		chmod a+x target/$(PROJECT_NAME)
	@ cp target/$(PROJECT_NAME) target/$(PROJECT_NAME)-$(PROJECT_VERSION)


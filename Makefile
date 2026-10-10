.PHONY: test build volume volumes all watch release clean check-target

test:
	./tests/check-index-terms.sh
	python3 -m unittest -v tests/test_target_pdfs.py tests/test_audit_math_reading_structure.py
	bash tests/check-build-clean.sh
	bash tests/check-part-openings.sh
	python3 tests/check-heading-anchors.py

build:
	./build.sh build

volume:
	./build.sh volume $(VOLUME)

volumes:
	./build.sh volumes

all:
	./build.sh all

watch:
	./build.sh watch

release:
	./build.sh release

clean:
	./build.sh clean

check-target:
	./build.sh check-target

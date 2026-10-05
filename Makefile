.PHONY: test build volume volumes all watch release clean

test:
	./tests/check-index-terms.sh

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

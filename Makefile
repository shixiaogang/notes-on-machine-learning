.PHONY: all watch release clean

all:
	./build.sh build

watch:
	./build.sh watch

release:
	./build.sh release

clean:
	./build.sh clean

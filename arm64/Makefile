deb_dir = My
version = 0.0.1
architecture = arm64

all: builddir createdeb clean
	echo "OK"
builddir:
	mkdir -p $(deb_dir)/usr/local/myDemo
	cp -rf app/* $(deb_dir)/usr/local/myDemo/
createdeb:
	dpkg-deb -b $(deb_dir) demo_$(version)_$(architecture).deb
clean:
	rm -rf $(deb_dir)/usr/local/multic-toolbox/*
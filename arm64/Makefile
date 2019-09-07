deb_dir = multic-toolbox-deb
version = 0.0.1
architecture = arm64

all: builddir createdeb clean
	echo "OK"

builddir:
	mkdir -p $(deb_dir)/usr/local/multic-toolbox
	cp -rf multic_toolbox/* $(deb_dir)/usr/local/multic-toolbox/

createdeb:
	dpkg-deb -b $(deb_dir) demo_$(version)_$(architecture).deb

clean:
	rm -rf $(deb_dir)/usr/local/multic-toolbox/*
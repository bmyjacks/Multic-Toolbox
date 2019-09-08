deb_dir = multic_toolbox_deb
version = 0.0.1

all: builddir createdeb clean
	echo "OK"

builddir:
	mkdir -p $(deb_dir)/usr/local/multic_toolbox
	cp -rf multic_toolbox/* $(deb_dir)/usr/local/multic_toolbox/
	echo "Build folds successful!"

createdeb:
	dpkg-deb -b $(deb_dir) Multic_Toolbox_$(version).deb
	echo "Create deb successful!"

clean:
	-rm -rf $(deb_dir)/usr
	-rm -rf multic-toolbox-deb
	echo "Clean!"
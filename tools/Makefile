XSCHEM_VERSION=2.9.7
XSCHEM_URL=http://repo.hu/projects/xschem/releases/xschem-$(XSCHEM_VERSION).tar.gz 
XSCHEM_INSTALL_DIR=$(HOME)/tmp/xschem/$(XSCHEM_VERSION)

download_xschem:
	mkdir build
	wget $(XSCHEM_URL) -O  build/xschem-$(XSCHEM_VERSION).tar.gz

install_xschem:
	cd build && tar xvzf xschem-$(XSCHEM_VERSION).tar.gz
	cd build/xschem-$(XSCHEM_VERSION) && ./configure prefix=$(XSCHEM_INSTALL_DIR)
	make -C build/xschem-$(XSCHEM_VERSION) install

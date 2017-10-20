# 'Makefile'.
# Chris Shiels.


TARGETS = audacious-3.7.2-gtk3.tar.bz2 \
	  audacious-plugins-3.7.2-gtk3.tar.bz2 \
	  ffmpeg-2.8.7.tar.xz \
	  grip-3.2.0.tar.gz \
	  id3lib-3.8.3.tar.gz \
	  lame-3.99.5.tar.gz \
	  mpg123-1.23.6.tar.bz2 \
	  vlc-2.2.4.tar.xz


all: $(TARGETS)


audacious-3.7.2-gtk3.tar.bz2:
	curl -L -O http://distfiles.audacious-media-player.org/audacious-3.7.2-gtk3.tar.bz2


audacious-plugins-3.7.2-gtk3.tar.bz2:
	curl -L -O http://distfiles.audacious-media-player.org/audacious-plugins-3.7.2-gtk3.tar.bz2


ffmpeg-2.8.7.tar.xz:
	curl -L -O https://ffmpeg.org/releases/ffmpeg-2.8.7.tar.xz


grip-3.2.0.tar.gz:
	curl -L -O https://sourceforge.net/projects/grip/files/grip/3.2.0/grip-3.2.0.tar.gz


id3lib-3.8.3.tar.gz:
	curl -L -O https://sourceforge.net/projects/id3lib/files/id3lib/3.8.3/id3lib-3.8.3.tar.gz


lame-3.99.5.tar.gz:
	curl -L -O https://sourceforge.net/projects/lame/files/lame/3.99/lame-3.99.5.tar.gz


mpg123-1.23.6.tar.bz2:
	curl -L -O https://www.mpg123.de/download/mpg123-1.23.6.tar.bz2


vlc-2.2.4.tar.xz:
	curl -L -O http://get.videolan.org/vlc/2.2.4/vlc-2.2.4.tar.xz


clean:
	rm -vf $(TARGETS)

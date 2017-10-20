# 'Makefile'.
# Chris Shiels.


TARGETS = audacious-3.7.2-gtk3.tar.bz2 \
	  audacious-plugins-3.7.2-gtk3.tar.bz2 \
	  ffmpeg-3.4.tar.xz \
	  vlc-2.2.4.tar.xz


all: $(TARGETS)


audacious-3.7.2-gtk3.tar.bz2:
	curl -L -O http://distfiles.audacious-media-player.org/audacious-3.7.2-gtk3.tar.bz2


audacious-plugins-3.7.2-gtk3.tar.bz2:
	curl -L -O http://distfiles.audacious-media-player.org/audacious-plugins-3.7.2-gtk3.tar.bz2


ffmpeg-3.4.tar.xz:
	curl -L -O https://www.ffmpeg.org/releases/ffmpeg-3.4.tar.xz


vlc-2.2.4.tar.xz:
	curl -L -O http://get.videolan.org/vlc/2.2.4/vlc-2.2.4.tar.xz


clean:
	rm -vf $(TARGETS)

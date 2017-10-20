# 'Makefile'.
# Chris Shiels.


TARGETS = ffmpeg-3.4.tar.xz \
	  vlc-2.2.4.tar.xz


all: $(TARGETS)


ffmpeg-3.4.tar.xz:
	curl -L -O https://www.ffmpeg.org/releases/ffmpeg-3.4.tar.xz


vlc-2.2.4.tar.xz:
	curl -L -O http://get.videolan.org/vlc/2.2.4/vlc-2.2.4.tar.xz


clean:
	rm -vf $(TARGETS)

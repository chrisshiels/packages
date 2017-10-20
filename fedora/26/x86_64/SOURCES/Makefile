# 'Makefile'.
# Chris Shiels.


TARGETS = ffmpeg-2.8.13.tar.xz \
	  vlc-2.2.6.tar.xz


all: $(TARGETS)


ffmpeg-2.8.13.tar.xz:
	curl -L -O https://www.ffmpeg.org/releases/ffmpeg-2.8.13.tar.xz


vlc-2.2.6.tar.xz:
	curl -L -O http://get.videolan.org/vlc/2.2.6/vlc-2.2.6.tar.xz


clean:
	rm -vf $(TARGETS)

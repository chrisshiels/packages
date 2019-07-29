# 'Makefile'.
# Chris Shiels.


TARGETS = ffmpeg-4.1.4.tar.xz \
	  vlc-3.0.7.1.tar.xz


all: $(TARGETS)


ffmpeg-4.1.4.tar.xz:
	curl -L -O https://www.ffmpeg.org/releases/ffmpeg-4.1.4.tar.xz


vlc-3.0.7.1.tar.xz:
	curl -L -O http://get.videolan.org/vlc/3.0.7.1/vlc-3.0.7.1.tar.xz


clean:
	rm -vf $(TARGETS)

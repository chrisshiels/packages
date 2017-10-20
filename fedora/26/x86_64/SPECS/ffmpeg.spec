# 'ffmpeg.spec'.
# Chris Shiels.


Name:       ffmpeg
Version:    3.4
Release:    1.mecachis.fc26
BuildArch:  x86_64
Group:      Mecachis
License:    GPLv2, GPLv3, LGPLv2.1 and LGPLv3
Vendor:     Mecachis
URL:        https://www.ffmpeg.org/
Summary:    Record, convert and stream audio and video


Source0:    https://www.ffmpeg.org/releases/ffmpeg-3.4.tar.xz


BuildRequires:  yasm

BuildRequires:  lame-devel
Requires:       lame


%description
FFmpeg is the leading multimedia framework, able to decode, encode, transcode,
mux, demux, stream, filter and play pretty much anything that humans and
machines have created.  It supports the most obscure ancient formats up to the
cutting edge.  No matter if they were designed by some standards committee,
the community or a corporation.  It is also highly portable: FFmpeg compiles,
runs, and passes our testing infrastructure FATE across Linux, Mac OS X,
Microsoft Windows, the BSDs, Solaris, etc. under a wide variety of build
environments, machine architectures, and configurations.

It contains libavcodec, libavutil, libavformat, libavfilter, libavdevice,
libswscale and libswresample which can be used by applications.  As well as
ffmpeg, ffserver, ffplay and ffprobe which can be used by end users for
transcoding, streaming and playing.


%prep
%setup


%build
./configure \
        --prefix=/usr/local \
        --enable-shared \
        --enable-pic \
	--enable-libmp3lame \
	--disable-stripping \
	--enable-rpath
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root, -)
/usr/local/bin/*
/usr/local/include/*/*
/usr/local/lib/*.a
/usr/local/lib/*.so*
/usr/local/lib/pkgconfig/*
/usr/local/share/ffmpeg
#/usr/local/share/man/*/*
%doc Changelog
%doc COPYING.GPLv2
%doc COPYING.GPLv3
%doc COPYING.LGPLv2.1
%doc COPYING.LGPLv3
%doc CREDITS
%doc doc
%doc INSTALL.md
%doc LICENSE.md
%doc MAINTAINERS
%doc README.md
%doc RELEASE
%doc RELEASE_NOTES
%doc VERSION


%changelog
* Fri Oct 20 2017 Chris Shiels <chris@mecachis.net> 3.4-1.mecachis.fc26
- Initial release.

# 'vlc.spec'.
# Chris Shiels.


Name:       vlc
Version:    3.0.7.1
Release:    1.mecachis.fc30
BuildArch:  x86_64
Group:      Mecachis
License:    GPLv2 and LGPLv2.1
Vendor:     Mecachis
URL:        http://www.videolan.org/
Summary:    Cross-platform multimedia player and framework


Source0:    http://get.videolan.org/vlc/3.0.7.1/vlc-3.0.7.1.tar.xz


BuildRequires:  alsa-lib-devel
BuildRequires:  gcc
BuildRequires:  libgcrypt-devel
BuildRequires:  libva-devel
BuildRequires:  lua-devel
BuildRequires:  qt5-devel
BuildRequires:  xcb-util-keysyms-devel
Requires:       alsa-lib
Requires:       libgcrypt
Requires:       libva
Requires:       lua
Requires:       xcb-util-keysyms

BuildRequires:  ffmpeg
Requires:       ffmpeg


%description
VLC is a free and open source cross-platform multimedia player and framework
that plays most multimedia files as well as DVDs, Audio CDs, VCDs, and various
streaming protocols.


%prep
%setup


%build
PKG_CONFIG_PATH=/usr/local/lib/pkgconfig \
	./configure \
		--prefix=/usr/local \
		--disable-a52 \
		--disable-mad
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root, -)
/usr/local/bin/*
/usr/local/include/vlc
/usr/local/lib/*.la
/usr/local/lib/*.so*
/usr/local/lib/pkgconfig/*
/usr/local/lib/vlc
/usr/local/share/applications/*
/usr/local/share/doc/vlc
/usr/local/share/icons/hicolor/*/apps/*
/usr/local/share/kde4/apps/solid/actions/*
/usr/local/share/locale/*/LC_MESSAGES/*
/usr/local/share/man/man1/*
/usr/local/share/metainfo/vlc.appdata.xml
/usr/local/share/vlc
%doc ABOUT-NLS
%doc AUTHORS
%doc ChangeLog
%doc COPYING
%doc COPYING.LIB
%doc doc
%doc INSTALL
%doc NEWS
%doc README
%doc THANKS


%changelog
* Sun Jul 21 2019 Chris Shiels <chris@mecachis.net> 3.0.7.1-1.mecachis.fc30
- Initial release.

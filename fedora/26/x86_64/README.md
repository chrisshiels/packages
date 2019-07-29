# packages

RPM .spec files for various applications missing from stock Fedora 26.


    host$ ( cd SOURCES ; make )

    host$ ./setup.sh

    host$ rpmbuild -ba SPECS/ffmpeg.spec
    host$ sudo rpm -iv RPMS/x86_64/ffmpeg-2.8.13-1.mecachis.fc26.x86_64.rpm
    host$ rpmbuild -ba SPECS/vlc.spec
    host$ sudo rpm -ivh RPMS/x86_64/vlc-2.2.6-1.mecachis.fc26.x86_64.rpm

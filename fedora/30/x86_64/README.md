# packages

RPM .spec files for various applications missing from stock Fedora 30.


    host$ ( cd SOURCES ; make )

    host$ ./setup.sh

    host$ rpmbuild -ba SPECS/ffmpeg.spec
    host$ sudo rpm -iv RPMS/x86_64/ffmpeg-4.1.4-1.mecachis.fc30.x86_64.rpm
    host$ rpmbuild -ba SPECS/vlc.spec
    host$ sudo rpm -ivh RPMS/x86_64/vlc-3.0.7.1-1.mecachis.fc30.x86_64.rpm

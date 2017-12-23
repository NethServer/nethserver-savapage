%define savapage_version 0.9.12

Summary: Savapage open print portal
Name: nethserver-savapage
Version: 0.0.1
Release: 4%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
#Source2: SavaPassEncode.java
AutoReq: no

Requires: nethserver-avahi, nethserver-postgresql, nethserver-cups
Requires: java-1.8.0-openjdk,java-1.8.0-openjdk-devel
Requires: poppler-utils,ImageMagick,binutils,which,gzip,perl,avahi-tools
Requires(pre): shadow-utils

BuildRequires: nethserver-devtools
#BuildRequires: java-1.8.0-openjdk-devel

%description
Savapage integration to NethServer

%pre
getent group savapage >/dev/null || groupadd -r savapage
getent passwd savapage >/dev/null || \
    useradd -r -g savapage -d /home/savapage -s /bin/bash \
    -c "Savapage user" savapage
exit 0

%prep
%setup

%build
perl createlinks


#mkdir -p root/usr/share/savapage
#for source in %{SOURCE2}
#do
#    cp $source root/usr/share/savapage
#    source=`basename $source`
#    javac root/usr/share/savapage/$source
#    rm -f root/usr/share/savapage/$source
#done


%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Tue Dec 19 2017 Markus Neuberger <info@markusneuberger.at> - 0.1.0-4
- Added LDAP/AD join
- Added nethserver-savapage-conf-db perl action script
- Added description to pasted spec
* Thu Dec 14 2017 Markus Neuberger <info@markusneuberger.at> - 0.1.0-3
- Added postgres connection
- Download now at install, not at build
- Java 1.8 needed - thanks to Rob Bosch
* Mon Dec 11 2017 Markus Neuberger <info@markusneuberger.at> - 0.1.0-2
- changed savapage login shell to /bin/bash - thanks to Rob Bosch
- changed savapage home dir to /home/savapage - thanks to Rob Bosch
- Added application button
- Added savapage installation - thanks to Rob Bosch
- Added fresh savapage snapshot that works with postgresql - thanks to Rob Bosch
* Fri Dec 08 2017 Markus Neuberger <info@markusneuberger.at> - 0.1.0-1
- Cloned from gsanchietti - thanks to Giacomo Sanchietti & Rob Bosch
- Updated savapage version 0.9.12
- Added requires to spec
- Improved README.rst



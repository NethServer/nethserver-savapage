%define savapage_version 0.9.12

Summary: Savapage open print portal
Name: nethserver-savapage
Version: 0.0.1
Release: 3%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
#Source1: https://www.savapage.org/download/snapshots/savapage-setup-%{savapage_version}-linux-x64.bin
AutoReq: no

Requires: nethserver-avahi, nethserver-postgresql, nethserver-cups
Requires: java-1.7.0-openjdk
Requires: poppler-utils,ImageMagick
Requires: binutils,which,gzip,perl,avahi-tools
Requires(pre): shadow-utils

BuildRequires: nethserver-devtools

%description
Avahi daemon configuration

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

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
# %attr(-,savapage,savapage) /opt/savapage*
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Thu Dec 14 2017 Markus Neuberger <info@markusneuberger.at> - 0.1.0-3
- Added postgres connection
- Download now at install, not at build
- Changed to Java 1.7.0 - thanks to Rob Bosch
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



%define savapage_version 0.9.12

Summary: Savapage open print portal
Name: nethserver-savapage
Version: 0.0.1
Release: 7%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
AutoReq: no

Requires: nethserver-avahi, nethserver-postgresql, nethserver-cups
Requires: java-1.8.0-openjdk,java-1.8.0-openjdk-devel
Requires: poppler-utils,ImageMagick,binutils,which,gzip,perl,avahi-tools
Requires(pre): shadow-utils

BuildRequires: nethserver-devtools

%description
Savapage integration to NethServer

%pre
mkdir -p /opt/savapage/server
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
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog

* Tue Jan 02 2018 Markus Neuberger <info@markusneuberger.at> - 0.1.0-7
- Added trust self-signed cert
- Added AD SSL connection
- Removed samba DC patch for no strong auth
- Added nethserver-savapage-sync-users
* Sat Dec 30 2017 Markus Neuberger <info@markusneuberger.at> - 0.1.0-6
- Added AD/LDAP user sync via new savapage-cmd - thanks to Rijk Ravestein
- Added savaaduser creation to sync AD
- Replaced db commands with savapage-cmd
* Thu Dec 28 2017 Markus Neuberger <info@markusneuberger.at> - 0.1.0-5
- Added password with savapage-cmd - thanks to Rijk Ravestein
- Added no user source when no AD/LDAP is installed - thanks to Rob Bosch
- Added defaults to get a ready to use savapage instead of having to do some setup steps - thanks to Rob Bosch
- Added remote LDAP host - thanks to Rob Bosch
- Added samba DC patch for no strong auth to make savapage work without cert
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

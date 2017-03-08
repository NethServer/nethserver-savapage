%define savapage_version 0.9.11

Summary: Savapage configuration
Name: nethserver-savapage
Version: 0.0.1
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
Source1: https://www.savapage.org/download/installer/savapage-setup-%{savapage_version}-linux-x64.bin

Requires: nethserver-avahi, nethserver-postgresql, nethserver-cups
Requires: java-1.7.0-openjdk
Requires: poppler-utils, ImageMagick
Requires(pre): shadow-utils

BuildRequires: nethserver-devtools

%description
Avahi daemon configuration


%pre
getent group savapage >/dev/null || groupadd -r savapage
getent passwd savapage >/dev/null || \
    useradd -r -g savapage -d /opt/savapage -s /sbin/nologin \
    -c "Savapage user" savapage
exit 0

%prep
%setup

%build
perl createlinks

%install
rm -rf %{buildroot}
mkdir -p root/opt/
cp %{SOURCE1} root/opt/savapage-setup.bin
chmod a+x root/opt/savapage-setup.bin
cd root/opt/ && ./savapage-setup.bin -e 
cd -
rm -f root/opt/savapage-setup.bin
(cd root ; find . -depth -not -name '*.orig' -print  | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist


%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%attr(-,savapage,savapage) /opt/savapage*
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog

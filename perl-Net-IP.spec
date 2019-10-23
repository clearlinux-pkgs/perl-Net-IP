#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-IP
Version  : 1.26
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/M/MA/MANU/Net-IP-1.26.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MANU/Net-IP-1.26.tar.gz
Summary  : Perl extension for manipulating IPv4/IPv6 addresses
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Net-IP-bin = %{version}-%{release}
Requires: perl-Net-IP-data = %{version}-%{release}
Requires: perl-Net-IP-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This is the Net::IP module, designed to allow easy manipulation of IPv4 and
IPv6 addresses.

%package bin
Summary: bin components for the perl-Net-IP package.
Group: Binaries
Requires: perl-Net-IP-data = %{version}-%{release}
Requires: perl-Net-IP-license = %{version}-%{release}

%description bin
bin components for the perl-Net-IP package.


%package data
Summary: data components for the perl-Net-IP package.
Group: Data

%description data
data components for the perl-Net-IP package.


%package dev
Summary: dev components for the perl-Net-IP package.
Group: Development
Requires: perl-Net-IP-bin = %{version}-%{release}
Requires: perl-Net-IP-data = %{version}-%{release}
Provides: perl-Net-IP-devel = %{version}-%{release}
Requires: perl-Net-IP = %{version}-%{release}

%description dev
dev components for the perl-Net-IP package.


%package license
Summary: license components for the perl-Net-IP package.
Group: Default

%description license
license components for the perl-Net-IP package.


%prep
%setup -q -n Net-IP-1.26

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Net-IP
cp %{_builddir}/Net-IP-1.26/COPYING %{buildroot}/usr/share/package-licenses/perl-Net-IP/7d58fbe5dd4a587d16ca1b98833a9eed034ef6a3
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ipcount
/usr/bin/iptab

%files data
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Net/IP.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::IP.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Net-IP/7d58fbe5dd4a587d16ca1b98833a9eed034ef6a3

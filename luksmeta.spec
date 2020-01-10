Name:           luksmeta
Version:        8
Release:        2%{?dist}
Summary:        Utility for storing small metadata in the LUKSv1 header

License:        LGPLv2+
URL:            https://github.com/latchset/%{name}
Source0:        https://github.com/latchset/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig
BuildRequires:  cryptsetup-devel
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description
LUKSMeta is a command line utility for storing small portions of metadata in
the LUKSv1 header for use before unlocking the volume.

%package -n lib%{name}
Summary:        Library for storing small metadata in the LUKSv1 header

%description -n lib%{name}
LUKSMeta is a C library for storing small portions of metadata in the LUKSv1
header for use before unlocking the volume.

%package -n lib%{name}-devel
Summary:        Development files for libluksmeta
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description -n lib%{name}-devel
This package contains development files for the LUKSMeta library.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}/%{_libdir}/libluksmeta.la

#%check
#make %{?_smp_mflags} check

%post -n lib%{name} -p /sbin/ldconfig
%postun -n lib%{name} -p /sbin/ldconfig

%files
%{_bindir}/luksmeta
%{_mandir}/man8/luksmeta.8*

%files -n lib%{name}
%license COPYING
%{_libdir}/libluksmeta.so.*

%files -n lib%{name}-devel
%{_includedir}/luksmeta.h
%{_libdir}/libluksmeta.so
%{_libdir}/pkgconfig/luksmeta.pc

%changelog
* Mon Aug 06 2018 Nathaniel McCallum <npmccallum@redhat.com> - 8-2
- Rebuild for new libcryptsetup
- Resolves rhbz#1593844

* Fri Sep 29 2017 Nathaniel McCallum <npmccallum@redhat.com> - 8-1
- New upstream release
- Resolves #1461448

* Wed Jun 14 2017 Nathaniel McCallum <npmccallum@redhat.com> - 6-1
- New upstream release
- Fixes the stray fprintf() caused by the last build

* Thu Jun 01 2017 Nathaniel McCallum <npmccallum@redhat.com> - 5-1
- New upstream release
- Resolves #1436705

* Tue Oct 25 2016 Nathaniel McCallum <npmccallum@redhat.com> - 3-1
- New upstream release
- Temporarily disable the tests

* Thu Aug 25 2016 Nathaniel McCallum <npmccallum@redhat.com> - 2-1
- First release

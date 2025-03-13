Summary:    Free library to decode DTS Coherent Acoustics streams
Name:       libdca
Version:    0.0.7
Release:    1%{?dist}
License:    GPLv2+
URL:        https://www.videolan.org/developers/libdca.html

Source:     https://code.videolan.org/videolan/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc

%description
%{name} is a free library for decoding DTS Coherent Acoustics streams. It is
released under the terms of the GPL license. The DTS Coherent Acoustics standard
is used in a variety of applications, including DVD, DTS audio CD and radio
broadcasting.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary:    Various tools that use with %{name}

%description tools
Various tools that use %{name}.

%prep
%autosetup -p1

%build
autoreconf -vif
%configure --disable-static
%make_build

%install
%make_install

find %{buildroot} -name "*.la" -delete
find %{buildroot} -name "*.a" -delete

%files
%doc AUTHORS NEWS README
%license COPYING
%{_libdir}/%{name}.so.0
%{_libdir}/%{name}.so.0.0.0

%files tools
%{_bindir}/dcadec
%{_bindir}/dtsdec
%{_bindir}/extract_dca
%{_bindir}/extract_dts
%{_mandir}/man1/dcadec.*
%{_mandir}/man1/dtsdec.*
%{_mandir}/man1/extract_dca.*
%{_mandir}/man1/extract_dts.*

%files devel
%doc doc/%{name}.txt
%{_includedir}/dca.h
%{_includedir}/dts.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/libdca.pc
%{_libdir}/pkgconfig/libdts.pc

%changelog
* Thu Jan 14 2021 Simone Caronni <negativo17@gmail.com> - 0.0.7-1
- First build.

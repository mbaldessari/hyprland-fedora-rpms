Name:		xcb-util-errors
Version:	1.0.1
Release:	1%{?dist}
Summary:	XCB utility library that gives human readable names to error, event, & request codes
License:	MIT
URL:		http://xcb.freedesktop.org
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.xz
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	pkgconfig(xcb-util) >= 0.3.8
BuildRequires:	pkgconfig(xcb-proto)
BuildRequires:	m4

%description
xcb-util-errors is a utility library that gives human readable names to error
codes and event codes and also to major and minor numbers.

The necessary information is drawn from xcb-proto's protocol descriptions.
This library is especially useful when working with extensions and is mostly
useful for debugging.


%package	devel
Summary:	Development and header files for xcb-util-errors
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
Development files for xcb-util-errors.


%prep
%setup -q

%build
%configure --with-pic --disable-static --disable-silent-rules
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/*.la
%ldconfig_post
%ldconfig_postun

%check
make check

%files
%if 0%{?_licensedir:1}
%license COPYING
%else
%doc COPYING
%endif
%{_libdir}/*.so.*

%files devel
%doc NEWS
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/xcb/*.h

%changelog
* Thu Apr 13 2023 Michele Baldessari <michele@acksyn.org> - 1.0.1-1
- Initial build

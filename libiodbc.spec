%bcond_with gtk

%define major 2
%define libname %mklibname iodbc %{major}
%define libadm %mklibname iodbcadm %{major}
%define libinst %mklibname iodbcinst %{major}
%define libdrvproxy %mklibname iodbcdrvproxy %{major}
%define devname %mklibname iodbc -d

%define _disable_lto 1

Summary:	The iODBC Driver Manager
Name:		libiodbc
Version:	3.52.12
Release:	1
Group:		System/Libraries
License:	BSD
Url:		http://www.iodbc.org/
Source0:	https://downloads.sourceforge.net/project/iodbc/iodbc/%{version}/libiodbc-%{version}.tar.gz
%if %with gtk
BuildRequires:	pkgconfig(gtk+-2.0)
%endif

%description
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

The iODBC Driver Manager was originally created by Ke Jin and is
currently maintained by OpenLink Software under a LGPL or BSD license
(see "LICENSE" file included in the distribution).

%package util
Summary:	The iODBC Driver Manager common binary files
Group:		System/Libraries

%description util
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

%package -n %{libname}
Summary:	The iODBC Driver Manager main library
Group:		System/Libraries

%description -n %{libname}
This package contains a shared library for %{name}.

%package -n %{libinst}
Summary:	The iODBC Driver Manager main library
Group:		System/Libraries

%description -n %{libinst}
This package contains a shared library for %{name}.

%if %with gtk
%package -n %{libdrvproxy}
Summary:	The iODBC Driver Manager main library
Group:		System/Libraries

%description -n %{libdrvproxy}
This package contains a shared library for %{name}.

%package -n %{libadm}
Summary:	The iODBC Driver Manager main library
Group:		System/Libraries

%description -n %{libadm}
This package contains a shared library for %{name}.

%package admin
Summary:	GTK based administrator for iODBC development
Group:		Development/Libraries

%description admin
This package contains a GTK based administrator program for maintaining
DSN information in odbc.ini and odbcinst.ini files.
%endif

%package -n %{devname}
Summary:	header files and libraries for iODBC development
Group:		Development/Databases
Provides:	iodbc-devel = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}
Requires:	%{libinst}
Requires:	%{name}-util = %{EVRD}
%if %with gtk
Requires:	%{libdrvproxy} = %{EVRD}
Requires:	%{libadm} = %{EVRD}
%endif

%description -n %{devname}
This package contains the header files and libraries needed to develop
program that use the driver manager.

%prep
%setup -q

%build
%configure \
	--enable-odbc3 \
	--disable-libodbc \
	--disable-static \
%if %with gtk
	--enable-gui \
%else
	--disable-gui \
%endif
	--with-iodbc-inidir=%{_sysconfdir} \
	--includedir=%{_includedir}/iodbc \
	--enable-pthreads

%make

%install
%makeinstall_std

%files util
%{_bindir}/iodbctest
%{_bindir}/iodbctestw
%{_mandir}/man1/iodbctest.1*
%{_mandir}/man1/iodbctestw.1*

%files -n %{libname}
%{_libdir}/libiodbc.so.%{major}*

%files -n %{libinst}
%{_libdir}/libiodbcinst.so.%{major}*

%if %with gtk
%files admin
%{_bindir}/iodbcadm-gtk
%{_mandir}/man1/iodbcadm-gtk.1*

%files -n %{libadm}
%{_libdir}/libiodbcadm.so.%{major}*

%files -n %{libdrvproxy}
%{_libdir}/libiodbcdrvproxy.so.%{major}*
%endif

%files -n %{devname} 
%doc AUTHORS LICENSE* ChangeLog NEWS README*
%doc etc/odbc.ini.sample etc/odbcinst.ini.sample
%{_includedir}/*
%{_bindir}/iodbc-config
%{_libdir}/*.so
%{_libdir}/pkgconfig/libiodbc.pc
%{_datadir}/libiodbc
%{_mandir}/man1/iodbc-config.1*

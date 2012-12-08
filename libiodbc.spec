%bcond_with gtk 0

Name: libiodbc
Version: 3.52.8
Release: 2
Summary: The iODBC Driver Manager
Group: System/Libraries
License: BSD
URL: http://www.iodbc.org/
Source: http://www.iodbc.org/downloads/iODBC/libiodbc-%{version}.tar.gz
%if %with gtk
BuildRequires: gtk+2-devel
%endif

%description
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

The iODBC Driver Manager was originally created by Ke Jin and is
currently maintained by OpenLink Software under a LGPL or BSD license
(see "LICENSE" file included in the distribution).

#---------------------------------------------------------------

%define soname 2
%define libname %mklibname iodbc %{soname}

%package -n %{libname}
Summary: The iODBC Driver Manager main library
Group: System/Libraries

%description -n %{libname}
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

The iODBC Driver Manager was originally created by Ke Jin and is
currently maintained by OpenLink Software under a LGPL or BSD license
(see "LICENSE" file included in the distribution).

%files -n %{libname}
%{_libdir}/libiodbc.so.%{soname}*

#---------------------------------------------------------------

%define instsoname 2
%define libnameinst %mklibname iodbcinst %{instsoname}

%package -n %{libnameinst}
Summary: The iODBC Driver Manager main library
Group: System/Libraries

%description -n %{libnameinst}
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

The iODBC Driver Manager was originally created by Ke Jin and is
currently maintained by OpenLink Software under a LGPL or BSD license
(see "LICENSE" file included in the distribution).

%files -n %{libnameinst}
%{_libdir}/libiodbcinst.so.%{instsoname}*

#---------------------------------------------------------------

%package util
Summary: The iODBC Driver Manager common binary files
Group: System/Libraries

%description util
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

The iODBC Driver Manager was originally created by Ke Jin and is
currently maintained by OpenLink Software under a LGPL or BSD license
(see "LICENSE" file included in the distribution).

%files util
%{_bindir}/iodbctest
%{_bindir}/iodbctestw
%{_mandir}/man1/iodbctest.1*
%{_mandir}/man1/iodbctestw.1*

#---------------------------------------------------------------

%if %with gtk

%define drvproxysoname 2
%define libnamedrvproxy %mklibname drvproxy %{drvproxysoname}

%package -n %{libnamedrvproxy}
Summary: The iODBC Driver Manager main library
Group: System/Libraries

%description -n %{libnamedrvproxy}
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

The iODBC Driver Manager was originally created by Ke Jin and is
currently maintained by OpenLink Software under a LGPL or BSD license
(see "LICENSE" file included in the distribution).

%files -n %{libnamedrvproxy}
%{_libdir}/libiodbcdrvproxy.so.%{drvproxysoname}*

#---------------------------------------------------------------

%define admsoname 2
%define libnameadm %mklibname iodbcadm %{admsoname}

%package -n %{libnameadm}
Summary: The iODBC Driver Manager main library
Group: System/Libraries

%description -n %{libnameadm}
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

The iODBC Driver Manager was originally created by Ke Jin and is
currently maintained by OpenLink Software under a LGPL or BSD license
(see "LICENSE" file included in the distribution).

%files -n %{libnameadm}
%{_libdir}/libiodbcadm.so.%{admsoname}*

#---------------------------------------------------------------

%package admin
Summary: GTK based administrator for iODBC development
Group: Development/Libraries

%description admin
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

This package contains a GTK based administrator program for maintaining
DSN information in odbc.ini and odbcinst.ini files.

The iODBC Driver Manager was originally created by Ke Jin and is
currently maintained by OpenLink Software under a LGPL or BSD license
(see "LICENSE" file included in the distribution).

%files admin
%{_bindir}/iodbcadm-gtk
%{_mandir}/man1/iodbcadm-gtk.1*


%endif

#---------------------------------------------------------------

%define libdev %mklibname iodbc -d

%package -n %{libdev}
Summary: header files and libraries for iODBC development
Group: Development/Databases
Provides: iodbc-devel
Provides: %name-devel
Requires: %{libname}
Requires: %{libnameinst}
Requires: %{name}-util
%if %with gtk
Requires: %{libnamedrvproxy}
Requires: %{libnameadm}
%endif
Requires: unixODBC-devel

%description -n %{libdev}
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

This package contains the header files and libraries needed to develop
program that use the driver manager.

The iODBC Driver Manager was originally created by Ke Jin and is 
currently maintained by OpenLink Software under a LGPL or BSD license
(see "LICENSE" file included in the distribution).

%files -n %{libdev} 
%doc AUTHORS 
%doc AUTHORS 
%doc LICENSE
%doc LICENSE.LGPL
%doc LICENSE.BSD
%doc ChangeLog 
%doc NEWS 
%doc README
%doc README.CVS
%doc etc/odbc.ini.sample
%doc etc/odbcinst.ini.sample
%{_includedir}/*
%{_libdir}/*.so
%{_bindir}/iodbc-config
%{_libdir}/pkgconfig/libiodbc.pc
%{_mandir}/man1/iodbc-config.1*
%{_datadir}/libiodbc
%multiarch_bindir/iodbc-config

#---------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x \
	--enable-odbc3 \
	--disable-libodbc \
	--disable-static \
	%if %with gtk
	--enable-gui \
	%else
	--disable-gui \
	%endif
	--with-iodbc-inidir=%_sysconfdir \
	--includedir=%_includedir/iodbc \
	--enable-pthreads

%make

%install
rm -rf %buildroot

%makeinstall_std

# Multiarch fixes
%multiarch_binaries %buildroot/%_bindir/iodbc-config


%clean
rm -rf %buildroot



%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 3.52.7-4mdv2011.0
+ Revision: 661959
- rebuild

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 3.52.7-3
+ Revision: 661448
- multiarch fixes

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 3.52.7-2mdv2011.0
+ Revision: 602562
- rebuild

* Fri Jan 15 2010 Emmanuel Andry <eandry@mandriva.org> 3.52.7-1mdv2010.1
+ Revision: 491779
- New version 3.52.7

* Fri Jul 17 2009 Helio Chissini de Castro <helio@mandriva.com> 3.52.6-4mdv2010.0
+ Revision: 396896
- We do not need unixODBC to compile

* Fri Jun 19 2009 Helio Chissini de Castro <helio@mandriva.com> 3.52.6-3mdv2010.0
+ Revision: 387368
- Rebuild to regenerate hdlists for missing packages

* Fri Jun 19 2009 Helio Chissini de Castro <helio@mandriva.com> 3.52.6-2mdv2010.0
+ Revision: 387361
- Header installed in includedir/iodbc and not conflicting anymore with unixODBC

* Thu Jun 18 2009 Helio Chissini de Castro <helio@mandriva.com> 3.52.6-1mdv2010.0
+ Revision: 387145
- Add iODBC package required by virtuoso. This will enable fix virtuoso use of internl unixODBC and iODBC
- imported package libiodbc



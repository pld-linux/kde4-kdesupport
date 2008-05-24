%define		_state		snapshots
%define	orgname		kdesupport

%define		snap	810529

Summary:	Kde Support
Name:		kde4-kdesupport
Version:	4.0.74
Release:	0.%{snap}.1
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{orgname}-%{snap}.tar.bz2
# Source0-md5:	48d93173916bfaa95ea1eeda7577530c
URL:		http://www.kde.org/
Patch0:		%{name}-lib64.patch
BuildRequires:	QtDBus-devel >= 4.4.0
BuildRequires:	clucene-core-devel >= 0.9.16a
BuildRequires:	cmake
BuildRequires:	exiv2-devel >= 0.12
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libraptor-devel
BuildRequires:	libxslt-progs
BuildRequires:	libxml2-devel
BuildRequires:	redland-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kde4 support packages including:
- akonadi
- automoc4
- qimageblitz
- soprano
- strigi
- taglib

%package soprano
Summary:	Soprano - Qt wrapper API to librdf
Group:		X11/Applications
Provides:	soprano
Obsoletes:	soprano

%description soprano
Soprano (formally known as QRDF) is a library which provides a Qt
wrapper API to different RDF storage solutions. It features named
graphs (contexts) and has a modular plug-in structure which allows to
use different RDF storage implementations.

%package soprano-devel
Summary:	Header files for soprano
Group:		Development/Libraries
Requires:	%{name}-soprano = %{version}-%{release}

%description soprano-devel
Header files for soprano.

%package strigi
Summary:	Strigi desktop search
Group:		X11/Applications
Provides:	strigi
Obsoletes:	strigi

%description strigi
Here are the main features of Strigi Desktop Search: very fast
crawling, very small memory footprint, no hammering of the system,
pluggable backend (currently clucene and hyperestraier, sqlite3 and
xapian are in the works), communication between daemon and search
program over an abstract interface with two implementations: DBus and
a simple Unix socket. Especially the DBus interface makes it very easy
to write client applications. There are a few sample scripts in the
code using Perl, Python, GTK+ and Qt. Writing clients is so easy that
any GNOME or KDE app could implement this. Additionally, there is a
simple interface for implementing plugins for extracting information.
We'll try to reuse the kat plugins, although native plugins will have
a large speed advantage. Strigi also has calculation of sha1 for every
file crawled which allows for fast finding of duplicate files.

%package strigi-devel
Summary:	Header files for strigi
Group:		Development/Libraries
Requires:	%{name}-strigi = %{version}-%{release}

%description strigi-devel
Header files for strigi.

%package akonadi
Summary:	Akonadi
Group:		X11/Applications
Provides:	akonadi
Obsoletes:	akonadi

%description akonadi
Akonadi.

%package akonadi-devel
Summary:	Header files for akonadi
Group:		Development/Libraries
Requires:	%{name}-akonadi = %{version}-%{release}

%description akonadi-devel
Header files for akonadi.

%package taglib
Summary:	A tag library for reading and editing audio meta data
Group:		X11/Libraries
Provides:	taglib
Obsoletes:	taglib

%description taglib
A tag library needed for juk application which is part of
kde4-kdemultimedia package.

%package taglib-devel
Summary:	Header files for tag library
Group:		Development/Libraries
Requires:	%{name}-taglib = %{version}-%{release}

%description taglib-devel
Header files for tag library.

%package automoc4
Summary:	Automoc4
Group:		X11/Applications
Provides:	kde4-automoc
Obsoletes:	kde4-automoc

%description automoc4
Automoc4.

%package qimageblitz
Summary:	QimageBlitz
Group:		X11/Applications
Provides:	qimageblitz
Obsoletes:	qimageblitz

%description qimageblitz
QimageBlitz.

%package qimageblitz-devel
Summary:	Header files for tag qimageblitz
Group:		Development/Libraries
Requires:	%{name}-qimageblitz = %{version}-%{release}

%description qimageblitz-devel
Header files for tag qimageblitz.

%prep
%setup -q -n %{orgname}-%{snap}
%patch0 -p0

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	soprano	-p /sbin/ldconfig
%postun	soprano	-p /sbin/ldconfig

%post	strigi	-p /sbin/ldconfig
%postun	strigi	-p /sbin/ldconfig

%post	akonadi	-p /sbin/ldconfig
%postun	akonadi	-p /sbin/ldconfig

%post	taglib	-p /sbin/ldconfig
%postun	taglib	-p /sbin/ldconfig

%post	qimageblitz	-p /sbin/ldconfig
%postun	qimageblitz	-p /sbin/ldconfig

%files soprano
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sopranocmd
%attr(755,root,root) %{_bindir}/sopranod
%attr(755,root,root) %{_bindir}/onto2vocabularyclass
%attr(755,root,root) %{_libdir}/libsoprano.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsoprano.so.?
%attr(755,root,root) %{_libdir}/libsopranoclient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsopranoclient.so.?
%attr(755,root,root) %{_libdir}/libsopranoserver.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsopranoserver.so.?
%attr(755,root,root) %{_libdir}/libsopranoindex.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsopranoindex.so.?
%dir %{_libdir}/soprano
%attr(755,root,root) %{_libdir}/soprano/libsoprano_redlandbackend.so
%attr(755,root,root) %{_libdir}/soprano/libsoprano_nquadparser.so
%attr(755,root,root) %{_libdir}/soprano/libsoprano_nquadserializer.so
%attr(755,root,root) %{_libdir}/soprano/libsoprano_raptorparser.so
%attr(755,root,root) %{_libdir}/soprano/libsoprano_sesame2backend.so
%attr(755,root,root) %{_libdir}/soprano/libsoprano_raptorserializer.so
%{_datadir}/soprano
%dir %{_datadir}/dbus-1/interfaces
%{_datadir}/dbus-1/interfaces/org.soprano.Model.xml
%{_datadir}/dbus-1/interfaces/org.soprano.NodeIterator.xml
%{_datadir}/dbus-1/interfaces/org.soprano.QueryResultIterator.xml
%{_datadir}/dbus-1/interfaces/org.soprano.Server.xml
%{_datadir}/dbus-1/interfaces/org.soprano.StatementIterator.xml

%files soprano-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoprano.so
%attr(755,root,root) %{_libdir}/libsopranoserver.so
%attr(755,root,root) %{_libdir}/libsopranoclient.so
%attr(755,root,root) %{_libdir}/libsopranoindex.so
%dir %{_includedir}/soprano
%{_includedir}/soprano/*.h
%{_includedir}/Soprano
%{_pkgconfigdir}/soprano.pc

%files strigi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libsearchclient.so.*.*.*
%attr(755,root,root) %{_libdir}/libstreamanalyzer.so.*.*.*
%attr(755,root,root) %{_libdir}/libstreams.so.*.*.*
%attr(755,root,root) %{_libdir}/libstrigihtmlgui.so.*.*.*
%attr(755,root,root) %{_libdir}/libstrigiqtdbusclient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsearchclient.so.0
%attr(755,root,root) %ghost %{_libdir}/libstreamanalyzer.so.0
%attr(755,root,root) %ghost %{_libdir}/libstreams.so.0
%attr(755,root,root) %ghost %{_libdir}/libstrigihtmlgui.so.0
%attr(755,root,root) %ghost %{_libdir}/libstrigiqtdbusclient.so.0
%dir %{_libdir}/strigi
%attr(755,root,root) %{_libdir}/strigi/*.so
%{_datadir}/dbus-1/services/*.service
%dir %{_datadir}/strigi
%{_datadir}/strigi/fieldproperties

%files strigi-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsearchclient.so
%attr(755,root,root) %{_libdir}/libstreamanalyzer.so
%attr(755,root,root) %{_libdir}/libstreams.so
%attr(755,root,root) %{_libdir}/libstrigihtmlgui.so
%attr(755,root,root) %{_libdir}/libstrigiqtdbusclient.so
%{_libdir}/strigi/*.cmake
%dir %{_includedir}/strigi
%{_includedir}/strigi/*.h
%{_includedir}/strigi/qtdbus
%{_pkgconfigdir}/libstreamanalyzer.pc
%{_pkgconfigdir}/libstreams.pc

%files akonadi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akonadi_control
%attr(755,root,root) %{_bindir}/akonadictl
%attr(755,root,root) %{_bindir}/akonadiserver
%attr(755,root,root) %ghost %{_libdir}/libakonadiprivate.so.?
%attr(755,root,root) %{_libdir}/libakonadiprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libakonadiprotocolinternals.so.?
%attr(755,root,root) %{_libdir}/libakonadiprotocolinternals.so.*.*.*
%dir %{_datadir}/config/akonadi
%{_datadir}/config/akonadi/mysql-global.conf
%{_pkgconfigdir}/akonadi.pc
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.Agent.Control.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.Agent.Status.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.AgentManager.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.ControlManager.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.NotificationManager.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.Resource.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.Search.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.SearchQuery.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.SearchQueryIterator.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.Server.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.Tracer.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.TracerNotification.xml
%{_datadir}/dbus-1/services/org.freedesktop.Akonadi.Control.service
%{_datadir}/mime/packages/akonadi-mime.xml

%files akonadi-devel
%defattr(644,root,root,755)
%{_libdir}/libakonadiprivate.so
%{_libdir}/libakonadiprotocolinternals.so
%{_includedir}/akonadi

%files taglib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtag.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtag.so.?
%attr(755,root,root) %{_libdir}/libtag_c.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtag_c.so.?

%files taglib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/taglib-config
%attr(755,root,root) %{_libdir}/libtag.so
%attr(755,root,root) %{_libdir}/libtag_c.so
%{_pkgconfigdir}/taglib.pc
%{_pkgconfigdir}/taglib_c.pc
%{_includedir}/taglib

%files automoc4
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/automoc4
%dir %{_libdir}/automoc4
%{_libdir}/automoc4/Automoc4Config.cmake
%{_libdir}/automoc4/automoc4.files.in

%files qimageblitz
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/blitztest
%attr(755,root,root) %{_libdir}/libqimageblitz.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqimageblitz.so.?
%{_pkgconfigdir}/qimageblitz.pc

%files qimageblitz-devel
%defattr(644,root,root,755)
%{_includedir}/qimageblitz
%attr(755,root,root) %{_libdir}/libqimageblitz.so

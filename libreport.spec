Summary:	Generic library for reporting various problems
Name:		libreport
Version:	2.0.16
Release:	4
License:	GPL v2
Group:		Libraries
Source0:	https://fedorahosted.org/released/abrt/%{name}-%{version}.tar.gz
# Source0-md5:	b8aa7475152dc8420d7dd0c71752b5ed
Patch0:		format-security.patch
URL:		https://fedorahosted.org/abrt/
BuildRequires:	asciidoc
BuildRequires:	btparser-devel
BuildRequires:	curl-devel
BuildRequires:	dbus-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libproxy-devel
BuildRequires:	libtar-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	newt-devel
BuildRequires:	nss-devel
BuildRequires:	python-devel
BuildRequires:	texinfo
BuildRequires:	xmlrpc-c-client-devel
BuildRequires:	xmlrpc-c-devel
BuildRequires:	xmlto
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libraries providing API for reporting different problems in
applications to different bug targets like Bugzilla, ftp, trac, etc...

%package common
Summary:	Common files for %{name} library
Summary(pl.UTF-8):	Wspólne pliki biblioteki %{name}
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description common
Common files for %{name} library.

%description common -l pl.UTF-8
Wspólne pliki biblioteki %{name}.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%package web
Summary:	Library providing network API for libreport
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description web
Library providing network API for libreport

%package web-devel
Summary:	Development headers for libreport-web
Group:		Development/Libraries
Requires:	%{name}-web = %{version}-%{release}

%description web-devel
Development headers for libreport-web

%package python
Summary:	Python bindings for report-libs
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description python
Python bindings for report-libs.

%package cli
Summary:	%{name}'s command line interface
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description cli
This package contains simple command line tool for working with
problem dump reports

%package newt
Summary:	%{name}'s newt interface
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description newt
This package contains a simple newt application for reporting bugs

%package gtk
Summary:	GTK front-end for libreport
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description gtk
Applications for reporting bugs using libreport backend

%package gtk-devel
Summary:	Development libraries and headers for libreport
Group:		Development/Libraries
Requires:	%{name}-gtk = %{version}-%{release}

%description gtk-devel
Development libraries and headers for libreport-gtk

%package plugin-kerneloops
Summary:	%{name}'s kerneloops reporter plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl

%description plugin-kerneloops
This package contains plugin which sends kernel crash information to
specified server, usually to kerneloops.org.

%package plugin-logger
Summary:	%{name}'s logger reporter plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	abrt-plugin-logger < 2.0.4

%description plugin-logger
The simple reporter plugin which writes a report to a specified file.

%package plugin-mailx
Summary:	%{name}'s mailx reporter plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	mailx
Obsoletes:	abrt-plugin-mailx < 2.0.4

%description plugin-mailx
The simple reporter plugin which sends a report via mailx to a
specified email address.

%package plugin-bugzilla
Summary:	%{name}'s bugzilla plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	abrt-plugin-bugzilla < 2.0.4

%package plugin-ureport
Summary:	%{name}'s micro report plugin
Group:		Libraries
BuildRequires:	json-c-devel
Requires:	%{name} = %{version}-%{release}

%description plugin-ureport
Uploads micro-report to abrt server

%description plugin-bugzilla
Plugin to report bugs into the bugzilla.

%package plugin-rhtsupport
Summary:	%{name}'s RHTSupport plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	abrt-plugin-rhtsupport < 2.0.4

%description plugin-rhtsupport
Plugin to report bugs into RH support system.

%package plugin-reportuploader
Summary:	%{name}'s reportuploader plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	abrt-plugin-reportuploader < 2.0.4

%description plugin-reportuploader
Plugin to report bugs into anonymous FTP site associated with
ticketing system.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	web -p /sbin/ldconfig
%postun	web -p /sbin/ldconfig

%post	gtk -p /sbin/ldconfig
%postun	gtk -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%config(noreplace) %{_sysconfdir}/%{name}/report_event.conf
%config(noreplace) %{_sysconfdir}/%{name}/forbidden_words.conf
%attr(755,root,root) %{_libdir}/libreport.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libreport.so.0
%attr(755,root,root) %{_libdir}/libabrt_dbus.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libabrt_dbus.so.0
%{_mandir}/man5/report_event.conf.5*

%files common
%defattr(644,root,root,755)
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/events.d
%dir %{_sysconfdir}/%{name}/events
%dir %{_sysconfdir}/%{name}/plugins

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/libreport
%{_includedir}/libreport/client.h
%{_includedir}/libreport/dump_dir.h
%{_includedir}/libreport/event_config.h
%{_includedir}/libreport/problem_data.h
%{_includedir}/libreport/report.h
%{_includedir}/libreport/run_event.h
%{_includedir}/libreport/internal_abrt_dbus.h
%{_includedir}/libreport/internal_libreport.h
%attr(755,root,root) %{_libdir}/libreport.so
%attr(755,root,root) %{_libdir}/libabrt_dbus.so
%{_pkgconfigdir}/%{name}.pc

%files web
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libreport-web.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libreport-web.so.0

%files web-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libreport-web.so
%{_includedir}/libreport/libreport_curl.h
%{_pkgconfigdir}/libreport-web.pc

%files python
%defattr(644,root,root,755)
%{py_sitedir}/report
%{py_sitedir}/reportclient

%files cli
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/report-cli
%{_mandir}/man1/report-cli.1*

%files newt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/report-newt

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/report-gtk
%attr(755,root,root) %{_libdir}/libreport-gtk.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libreport-gtk.so.0

%files gtk-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libreport-gtk.so
%{_includedir}/libreport/internal_libreport_gtk.h
%{_pkgconfigdir}/libreport-gtk.pc

%files plugin-kerneloops
%defattr(644,root,root,755)
%{_sysconfdir}/libreport/events/report_Kerneloops.xml
%attr(755,root,root) %{_bindir}/reporter-kerneloops
%{_mandir}/man1/reporter-kerneloops.1*

%files plugin-logger
%defattr(644,root,root,755)
%{_sysconfdir}/libreport/events/report_Logger.conf
%{_sysconfdir}/libreport/events/report_Logger.xml
%config(noreplace) %{_sysconfdir}/libreport/events.d/print_event.conf
%attr(755,root,root) %{_bindir}/reporter-print
%{_mandir}/man1/reporter-print.1*

%files plugin-mailx
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/libreport/plugins/mailx.conf
%config(noreplace) %{_sysconfdir}/libreport/events.d/mailx_event.conf
%{_sysconfdir}/libreport/events/report_Mailx.xml
%attr(755,root,root) %{_bindir}/reporter-mailx
%{_mandir}/man1/reporter-mailx.1*

%files plugin-ureport
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/reporter-ureport
%{_sysconfdir}/libreport/events/report_uReport.xml

%files plugin-bugzilla
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla.conf
%config(noreplace) %{_sysconfdir}/libreport/events/report_Bugzilla.conf
%config(noreplace) %{_sysconfdir}/libreport/events.d/bugzilla_event.conf
%{_sysconfdir}/libreport/events/report_Bugzilla.xml
%attr(755,root,root) %{_bindir}/reporter-bugzilla
%{_mandir}/man1/reporter-bugzilla.1*

%files plugin-rhtsupport
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/libreport/plugins/rhtsupport.conf
%config(noreplace) %{_sysconfdir}/libreport/events.d/rhtsupport_event.conf
%{_sysconfdir}/libreport/events/report_RHTSupport.xml
%attr(755,root,root) %{_bindir}/reporter-rhtsupport
%{_mandir}/man1/reporter-rhtsupport.1*

%files plugin-reportuploader
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/reporter-upload
%config(noreplace) %{_sysconfdir}/libreport/events.d/uploader_event.conf
%{_sysconfdir}/libreport/events/report_Uploader.xml
%{_mandir}/man1/reporter-upload.1*

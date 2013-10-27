Summary:	Generic library for reporting various problems
Summary(pl.UTF-8):	Ogólna biblioteka do zgłaszania różnych problemów
Name:		libreport
Version:	2.1.9
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://fedorahosted.org/released/abrt/%{name}-%{version}.tar.gz
# Source0-md5:	07ccab47869d6f9cfd851b4fba8ba015
Patch0:		format-security.patch
URL:		https://fedorahosted.org/abrt/
BuildRequires:	asciidoc
BuildRequires:	curl-devel
BuildRequires:	dbus-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	glib2-devel >= 1:2.21
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	json-c-devel
BuildRequires:	libproxy-devel
BuildRequires:	libtar-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2
BuildRequires:	newt-devel
BuildRequires:	nss-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	satyr-devel
BuildRequires:	xmlrpc-c-client-devel
BuildRequires:	xmlrpc-c-devel
BuildRequires:	xmlto
Requires:	glib2 >= 1:2.21
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libraries providing API for reporting different problems in
applications to different bug targets like Bugzilla, ftp, trac, etc...

%description -l pl.UTF-8
Biblioteki udostępniające API do zgłaszania różnych programów w
aplikacjach do różnych docelowych systemów raportowania błędów, takich
jak Bugzilla, ftp, trac...

%package devel
Summary:	Header files for libreport libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek libreport
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.21

%description devel
Header files for libreport libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek libreport.

%package web
Summary:	Library providing network API for libreport
Summary(pl.UTF-8):	Biblioteka zapewniająca API sieciowe dla libreport
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description web
Library providing network API for libreport.

%description web -l pl.UTF-8
Biblioteka zapewniająca API sieciowe dla libreport.

%package web-devel
Summary:	Development headers for libreport-web
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libreport-web
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-web = %{version}-%{release}
Requires:	curl-devel
Requires:	json-c-devel
Requires:	libproxy-devel
Requires:	libxml2-devel >= 2
Requires:	satyr-devel
Requires:	xmlrpc-c-client-devel
Requires:	xmlrpc-c-devel

%description web-devel
Development headers for libreport-web.

%description web-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libreport-web.

%package -n python-%{name}
Summary:	Python bindings for libreport libraries
Summary(pl.UTF-8):	Wiązania Pythona dla bibliotek libreport
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-python = %{version}-%{release}
Obsoletes:	libreport-python < 2.1.3-1

%description -n python-%{name}
Python bindings for libreport libraries.

%description -n python-%{name} -l pl.UTF-8
Wiązania Pythona dla bibliotek libreport

%package cli
Summary:	libreport's command line interface
Summary(pl.UTF-8):	Interfejs linii poleceń libreport
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description cli
This package contains simple command line tool for working with
problem dump reports.

%description cli -l pl.UTF-8
Ten pakiet zawiera proste, działające z linii poleceń narzędzie do
pracy ze zgłoszeniami zawierającymi zrzuty problemów.

%package newt
Summary:	libreport's newt interface
Summary(pl.UTF-8):	Interfejs newt libreport
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description newt
This package contains a simple newt application for reporting bugs.

%description newt -l pl.UTF-8
Ten pakiet zawiera prostą aplikację newt do zgłaszania błędów.

%package gtk
Summary:	GTK+ front-end for libreport
Summary(pl.UTF-8):	Interfejs GTK+ libreport
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description gtk
Application for reporting bugs using libreport backend.

%description gtk -l pl.UTF-8
Aplikacja do zgłaszania błędów przy użyciu libreport.

%package gtk-devel
Summary:	Development headers for libreport-gtk
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libreport-gtk
Group:		Development/Libraries
Requires:	%{name}-gtk = %{version}-%{release}

%description gtk-devel
Development headers for libreport-gtk.

%description gtk-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libreport-gtk.

%package plugin-bugzilla
Summary:	libreport's bugzilla plugin
Summary(pl.UTF-8):	Wtyczka libreport do zgłoszeń przez Bugzillę
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	abrt-plugin-bugzilla < 2.0.4

%description plugin-bugzilla
Plugin to report bugs into the bugzilla.

%description plugin-bugzilla -l pl.UTF-8
Wtyczka zgłaszająca problemy do systemu Bugzilla.

%package plugin-kerneloops
Summary:	libreport's kerneloops reporter plugin
Summary(pl.UTF-8):	Wtyczka libreport do zgłoszeń awarii jądra (kerneloops)
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl

%description plugin-kerneloops
This package contains plugin which sends kernel crash information to
specified server, usually to kerneloops.org.

%description plugin-kerneloops -l pl.UTF-8
Ten pakiet zawiera wtyczkę wysyłającą informacje o awariach jądra na
określony serwer, zwykle kerneloops.org.

%package plugin-logger
Summary:	libreport's logger reporter plugin
Summary(pl.UTF-8):	Wtyczka libreport do zgłoszeń w logu
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	abrt-plugin-logger < 2.0.4

%description plugin-logger
The simple reporter plugin which writes a report to a specified file.

%description plugin-logger -l pl.UTF-8
Prosta wtyczka zgłaszająca problem, zapisująca raport w określonym
pliku.

%package plugin-mailx
Summary:	libreport's mailx reporter plugin
Summary(pl.UTF-8):	Wtyczka libreport do zgłoszeń przez pocztę elektroniczną
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	mailx
Obsoletes:	abrt-plugin-mailx < 2.0.4

%description plugin-mailx
The simple reporter plugin which sends a report via mailx to a
specified email address.

%description plugin-mailx -l pl.UTF-8
Prosta wtyczka zgłaszająca problem, wysyłająca raport na określony
adres e-mail przy użyciu programu mailx.

%package plugin-reportuploader
Summary:	libreport's reportuploader plugin
Summary(pl.UTF-8):	Wtyczka libreport do zgłoszeń przez FTP
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	abrt-plugin-reportuploader < 2.0.4

%description plugin-reportuploader
Plugin to report bugs into anonymous FTP site associated with
ticketing system.

%description plugin-reportuploader -l pl.UTF-8
Wtyczka zgłaszająca błędy poprzez serwer anonimowego FTP powiązany z
systemem biletów.

%package plugin-rhtsupport
Summary:	libreport's RHTSupport plugin
Summary(pl.UTF-8):	Wtyczka libreport do zgłoszeń przez RHTSupport
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	abrt-plugin-rhtsupport < 2.0.4

%description plugin-rhtsupport
Plugin to report bugs into RH support system.

%description plugin-rhtsupport -l pl.UTF-8
Wtyczka zgłaszająca problemy do systemu obsługi RH.

%package plugin-ureport
Summary:	libreport's micro report plugin
Summary(pl.UTF-8):	Wtyczka libreport do zgłoszeń typu micro-report
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-ureport
Uploads micro-report to abrt server.

%description plugin-ureport -l pl.UTF-8
Wtyczka przesyłająca raporty typu micro-report na serwer abrt.

%package anaconda
Summary:	Default configuration for reporting Anaconda bugs
Summary(pl.UTF-8):	Domyślna konfiguracja do zgłaszania błędów w Anacondzie
Group:		Applications/File
Requires:	%{name}-plugin-bugzilla = %{version}-%{release}
Requires:	%{name}-plugin-reportuploader = %{version}-%{release}

%description anaconda
Default configuration for reporting Anaconda problems using Fedora
infrastructure or uploading the gathered data over ftp/scp...

%description anaconda -l pl.UTF-8
Domyślna konfiguracja do zgłaszania problemów z Anacondą przy użyciu
infrastruktury Fedory lub przesyłając zebrane dane po ftp/scp.

%package fedora
Summary:	Default configuration for reporting bugs via Fedora infrastructure
Summary(pl.UTF-8):	Domyślna konfiguracja do zgłaszania błędów poprzeze infrastrukturę Fedory
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description fedora
Default configuration for reporting bugs via Fedora infrastructure
used primarily to easy configure the reporting process for Fedora
systems.

%description fedora -l pl.UTF-8
Domyślna konfiguracja do zgłaszania błędów poprzez infrastrukturę
Fedory, służąca przede wszystkim do łatwej konfiguracji procesu
zgłaszania błędów w systemach Fedora.

%package rhel
Summary:	Default configuration for reporting bugs via RHEL infrastructure
Summary(pl.UTF-8):	Domyślna konfiguracja do zgłaszania błędów poprzeze infrastrukturę RHEL
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description rhel
Default configuration for reporting bugs via RHEL infrastructure used
primarily to easy configure the reporting process for RHEL systems.

%description rhel -l pl.UTF-8
Domyślna konfiguracja do zgłaszania błędów poprzez infrastrukturę
RHEL, służąca przede wszystkim do łatwej konfiguracji procesu
zgłaszania błędów w systemach RHEL.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
# compat layer for compatibility tool
%{__rm} $RPM_BUILD_ROOT{%{_bindir}/report,%{_mandir}/man1/report.1}

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
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/report_event.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/forbidden_words.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/ignored_words.conf
%dir %{_sysconfdir}/%{name}/events
%dir %{_sysconfdir}/%{name}/events.d
%dir %{_sysconfdir}/%{name}/plugins
%dir %{_sysconfdir}/%{name}/workflows.d
%attr(755,root,root) %{_libdir}/libreport.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libreport.so.0
%attr(755,root,root) %{_libdir}/libabrt_dbus.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libabrt_dbus.so.0
%dir %{_datadir}/libreport
%dir %{_datadir}/libreport/events
%dir %{_datadir}/libreport/workflows
%{_mandir}/man5/forbidden_words.conf.5*
%{_mandir}/man5/report_event.conf.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libreport.so
%attr(755,root,root) %{_libdir}/libabrt_dbus.so
%dir %{_includedir}/libreport
%{_includedir}/libreport/client.h
%{_includedir}/libreport/config_item_info.h
%{_includedir}/libreport/dump_dir.h
%{_includedir}/libreport/event_config.h
%{_includedir}/libreport/file_obj.h
%{_includedir}/libreport/libreport_types.h
%{_includedir}/libreport/problem_data.h
%{_includedir}/libreport/report.h
%{_includedir}/libreport/run_event.h
%{_includedir}/libreport/internal_abrt_dbus.h
%{_includedir}/libreport/internal_libreport.h
%{_includedir}/libreport/workflow.h
%{_includedir}/libreport/xml_parser.h
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

%files -n python-%{name}
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
%{_mandir}/man1/report-newt.1*

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/report-gtk
%attr(755,root,root) %{_libdir}/libreport-gtk.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libreport-gtk.so.0
%{_mandir}/man1/report-gtk.1*

%files gtk-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libreport-gtk.so
%{_includedir}/libreport/internal_libreport_gtk.h
%{_pkgconfigdir}/libreport-gtk.pc

%files plugin-bugzilla
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/reporter-bugzilla
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla_format.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla_format_kernel.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla_format_libreport.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla_formatdup.conf
%config(noreplace) %{_sysconfdir}/libreport/events/report_Bugzilla.conf
%config(noreplace) %{_sysconfdir}/libreport/events.d/bugzilla_event.conf
%{_datadir}/libreport/events/report_Bugzilla.xml
%{_mandir}/man1/reporter-bugzilla.1*
%{_mandir}/man5/bugzilla.conf.5*
%{_mandir}/man5/bugzilla_event.conf.5*
%{_mandir}/man5/bugzilla_format.conf.5*
%{_mandir}/man5/bugzilla_format_kernel.conf.5*
%{_mandir}/man5/bugzilla_format_libreport.conf.5*
%{_mandir}/man5/bugzilla_formatdup.conf.5*
%{_mandir}/man5/report_Bugzilla.conf.5*

%files plugin-kerneloops
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/reporter-kerneloops
%{_datadir}/libreport/events/report_Kerneloops.xml
%{_mandir}/man1/reporter-kerneloops.1*

%files plugin-logger
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/reporter-print
%{_sysconfdir}/libreport/events/report_Logger.conf
%{_datadir}/libreport/events/report_Logger.xml
%config(noreplace) %{_sysconfdir}/libreport/events.d/print_event.conf
%{_mandir}/man1/reporter-print.1*
%{_mandir}/man5/print_event.conf.5*
%{_mandir}/man5/report_Logger.conf.5*

%files plugin-mailx
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/reporter-mailx
%config(noreplace) %{_sysconfdir}/libreport/plugins/mailx.conf
%config(noreplace) %{_sysconfdir}/libreport/events.d/mailx_event.conf
%{_datadir}/libreport/events/report_Mailx.xml
%{_mandir}/man1/reporter-mailx.1*
%{_mandir}/man5/mailx.conf.5*
%{_mandir}/man5/mailx_event.conf.5*

%files plugin-reportuploader
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/reporter-upload
%config(noreplace) %{_sysconfdir}/libreport/events.d/uploader_event.conf
%{_datadir}/libreport/events/report_Uploader.xml
%{_datadir}/libreport/workflows/workflow_Upload.xml
%{_mandir}/man1/reporter-upload.1*
%{_mandir}/man5/uploader_event.conf.5*

%files plugin-rhtsupport
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/reporter-rhtsupport
%config(noreplace) %{_sysconfdir}/libreport/plugins/rhtsupport.conf
%config(noreplace) %{_sysconfdir}/libreport/events.d/rhtsupport_event.conf
%{_datadir}/libreport/events/report_RHTSupport.xml
%{_mandir}/man1/reporter-rhtsupport.1*
%{_mandir}/man5/rhtsupport.conf.5*
%{_mandir}/man5/rhtsupport_event.conf.5*

%files plugin-ureport
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/reporter-ureport
%config(noreplace) %{_sysconfdir}/libreport/events.d/emergencyanalysis_event.conf
%{_datadir}/libreport/events/report_uReport.xml
%{_datadir}/libreport/events/report_EmergencyAnalysis.xml
%{_mandir}/man1/reporter-ureport.1*
%{_mandir}/man5/emergencyanalysis_event.conf.5*

%files anaconda
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/libreport/events.d/bugzilla_anaconda_event.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla_format_anaconda.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla_formatdup_anaconda.conf
%config(noreplace) %{_sysconfdir}/libreport/workflows.d/anaconda_event.conf
%{_datadir}/libreport/workflows/workflow_AnacondaFedora.xml
%{_datadir}/libreport/workflows/workflow_AnacondaRHEL.xml
%{_datadir}/libreport/workflows/workflow_AnacondaUpload.xml
%{_mandir}/man5/anaconda_event.conf.5*
%{_mandir}/man5/bugzilla_anaconda_event.conf.5*
%{_mandir}/man5/bugzilla_format_anaconda.conf.5*
%{_mandir}/man5/bugzilla_formatdup_anaconda.conf.5*

%files fedora
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/libreport/workflows.d/report_fedora.conf
%{_datadir}/libreport/workflows/workflow_Fedora*.xml
%{_mandir}/man5/report_fedora.conf.5*

%files rhel
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/libreport/workflows.d/report_rhel.conf
%{_datadir}/libreport/workflows/workflow_RHEL*.xml
%{_mandir}/man5/report_rhel.conf.5*

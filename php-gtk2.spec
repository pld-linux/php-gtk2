Summary:	PHP language bindings for GTK+ toolkit
Summary(pl):	Modu³ PHP z wi±zaniami do GTK+
Name:		php-gtk
Version:	0.5.0
Release:	2
License:	GPL
Group:		Libraries
Source0:	%{name}-%{version}.tar.gz
#Source0:	http://gtk.php.net/do_download.php?download_file=%{name}-%{version}
URL:		http://gtk.php.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	php-cgi
BuildRequires:	php-devel
BuildRequires:	php-pcre
BuildRequires:	libglade-devel
BuildRequires:	gtk+-devel
Requires:	php-cgi
Provides:	pear(gdk)
Provides:	pear(GtkWindow)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php

%description
PHP-GTK is a PHP extension that enables you to write client-side
cross-platform GUI applications. This is the first such extension of
this kind and one of the goals behind it was to prove that PHP is a
capable general-purpose scripting language that is suited for more
than just Web applications.

This extension will _not_ allow you to display GTK+ programs in a Web
browser, and cannot be used in the Web environment. It is intended for
creating standalone GUI applications.

%description -l pl
PHP-GTK jest rozszerzeniem PHP które pozwala pisaæ klienckie przeno¶ne
aplikacje typu GUI. To jest pierwsze roszerzenie tego typu i jednym z
celów które przy¶wieca³y jego autorom by³o pokazanie ¿e PHP jest
jêzykiem skryptowym ogólnego zastosowania, który pasuje do czego¶
wiêcej ni¿ tylko aplikacje webowe.

To roszerzenie _nie_pozwoli_ Ci u¿ywaæ programów korzystaj±cych GTK+
przez przegl±darkê i nie mo¿e byæ u¿ywane w ¶rodowisku webowym. Jest
przeznaczone do tworzenia samodzielnych aplikacji GUI.

%prep
%setup -q

%build
phpize
aclocal
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/php

install modules/php_gtk.so $RPM_BUILD_ROOT%{_libdir}/php/gtk.so

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install gtk %{_sysconfdir}/php.ini

%preun
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove gtk %{_sysconfdir}/php.ini
fi

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS TODO NEWS
%attr(755,root,root) %{_libdir}/php/*.so

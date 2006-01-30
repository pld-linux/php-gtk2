# TODO:
#  - rename php-gtk -> php-gtk2
#
%define		_modname	gtk2
%define		_sysconfdir	/etc/php
%define		extensionsdir	%(php-config --extension-dir 2>/dev/null)
Summary:	PHP language bindings for GTK+ toolkit
Summary(pl):	Modu³ PHP z wi±zaniami do GTK+
Name:		php-gtk
Version:	0.0.cvs
%define	_snap 20060131
Release:	0.%{_snap}.1
License:	GPL
Group:		Libraries
#Source0:	http://gtk.php.net/distributions/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.tii.pl/PLD/%{name}-%{_snap}.tar.gz
# Source0-md5:	dfe110e073a63bdce3cee032ad643e06
Patch0:		%{name}-object.patch
Patch1:		%{name}-generator.patch
URL:		http://gtk.php.net/
#BuildRequires:	libglade-devel
BuildRequires:	gtk+2-devel
BuildRequires:	php-devel >= 4:5.1.0
BuildRequires:	php-pcre >= 4:5.1.0
BuildRequires:	rpmbuild(macros) >= 1.238
%{?requires_php_extension}
Requires:	php-cli
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP-GTK is a PHP extension that enables you to write client-side
cross-platform GUI applications. This is the first such extension of
this kind and one of the goals behind it was to prove that PHP is a
capable general-purpose scripting language that is suited for more
than just Web applications.

This extension will _not_ allow you to display GTK+ programs in a Web
browser, and cannot be used in the Web environment. It is intended for
creating standalone GUI applications.

This version (php-gtk2) was rewriten almost from scratch,
and is based on PHP 5.1 and GTK+ 2.6

%description -l pl
PHP-GTK jest rozszerzeniem PHP które pozwala pisaæ klienckie przeno¶ne
aplikacje typu GUI. To jest pierwsze rozszerzenie tego typu i jednym z
celów które przy¶wieca³y jego autorom by³o pokazanie ¿e PHP jest
jêzykiem skryptowym ogólnego zastosowania, który pasuje do czego¶
wiêcej ni¿ tylko aplikacje WWW.

To rozszerzenie _nie_pozwala_ na u¿ywanie programów korzystaj±cych z
GTK+ przez przegl±darkê i nie mo¿e byæ u¿ywane w ¶rodowisku WWW. Jest
przeznaczone do tworzenia samodzielnych aplikacji GUI.

Ta wersja (php-gtk2) zostala przepisana, obecnie bazuje na PHP 5.1
i GTK+ 2.6.

%prep
%setup -q -n php-gtk
%patch0 -p1
#%patch1 -p1

%build
./buildconf \
	 --with-phpize=%{_bindir}/phpize
%configure \
	--with-php-config=%{_bindir}/php-config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}
install modules/php_gtk2.so $RPM_BUILD_ROOT%{extensionsdir}/%{_modname}.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS TODO2 NEWS
%attr(755,root,root) %{extensionsdir}/%{_modname}.so

%define		_modname	gtk2
%define		_sysconfdir	/etc/php
%define		extensionsdir	%(php-config --extension-dir 2>/dev/null)
%define		_snap		20060715
%define		_rel	3
Summary:	PHP language bindings for GTK+ toolkit
Summary(pl):	Modu� PHP z wi�zaniami do GTK+
Name:		php-gtk2
Version:	0.0.cvs
Release:	0.%{_snap}.%{_rel}
License:	GPL
Group:		Libraries
#Source0:	http://gtk.php.net/distributions/%{name}-%{version}.tar.gz
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	2a65f938384060bf7d0a9a8a14a9e54b
Patch0:		%{name}-object.patch
Patch1:		%{name}-memlimit.patch
URL:		http://gtk.php.net/
BuildRequires:	gtk+2-devel
BuildRequires:	php-devel >= 4:5.1
BuildRequires:	php-pcre
BuildRequires:	rpmbuild(macros) >= 1.322
%{?requires_php_extension}
Requires:	php-cli
Provides:	php(gtk2)
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

This version (php-gtk2) was rewriten almost from scratch and is based
on PHP 5.1 and GTK+ 2.6.

%description -l pl
PHP-GTK jest rozszerzeniem PHP kt�re pozwala pisa� klienckie przeno�ne
aplikacje typu GUI. To jest pierwsze rozszerzenie tego typu i jednym z
cel�w kt�re przy�wieca�y jego autorom by�o pokazanie �e PHP jest
j�zykiem skryptowym og�lnego zastosowania, kt�ry pasuje do czego�
wi�cej ni� tylko aplikacje WWW.

To rozszerzenie _nie_pozwala_ na u�ywanie program�w korzystaj�cych z
GTK+ przez przegl�dark� i nie mo�e by� u�ywane w �rodowisku WWW. Jest
przeznaczone do tworzenia samodzielnych aplikacji GUI.

Ta wersja (php-gtk2) zosta�a przepisana prawie od zera, obecnie jest
oparta na PHP 5.1 i GTK+ 2.6.

%prep
%setup -q -n php-gtk
%patch0 -p1
%patch1 -p1

%build
./buildconf \
	 --with-phpize=%{_bindir}/phpize
%configure \
	--with-php-config=%{_bindir}/php-config
%{__make} -j1

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

# NOTE:
#  - fails to build on Ac: http://bugs.php.net/bug.php?id=41720
#  - make NOT fail if $DISPLAY not present, or we can't autoload package
%define		modname	gtk2
Summary:	PHP language bindings for GTK+ toolkit
Summary(pl.UTF-8):	Moduł PHP z wiązaniami do GTK+
Name:		php-gtk2
Version:	2.0.2
Release:	3
License:	GPL
Group:		Libraries
#Source0:	http://gtk.php.net/distributions/php-gtk-%{version}.tar.gz
# 2.0.2 tagged, but no tarball
# svn co http://svn.php.net/repository/gtk/php-gtk/tags/php_gtk_2_0_2 php-gtk-2.0.2
# tar --exclude-vcs -czf php-gtk-2.0.2.tar.gz php-gtk-2.0.2
Source0:	php-gtk-%{version}.tar.gz
# Source0-md5:	63a132426b1f007efc82876906a4e006
URL:		http://gtk.php.net/
BuildRequires:	gtk+2-devel
BuildRequires:	php-devel >= 4:5.1
BuildRequires:	php-pecl-cairo-devel
BuildRequires:	php-program
BuildRequires:	rpmbuild(macros) >= 1.344
Requires:	php-cli
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
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

%description -l pl.UTF-8
PHP-GTK jest rozszerzeniem PHP które pozwala pisać klienckie przenośne
aplikacje typu GUI. To jest pierwsze rozszerzenie tego typu i jednym z
celów które przyświecały jego autorom było pokazanie że PHP jest
językiem skryptowym ogólnego zastosowania, który pasuje do czegoś
więcej niż tylko aplikacje WWW.

To rozszerzenie _nie_pozwala_ na używanie programów korzystających z
GTK+ przez przeglądarkę i nie może być używane w środowisku WWW. Jest
przeznaczone do tworzenia samodzielnych aplikacji GUI.

Ta wersja (php-gtk2) została przepisana prawie od zera, obecnie jest
oparta na PHP 5.1 i GTK+ 2.6.

%prep
%setup -q -n php-gtk-%{version}

%build
./buildconf \
	--with-phpize=%{_bindir}/phpize
%configure \
	--with-php-config=%{_bindir}/php-config
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}
install -p modules/php_gtk2.so $RPM_BUILD_ROOT%{php_extensiondir}/%{modname}.so
# NOTE:
# - makes php unusable if loaded automatically and $DISPLAY not present:
# $ php -r
# PHP Fatal error:  php-gtk: Could not open display in Unknown on line 0
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
; DO NOT load automatically, as it requires DISPLAY being present
;extension=%{modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS TODO2 NEWS
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so

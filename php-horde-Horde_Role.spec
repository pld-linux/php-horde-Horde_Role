# TODO
# - use /usr/share/horde as default
# NOTE:
# - this pkg basically does:
# pear config-set -c horde horde_dir /usr/share/horde
%include	/usr/lib/rpm/macros.php
%define		status		stable
%define		pearname	Horde_Role
Summary:	%{pearname} - PEAR installer role used to install Horde components
Name:		php-horde-Horde_Role
Version:	1.0.0
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	e92a81116885aa932485e4ca0817f15e
URL:		https://github.com/horde/horde/tree/master/framework/Role/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
# http://bugs.horde.org/ticket/10028
BuildRequires:	php-tokenizer
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-channel(pear.horde.org)
Requires:	php-pear >= 4:1.3.6-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a method for PEAR to install Horde components
into a base Horde installation.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/PEAR/Installer/Role/Horde.php
%{php_pear_dir}/PEAR/Installer/Role/Horde.xml
%{php_pear_dir}/PEAR/Installer/Role/Horde

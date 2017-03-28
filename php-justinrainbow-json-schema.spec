%define		pkgname	json-schema
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	PHP implementation of JSON schema
Name:		php-justinrainbow-%{pkgname}
Version:	3.0.1
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/justinrainbow/json-schema/archive/%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	8439562a76016c29032041f513a750cd
URL:		https://github.com/justinrainbow/json-schema
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php(core) >= %{php_min_version}
Requires:	php(filter)
Requires:	php(json)
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(spl)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSON Schema for PHP.

A PHP Implementation for validating JSON Structures against a given
Schema.

Fork of the <http://jsonschemaphpv.sourceforge.net> project.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a src/JsonSchema $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{php_data_dir}/JsonSchema

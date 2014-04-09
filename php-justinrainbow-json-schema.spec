%define		pkgname	json-schema
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	PHP implementation of JSON schema
Name:		php-justinrainbow-%{pkgname}
Version:	1.1.0
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	https://github.com/justinrainbow/json-schema/archive/v%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	8a0d463f7bc9f8cb5b1d8debcccffc0e
URL:		https://github.com/justinrainbow/json-schema
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php(core) >= %{php_min_version}
Requires:	php(pcre)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSON Schema for PHP.

A PHP Implementation for validating JSON Structures against a given
Schema.

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

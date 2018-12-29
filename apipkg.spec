#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : apipkg
Version  : 1.5
Release  : 34
URL      : http://pypi.debian.net/apipkg/apipkg-1.5.tar.gz
Source0  : http://pypi.debian.net/apipkg/apipkg-1.5.tar.gz
Summary  : apipkg: namespace control and lazy-import mechanism
Group    : Development/Tools
License  : MIT
Requires: apipkg-python3
Requires: apipkg-license
Requires: apipkg-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv

%description
------------------------
        
        With apipkg you can control the exported namespace of a Python package and
        greatly reduce the number of imports for your users.
        It is a `small pure Python module`_ that works on CPython 2.7 and 3.4+,
        Jython and PyPy. It cooperates well with Python's ``help()`` system,
        custom importers (PEP302) and common command-line completion tools.

%package license
Summary: license components for the apipkg package.
Group: Default

%description license
license components for the apipkg package.


%package python
Summary: python components for the apipkg package.
Group: Default
Requires: apipkg-python3

%description python
python components for the apipkg package.


%package python3
Summary: python3 components for the apipkg package.
Group: Default
Requires: python3-core

%description python3
python3 components for the apipkg package.


%prep
%setup -q -n apipkg-1.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530988336
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/apipkg
cp LICENSE %{buildroot}/usr/share/doc/apipkg/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/apipkg/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : apipkg
Version  : 1.4
Release  : 10
URL      : https://pypi.python.org/packages/source/a/apipkg/apipkg-1.4.tar.gz
Source0  : https://pypi.python.org/packages/source/a/apipkg/apipkg-1.4.tar.gz
Summary  : apipkg: namespace control and lazy-import mechanism
Group    : Development/Tools
License  : MIT
Requires: apipkg-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
Welcome to apipkg!
------------------------
With apipkg you can control the exported namespace of a
python package and greatly reduce the number of imports for your users.
It is a `small pure python module`_ that works on virtually all Python
versions, including CPython2.3 to Python3.1, Jython and PyPy.  It co-operates
well with Python's ``help()`` system, custom importers (PEP302) and common
command line completion tools.

%package python
Summary: python components for the apipkg package.
Group: Default

%description python
python components for the apipkg package.


%prep
%setup -q -n apipkg-1.4

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487900192
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1487900192
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*

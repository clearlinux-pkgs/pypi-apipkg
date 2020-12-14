#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : apipkg
Version  : 1.5
Release  : 43
URL      : http://pypi.debian.net/apipkg/apipkg-1.5.tar.gz
Source0  : http://pypi.debian.net/apipkg/apipkg-1.5.tar.gz
Summary  : apipkg: namespace control and lazy-import mechanism
Group    : Development/Tools
License  : MIT
Requires: apipkg-license = %{version}-%{release}
Requires: apipkg-python = %{version}-%{release}
Requires: apipkg-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
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
Requires: apipkg-python3 = %{version}-%{release}

%description python
python components for the apipkg package.


%package python3
Summary: python3 components for the apipkg package.
Group: Default
Requires: python3-core
Provides: pypi(apipkg)

%description python3
python3 components for the apipkg package.


%prep
%setup -q -n apipkg-1.5
cd %{_builddir}/apipkg-1.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603385811
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/apipkg
cp %{_builddir}/apipkg-1.5/LICENSE %{buildroot}/usr/share/package-licenses/apipkg/cf3eaf29116a37a7d9ba773e776104c067c8e5fc
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/apipkg/cf3eaf29116a37a7d9ba773e776104c067c8e5fc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-apipkg
Version  : 3.0.1
Release  : 71
URL      : https://files.pythonhosted.org/packages/dc/d8/1883595b81446c61380bdfe10e67f593508c688692b2ce6bf9cc1dc4d007/apipkg-3.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/dc/d8/1883595b81446c61380bdfe10e67f593508c688692b2ce6bf9cc1dc4d007/apipkg-3.0.1.tar.gz
Summary  : apipkg: namespace control and lazy-import mechanism
Group    : Development/Tools
License  : MIT
Requires: pypi-apipkg-license = %{version}-%{release}
Requires: pypi-apipkg-python = %{version}-%{release}
Requires: pypi-apipkg-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatch_vcs)
BuildRequires : pypi(hatchling)

%description
Welcome to apipkg !
-------------------
With apipkg you can control the exported namespace of a Python package and
greatly reduce the number of imports for your users.
It is a `small pure Python module`_ that works on CPython 3.7+,
Jython and PyPy. It cooperates well with Python's ``help()`` system,
custom importers (PEP302) and common command-line completion tools.

%package license
Summary: license components for the pypi-apipkg package.
Group: Default

%description license
license components for the pypi-apipkg package.


%package python
Summary: python components for the pypi-apipkg package.
Group: Default
Requires: pypi-apipkg-python3 = %{version}-%{release}

%description python
python components for the pypi-apipkg package.


%package python3
Summary: python3 components for the pypi-apipkg package.
Group: Default
Requires: python3-core
Provides: pypi(apipkg)

%description python3
python3 components for the pypi-apipkg package.


%prep
%setup -q -n apipkg-3.0.1
cd %{_builddir}/apipkg-3.0.1
pushd ..
cp -a apipkg-3.0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656355623
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-apipkg
cp %{_builddir}/apipkg-3.0.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-apipkg/82dbfd684f7c04da81d4faa852c6317142daa3e7
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-apipkg/82dbfd684f7c04da81d4faa852c6317142daa3e7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

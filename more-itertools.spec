#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : more-itertools
Version  : 8.2.0
Release  : 25
URL      : https://files.pythonhosted.org/packages/a0/47/6ff6d07d84c67e3462c50fa33bf649cda859a8773b53dc73842e84455c05/more-itertools-8.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/a0/47/6ff6d07d84c67e3462c50fa33bf649cda859a8773b53dc73842e84455c05/more-itertools-8.2.0.tar.gz
Summary  : More routines for operating on iterables, beyond itertools
Group    : Development/Tools
License  : MIT
Requires: more-itertools-license = %{version}-%{release}
Requires: more-itertools-python = %{version}-%{release}
Requires: more-itertools-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
==============
More Itertools
==============
.. image:: https://coveralls.io/repos/github/erikrose/more-itertools/badge.svg?branch=master
:target: https://coveralls.io/github/erikrose/more-itertools?branch=master

%package license
Summary: license components for the more-itertools package.
Group: Default

%description license
license components for the more-itertools package.


%package python
Summary: python components for the more-itertools package.
Group: Default
Requires: more-itertools-python3 = %{version}-%{release}

%description python
python components for the more-itertools package.


%package python3
Summary: python3 components for the more-itertools package.
Group: Default
Requires: python3-core

%description python3
python3 components for the more-itertools package.


%prep
%setup -q -n more-itertools-8.2.0
cd %{_builddir}/more-itertools-8.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1580313925
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/more-itertools
cp %{_builddir}/more-itertools-8.2.0/LICENSE %{buildroot}/usr/share/package-licenses/more-itertools/0d43a836dac65c0ea426ad49c881a1086600bf85
cp %{_builddir}/more-itertools-8.2.0/docs/license.rst %{buildroot}/usr/share/package-licenses/more-itertools/ff8a160b2ccafe5031612c084dfcd3cc95950414
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/more-itertools/0d43a836dac65c0ea426ad49c881a1086600bf85
/usr/share/package-licenses/more-itertools/ff8a160b2ccafe5031612c084dfcd3cc95950414

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

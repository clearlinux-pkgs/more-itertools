#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : more-itertools
Version  : 5.0.0
Release  : 11
URL      : https://files.pythonhosted.org/packages/dd/26/30fc0d541d9fdf55faf5ba4b0fd68f81d5bd2447579224820ad525934178/more-itertools-5.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/dd/26/30fc0d541d9fdf55faf5ba4b0fd68f81d5bd2447579224820ad525934178/more-itertools-5.0.0.tar.gz
Summary  : More routines for operating on iterables, beyond itertools
Group    : Development/Tools
License  : MIT
Requires: more-itertools-license = %{version}-%{release}
Requires: more-itertools-python = %{version}-%{release}
Requires: more-itertools-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
More Itertools
        ==============

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
%setup -q -n more-itertools-5.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545954204
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/more-itertools
cp LICENSE %{buildroot}/usr/share/package-licenses/more-itertools/LICENSE
cp docs/license.rst %{buildroot}/usr/share/package-licenses/more-itertools/docs_license.rst
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/more-itertools/LICENSE
/usr/share/package-licenses/more-itertools/docs_license.rst

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : more-itertools
Version  : 4.1.0
Release  : 5
URL      : https://files.pythonhosted.org/packages/db/0b/f5660bf6299ec5b9f17bd36096fa8148a1c843fa77ddfddf9bebac9301f7/more-itertools-4.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/db/0b/f5660bf6299ec5b9f17bd36096fa8148a1c843fa77ddfddf9bebac9301f7/more-itertools-4.1.0.tar.gz
Summary  : More routines for operating on iterables, beyond itertools
Group    : Development/Tools
License  : MIT
Requires: more-itertools-python3
Requires: more-itertools-license
Requires: more-itertools-python
Requires: six
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

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
Requires: more-itertools-python3

%description python
python components for the more-itertools package.


%package python3
Summary: python3 components for the more-itertools package.
Group: Default
Requires: python3-core

%description python3
python3 components for the more-itertools package.


%prep
%setup -q -n more-itertools-4.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530323505
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/more-itertools
cp LICENSE %{buildroot}/usr/share/doc/more-itertools/LICENSE
cp docs/license.rst %{buildroot}/usr/share/doc/more-itertools/docs_license.rst
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/more-itertools/LICENSE
/usr/share/doc/more-itertools/docs_license.rst

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libkomparediff2
Version  : 21.12.0
Release  : 35
URL      : https://download.kde.org/stable/release-service/21.12.0/src/libkomparediff2-21.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.12.0/src/libkomparediff2-21.12.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 LGPL-2.0
Requires: libkomparediff2-data = %{version}-%{release}
Requires: libkomparediff2-lib = %{version}-%{release}
Requires: libkomparediff2-license = %{version}-%{release}
Requires: libkomparediff2-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data

%description
No detailed description available

%package data
Summary: data components for the libkomparediff2 package.
Group: Data

%description data
data components for the libkomparediff2 package.


%package dev
Summary: dev components for the libkomparediff2 package.
Group: Development
Requires: libkomparediff2-lib = %{version}-%{release}
Requires: libkomparediff2-data = %{version}-%{release}
Provides: libkomparediff2-devel = %{version}-%{release}
Requires: libkomparediff2 = %{version}-%{release}

%description dev
dev components for the libkomparediff2 package.


%package lib
Summary: lib components for the libkomparediff2 package.
Group: Libraries
Requires: libkomparediff2-data = %{version}-%{release}
Requires: libkomparediff2-license = %{version}-%{release}

%description lib
lib components for the libkomparediff2 package.


%package license
Summary: license components for the libkomparediff2 package.
Group: Default

%description license
license components for the libkomparediff2 package.


%package locales
Summary: locales components for the libkomparediff2 package.
Group: Default

%description locales
locales components for the libkomparediff2 package.


%prep
%setup -q -n libkomparediff2-21.12.0
cd %{_builddir}/libkomparediff2-21.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639668681
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1639668681
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkomparediff2
cp %{_builddir}/libkomparediff2-21.12.0/COPYING %{buildroot}/usr/share/package-licenses/libkomparediff2/3bbe716f8282e9688952d7abe4c1612794fe790d
cp %{_builddir}/libkomparediff2-21.12.0/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/libkomparediff2/ff3ed70db4739b3c6747c7f624fe2bad70802987
cp %{_builddir}/libkomparediff2-21.12.0/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkomparediff2/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/libkomparediff2-21.12.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkomparediff2/20079e8f79713dce80ab09774505773c926afa2a
pushd clr-build
%make_install
popd
%find_lang libkomparediff2

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/libkomparediff2.categories

%files dev
%defattr(-,root,root,-)
/usr/include/libkomparediff2/diff2_export.h
/usr/include/libkomparediff2/difference.h
/usr/include/libkomparediff2/diffhunk.h
/usr/include/libkomparediff2/diffmodel.h
/usr/include/libkomparediff2/diffmodellist.h
/usr/include/libkomparediff2/diffsettings.h
/usr/include/libkomparediff2/kompare.h
/usr/include/libkomparediff2/komparemodellist.h
/usr/include/libkomparediff2/marker.h
/usr/include/libkomparediff2/settingsbase.h
/usr/lib64/cmake/LibKompareDiff2/LibKompareDiff2Config.cmake
/usr/lib64/cmake/LibKompareDiff2/LibKompareDiff2ConfigVersion.cmake
/usr/lib64/cmake/LibKompareDiff2/LibKompareDiff2Targets-relwithdebinfo.cmake
/usr/lib64/cmake/LibKompareDiff2/LibKompareDiff2Targets.cmake
/usr/lib64/libkomparediff2.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkomparediff2.so.5
/usr/lib64/libkomparediff2.so.5.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkomparediff2/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/libkomparediff2/3bbe716f8282e9688952d7abe4c1612794fe790d
/usr/share/package-licenses/libkomparediff2/e712eadfab0d2357c0f50f599ef35ee0d87534cb
/usr/share/package-licenses/libkomparediff2/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files locales -f libkomparediff2.lang
%defattr(-,root,root,-)


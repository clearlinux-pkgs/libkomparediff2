#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : libkomparediff2
Version  : 19.08.0
Release  : 11
URL      : https://download.kde.org/stable/applications/19.08.0/src/libkomparediff2-19.08.0.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.0/src/libkomparediff2-19.08.0.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.0/src/libkomparediff2-19.08.0.tar.xz.sig
Summary  : Library to compare files and strings
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: libkomparediff2-lib = %{version}-%{release}
Requires: libkomparediff2-license = %{version}-%{release}
Requires: libkomparediff2-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde

%description
No detailed description available

%package dev
Summary: dev components for the libkomparediff2 package.
Group: Development
Requires: libkomparediff2-lib = %{version}-%{release}
Provides: libkomparediff2-devel = %{version}-%{release}
Requires: libkomparediff2 = %{version}-%{release}
Requires: libkomparediff2 = %{version}-%{release}

%description dev
dev components for the libkomparediff2 package.


%package lib
Summary: lib components for the libkomparediff2 package.
Group: Libraries
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
%setup -q -n libkomparediff2-19.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565914050
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1565914050
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkomparediff2
cp COPYING %{buildroot}/usr/share/package-licenses/libkomparediff2/COPYING
cp COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/libkomparediff2/COPYING-CMAKE-SCRIPTS
cp COPYING.GPL2 %{buildroot}/usr/share/package-licenses/libkomparediff2/COPYING.GPL2
cp COPYING.GPL3 %{buildroot}/usr/share/package-licenses/libkomparediff2/COPYING.GPL3
cp COPYING.LGPL2 %{buildroot}/usr/share/package-licenses/libkomparediff2/COPYING.LGPL2
cp COPYING.LGPL2.1 %{buildroot}/usr/share/package-licenses/libkomparediff2/COPYING.LGPL2.1
cp COPYING.LGPL3 %{buildroot}/usr/share/package-licenses/libkomparediff2/COPYING.LGPL3
pushd clr-build
%make_install
popd
%find_lang libkomparediff2

%files
%defattr(-,root,root,-)

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
/usr/share/package-licenses/libkomparediff2/COPYING
/usr/share/package-licenses/libkomparediff2/COPYING-CMAKE-SCRIPTS
/usr/share/package-licenses/libkomparediff2/COPYING.GPL2
/usr/share/package-licenses/libkomparediff2/COPYING.GPL3
/usr/share/package-licenses/libkomparediff2/COPYING.LGPL2
/usr/share/package-licenses/libkomparediff2/COPYING.LGPL2.1
/usr/share/package-licenses/libkomparediff2/COPYING.LGPL3

%files locales -f libkomparediff2.lang
%defattr(-,root,root,-)


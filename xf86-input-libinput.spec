#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v13
# autospec commit: dc0ff31
#
# Source0 file verified with key 0xE23B7E70B467F0BF (office@who-t.net)
#
Name     : xf86-input-libinput
Version  : 1.4.0
Release  : 36
URL      : https://www.x.org/releases/individual/driver/xf86-input-libinput-1.4.0.tar.xz
Source0  : https://www.x.org/releases/individual/driver/xf86-input-libinput-1.4.0.tar.xz
Source1  : https://www.x.org/releases/individual/driver/xf86-input-libinput-1.4.0.tar.xz.sig
Source2  : E23B7E70B467F0BF.pkey
Summary  : X.Org libinput input driver.
Group    : Development/Tools
License  : MIT
Requires: xf86-input-libinput-data = %{version}-%{release}
Requires: xf86-input-libinput-lib = %{version}-%{release}
Requires: xf86-input-libinput-license = %{version}-%{release}
Requires: xf86-input-libinput-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : file
BuildRequires : gnupg
BuildRequires : libpciaccess-dev
BuildRequires : pkgconfig(inputproto)
BuildRequires : pkgconfig(libinput)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)
BuildRequires : pkgconfig(xproto)
BuildRequires : systemd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Bump-priority-of-libinput.patch

%description
xf86-input-libinput - a libinput-based X driver
===============================================

%package data
Summary: data components for the xf86-input-libinput package.
Group: Data

%description data
data components for the xf86-input-libinput package.


%package dev
Summary: dev components for the xf86-input-libinput package.
Group: Development
Requires: xf86-input-libinput-lib = %{version}-%{release}
Requires: xf86-input-libinput-data = %{version}-%{release}
Provides: xf86-input-libinput-devel = %{version}-%{release}
Requires: xf86-input-libinput = %{version}-%{release}

%description dev
dev components for the xf86-input-libinput package.


%package lib
Summary: lib components for the xf86-input-libinput package.
Group: Libraries
Requires: xf86-input-libinput-data = %{version}-%{release}
Requires: xf86-input-libinput-license = %{version}-%{release}

%description lib
lib components for the xf86-input-libinput package.


%package license
Summary: license components for the xf86-input-libinput package.
Group: Default

%description license
license components for the xf86-input-libinput package.


%package man
Summary: man components for the xf86-input-libinput package.
Group: Default

%description man
man components for the xf86-input-libinput package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) E23B7E70B467F0BF' gpg.status
%setup -q -n xf86-input-libinput-1.4.0
cd %{_builddir}/xf86-input-libinput-1.4.0
%patch -P 1 -p1
pushd ..
cp -a xf86-input-libinput-1.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1720015572
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="-O3 -g -fopt-info-vec "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%reconfigure --disable-static
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%reconfigure --disable-static
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="-O3 -g -fopt-info-vec "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1720015572
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xf86-input-libinput
cp %{_builddir}/xf86-input-libinput-%{version}/COPYING %{buildroot}/usr/share/package-licenses/xf86-input-libinput/fa42615cf49e7d89b1e2008fe33ff6d00a9b0f5c || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/X11/xorg.conf.d/80-libinput.conf

%files dev
%defattr(-,root,root,-)
/usr/include/xorg/libinput-properties.h
/usr/lib64/pkgconfig/xorg-libinput.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/xorg/modules/input/libinput_drv.so
/usr/lib64/xorg/modules/input/libinput_drv.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xf86-input-libinput/fa42615cf49e7d89b1e2008fe33ff6d00a9b0f5c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man4/libinput.4

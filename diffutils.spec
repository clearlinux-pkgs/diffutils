#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7FD9FCCB000BEEEE (meyering@fb.com)
#
Name     : diffutils
Version  : 3.9
Release  : 29
URL      : https://mirrors.kernel.org/gnu/diffutils/diffutils-3.9.tar.xz
Source0  : https://mirrors.kernel.org/gnu/diffutils/diffutils-3.9.tar.xz
Source1  : https://mirrors.kernel.org/gnu/diffutils/diffutils-3.9.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: diffutils-bin = %{version}-%{release}
Requires: diffutils-info = %{version}-%{release}
Requires: diffutils-license = %{version}-%{release}
Requires: diffutils-locales = %{version}-%{release}
Requires: diffutils-man = %{version}-%{release}
BuildRequires : glibc-locale
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This directory contains the GNU diff, diff3, sdiff, and cmp utilities.
Their features are a superset of the Unix features and they are
significantly faster.

%package bin
Summary: bin components for the diffutils package.
Group: Binaries
Requires: diffutils-license = %{version}-%{release}

%description bin
bin components for the diffutils package.


%package info
Summary: info components for the diffutils package.
Group: Default

%description info
info components for the diffutils package.


%package license
Summary: license components for the diffutils package.
Group: Default

%description license
license components for the diffutils package.


%package locales
Summary: locales components for the diffutils package.
Group: Default

%description locales
locales components for the diffutils package.


%package man
Summary: man components for the diffutils package.
Group: Default

%description man
man components for the diffutils package.


%prep
%setup -q -n diffutils-3.9
cd %{_builddir}/diffutils-3.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1673888871
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1673888871
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/diffutils
cp %{_builddir}/diffutils-%{version}/COPYING %{buildroot}/usr/share/package-licenses/diffutils/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
%make_install
%find_lang diffutils

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cmp
/usr/bin/diff
/usr/bin/diff3
/usr/bin/sdiff

%files info
%defattr(0644,root,root,0755)
/usr/share/info/diffutils.info

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/diffutils/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cmp.1
/usr/share/man/man1/diff.1
/usr/share/man/man1/diff3.1
/usr/share/man/man1/sdiff.1

%files locales -f diffutils.lang
%defattr(-,root,root,-)


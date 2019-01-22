#
# spec file for package opsi-windows-support
#
# Copyright (c) 2017 uib GmbH.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
Name:           opsi-windows-support
Url:            https://www.opsi.org
License:        AGPL-3.0
Group:          Productivity/Networking/Opsi
Version:        4.1.1
Release:        6
Source:         opsi-windows-support_4.1.1-6.tar.gz
Requires:       wimlib
Requires:       cabextract
Requires:       samba-client
%if 0%{?suse_version} || 0%{?is_opensuse}
Requires:       winexe
%endif
Summary:        Install utilities useful for deploying Windows with opsi.
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# ===[ description ]================================
%description
This package configures the system that a deployment
of Linux distributions via opsi is possible

# ===[ prep ]=======================================
%prep

# ===[ setup ]======================================
%setup -n %{name}-%{version}

# ===[ build ]======================================
%build

# ===[ install ]====================================
%install

# ===[ clean ]======================================
%clean

# ===[ post ]=======================================
%post

# ===[ files ]======================================
%files

# ===[ changelog ]==================================
%changelog

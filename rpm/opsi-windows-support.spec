#
# spec file for package opsi-windows-support
#
# Copyright (c) 2017 uib GmbH.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
Name:           opsi-windows-support

Requires:       wimtools
%if 0%{?rhel_version} || 0%{?centos_version} || 0%{?fedora_version}
Requires:		cabextract
Requires:		p7zip
Requires:		p7zip-plugins
%endif
Url:            https://www.opsi.org
License:        AGPL-3.0
Group:          Productivity/Networking/Opsi
Version:        4.1.1
Release:        1
Source:         opsi-windows-support_4.1.1-1.tar.gz
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

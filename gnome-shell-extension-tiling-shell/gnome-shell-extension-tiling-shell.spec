%global debug_package %{nil}
%global extid tilingshell@ferrarodomenico.com

Name:           gnome-shell-extension-tiling-shell
Version:        18.0
Release:        2%{?dist}
Summary:        Extend GNOME Shell with advanced tiling window management

License:        GPL-3.0-or-later
URL:            https://github.com/domferr/tilingshell
Source0:        %{url}/releases/download/%{version}/%{extid}.zip

BuildArch:      noarch

BuildRequires:  unzip
BuildRequires:  gettext
BuildRequires:  glib2-devel

Requires:       gnome-shell >= 45

%description
Extend GNOME Shell with advanced tiling window management.

%prep
%setup -q -c -n "%{extid}" -T
unzip -q -o %{SOURCE0} -d .
sed -i '/^#!@GJS@ -m$/d' monitorDescription.js

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}

cp -a * %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/

if [ -d %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/schemas ]; then
glib-compile-schemas %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/schemas
fi

%files
%{_datadir}/gnome-shell/extensions/%{extid}

%changelog
%autochangelog

%global debug_package %{nil}
%global extid tilingshell@ferrarodomenico.com

Name:           gnome-shell-extension-tiling-shell
Version:        17.3
Release:        1%{?dist}
Summary:        Extend Gnome Shell with advanced tiling window management

License:        GPL-3.0-or-later
URL:            https://github.com/domferr/tilingshell
Source0:        %{url}/releases/download/%{version}/tilingshell@ferrarodomenico.com.zip

BuildArch:      noarch

BuildRequires:  unzip
BuildRequires:  gettext
BuildRequires:  glib2-devel

Requires:       gnome-shell >= 45

%description
Extend Gnome Shell with advanced tiling window management. Supports multiple monitors, Windows 11 Snap Assistant, Fancy Zones, automatic tiling, keyboard shortcuts, customised tiling layouts and more!

%prep
%setup -q -c -n "%{extid}" -T
unzip -q -o %{SOURCE0} -d .

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}
cp -r -p * %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/

# Compile GSettings schemas
if [ -d %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/schemas ]; then
    glib-compile-schemas %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/schemas
fi

%files
%dir %{_datadir}/gnome-shell/extensions/%{extid}
%{_datadir}/gnome-shell/extensions/%{extid}/*

%changelog
%autochangelog
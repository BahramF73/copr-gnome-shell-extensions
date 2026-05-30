%global debug_package %{nil}
%global uuid netspeedsimplified
%global extid %{uuid}@prateekmedia.extension

Name:           gnome-shell-extension-%{uuid}
Version:        46
Release:        1%{?dist}
Summary:        Simple network speed indicator for GNOME Shell

License:        GPL-3.0-or-later
URL:            https://github.com/prateekmedia/%{uuid}
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  glib2-devel

Requires:       gnome-shell

%description
NetSpeed Simplified is a GNOME Shell extension that displays
network upload and download speeds in the top panel.

%prep
%autosetup -n %{name}-%{version}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}

cp -a extension.js
metadata.json
prefs.js
stylesheet.css
LICENSE
%{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/

if [ -d schemas ]; then
cp -a schemas %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/
glib-compile-schemas
%{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/schemas
fi

%files
%license LICENSE
%dir %{_datadir}/gnome-shell/extensions/%{extid}
%{_datadir}/gnome-shell/extensions/%{extid}

%changelog
%autochangelog

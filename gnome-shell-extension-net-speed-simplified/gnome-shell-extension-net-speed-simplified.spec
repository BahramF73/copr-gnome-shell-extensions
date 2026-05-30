%global debug_package %{nil}
%global uuid netspeedsimplified
%global extid %{uuid}@prateekmedia.extension

Name:           gnome-shell-extension-net-speed-simplified
Version:        46
Release:        1%{?dist}
Summary:        A Net Speed monitor With Loads of Customization

License:        GPL-3.0-or-later
URL:            https://github.com/prateekmedia/netspeedsimplified
Source0:        %{extid}-%{version}.zip

BuildArch:      noarch

BuildRequires:  glib2-devel

Requires:       gnome-shell

%description
A Net Speed monitor With Loads of Customization.
Supports GNOME 45 through 50. For GNOME Shell versions earlier than 45, use previous releases of this extension.

%prep
%autosetup -n %{extid}-%{version}

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

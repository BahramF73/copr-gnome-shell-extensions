%global debug_package %{nil}
%global uuid netspeedsimplified
%global extid %{uuid}@prateekmedia.extension

Name:           gnome-shell-extension-net-speed-simplified
Version:        46
Release:        1%{?dist}
Summary:        A Net Speed monitor With Loads of Customization

License:        GPL-3.0-or-later
URL:            https://github.com/prateekmedia/netspeedsimplified
Source0:        %{url}/releases/download/%{version}/%{extid}-%{version}.zip

BuildArch:      noarch

BuildRequires:  glib2-devel unzip

Requires:       gnome-shell >= 45

%description
A Net Speed monitor With Loads of Customization.
Supports GNOME 45 through 50. For GNOME Shell versions earlier than 45, use previous releases of this extension.

%prep
%setup -q -c -n "%{extid}" -T
unzip -q -o %{SOURCE0} -d .
rm -rf __MACOSX

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

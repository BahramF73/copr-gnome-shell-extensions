%global debug_package %{nil}
%global extid ddterm@amezin.github.com

Name:           gnome-shell-extension-ddterm
Version:        63.2.0
Release:        1%{?dist}
Summary:        Another Drop Down Terminal Extension for GNOME Shell

License:        GPL-3.0-or-later
URL:            https://github.com/ddterm/gnome-shell-extension-ddterm
Source0:        %{url}/releases/download/v%{version}/%{extid}.shell-extension.zip

BuildArch:      noarch

BuildRequires:  unzip
BuildRequires:  gettext
BuildRequires:  glib2-devel

Requires:       gnome-shell >= 46

%description
Another drop down terminal extension for GNOME Shell. With tabs. Works on Wayland natively

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
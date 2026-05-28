%global extid ddterm@amezin.github.com

Name:           gnome-shell-extension-ddterm
Version:        63.0.1
Release:        1%{?dist}
Summary:        Another Drop Down Terminal Extension for GNOME Shell

License:        GPL-3.0-or-later
URL:            https://github.com/ddterm/gnome-shell-extension-ddterm
Source0:        %{url}/releases/download/v%{version}/%{extid}.shell-extension.zip

BuildArch:      noarch

BuildRequires:  unzip
BuildRequires:  glib2

Requires:       gnome-shell >= 46

%description
Another drop down terminal extension for GNOME Shell. With tabs. Works on Wayland natively

%prep
%setup -q -c -n %{extid} -T

%build

%install
install -d %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}

unzip -q %{SOURCE0} \
    -d %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}

# Compile GSettings schemas
if [ -d %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/schemas ]; then
    glib-compile-schemas \
        %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/schemas
fi

%files
%dir %{_datadir}/gnome-shell/extensions/%{extid}
%{_datadir}/gnome-shell/extensions/%{extid}/*

%changelog
%autochangelog
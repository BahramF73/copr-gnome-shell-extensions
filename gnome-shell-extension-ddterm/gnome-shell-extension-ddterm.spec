%global extid   ddterm@amezin.github.com

Name:           gnome-shell-extension-ddterm
Version:        63.0.1
Release:        1%{?dist}
Summary:        Another Drop Down Terminal Extension for GNOME Shell

License:        GPL-3.0-or-later
URL:            https://github.com/ddterm/gnome-shell-extension-ddterm
Source0:        %{url}/releases/download/v%{version}/ddterm@amezin.github.com.shell-extension.zip
BuildArch:      noarch

BuildRequires:  /usr/bin/glib-compile-schemas
BuildRequires:  unzip

Requires:       gnome-shell

%description
Another drop down terminal extension for GNOME Shell. With tabs. Works on Wayland natively

%prep

%build

%check

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}
unzip %{SOURCE0} -d %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas
mv %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/schemas/com.github.amezin.ddterm.gschema.xml \
	%{buildroot}%{_datadir}/glib-2.0/schemas/

rm -rf %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/schemas/

%files
%{_datadir}/gnome-shell/extensions/%{extid}/
%{_datadir}/glib-2.0/schemas/*


%changelog
%autochangelog
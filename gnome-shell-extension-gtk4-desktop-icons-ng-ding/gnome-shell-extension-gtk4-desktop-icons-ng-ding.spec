%global debug_package %{nil}
%global extid gtk4-ding@smedius.gitlab.com

Name:           gnome-shell-extension-gtk4-desktop-icons-ng-ding
Version:        100.17
Release:        1%{?dist}
Summary:        Libadwaita/Gtk4 port of Desktop Icons NG with multiple fixes and new features.
License:        GPL-3.0-or-later
URL:            https://gitlab.com/smedius/desktop-icons-ng
Source0:        %{url}/-/archive/Gtk4-%{version}/desktop-icons-ng-Gtk4-%{version}.zip

BuildRequires:  unzip
BuildRequires:  gettext
BuildRequires:  glib2-devel
Requires:       gnome-shell >= 45
BuildArch:      noarch

%description
Gtk4 Desktop Icons NG is an extension and a program together for the GNOME Shell that renders icons on the desktop. It is a fork from DING.

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
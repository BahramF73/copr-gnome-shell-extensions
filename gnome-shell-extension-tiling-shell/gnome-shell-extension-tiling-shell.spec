%global debug_package %{nil}
%global extid [tilingshell@ferrarodomenico.com](mailto:tilingshell@ferrarodomenico.com)

Name:           gnome-shell-extension-tiling-shell
Version:        18.0
Release:        1%{?dist}
Summary:        Extend GNOME Shell with advanced tiling window management

License:        GPL-3.0-or-later
URL:            https://github.com/domferr/tilingshell
Source0:        %{url}/archive/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  nodejs
BuildRequires:  npm
BuildRequires:  gettext
BuildRequires:  glib2-devel

Requires:       gnome-shell >= 45

%description
Extend GNOME Shell with advanced tiling window management.

%prep
%autosetup -n tilingshell-%{version}

%build
npm install
npm run build

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}

cp -a ./* %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/

rm -rf %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/src
rm -rf %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/node_modules
rm -rf %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/translations
rm -rf %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/doc

find %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}
-name "*.ts" -delete

if [ -d %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/schemas ]; then
glib-compile-schemas %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/schemas
fi

%files
%{_datadir}/gnome-shell/extensions/%{extid}

%changelog
%autochangelog

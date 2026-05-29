%global debug_package %{nil}
%global extid tilingshell@ferrarodomenico.com

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

cp -a dist/* %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/

if [ -d %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/schemas ]; then
glib-compile-schemas %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/schemas
fi

%files
%{_datadir}/gnome-shell/extensions/%{extid}

%changelog
%autochangelog

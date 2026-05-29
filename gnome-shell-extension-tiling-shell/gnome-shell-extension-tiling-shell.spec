%global debug_package %{nil}
%global extid tilingshell@ferrarodomenico.com

Name:           gnome-shell-extension-tiling-shell
Version:        18.0
Release:        1%{?dist}
Summary:        Extend Gnome Shell with advanced tiling window management

License:        GPL-3.0-or-later
URL:            https://github.com/domferr/tilingshell
Source0:        %{url}/archive/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gettext
BuildRequires:  glib2-devel

Requires:       gnome-shell >= 45

%description
Extend Gnome Shell with advanced tiling window management. Supports multiple monitors, Windows 11 Snap Assistant, Fancy Zones, automatic tiling, keyboard shortcuts, customised tiling layouts and more!

%prep
%autosetup -n tilingshell-%{version}

%build
meson setup builddir --prefix=%{_prefix} --libdir=%{_libdir}
meson compile -C builddir

%install
meson install -C builddir --destdir %{buildroot}

# Compile GSettings schemas if present
if [ -d %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/schemas ]; then
    glib-compile-schemas %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/schemas
fi

%files
%dir %{_datadir}/gnome-shell/extensions/%{extid}
%{_datadir}/gnome-shell/extensions/%{extid}/*

%changelog
%autochangelog
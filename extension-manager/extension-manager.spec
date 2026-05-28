Name:           extension-manager
Version:        0.6.5
Release:        1%{?dist}
Summary:        A utility for browsing and installing GNOME Shell Extensions.
License:        GPL-3.0-or-later
URL:            https://github.com/mjakeman/extension-manager
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:    git
BuildRequires:    meson gcc blueprint-compiler gettext desktop-file-utils libappstream-glib
BuildRequires:    pkgconfig(gtk4) pkgconfig(libadwaita-1) pkgconfig(json-glib-1.0) pkgconfig(libsoup-3.0) pkgconfig(libxml-2.0) pkgconfig(gio-unix-2.0)

%description
A native tool for browsing, installing, and managing GNOME Shell Extensions

%prep
%autosetup -n %{name}-%{version}

%build
%meson -Dbacktrace=false
%meson_build

%install
%meson_install
%find_lang %{name}

%check
%meson_test
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
glib-compile-schemas --dry-run --strict %{buildroot}%{_datadir}/glib-2.0/schemas/

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/icons/hicolor/symbolic/apps/*.svg
%{_metainfodir}/*.metainfo.xml
%{_datadir}/glib-2.0/schemas/*.gschema.xml

%changelog
%autochangelog

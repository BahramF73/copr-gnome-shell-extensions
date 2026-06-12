Name:           gnome-shell-extension-gtk4-ding
Version:        100.23
Release:        2%{?dist}
Summary:        Gtk4/libadwaita Desktop Icons NG extension for GNOME Shell
License:        GPL-3.0-or-later
URL:            https://gitlab.com/smedius/desktop-icons-ng
Source0:        https://gitlab.com/smedius/desktop-icons-ng/-/archive/gtk4-%{version}/desktop-icons-ng-gtk4-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gettext
BuildRequires:  glib2-devel

Requires:       gjs
Requires:       nautilus >= 3.38
Requires:       gsettings-desktop-schemas
Requires:       gnome-shell >= 49
Requires:       gnome-shell < 51

%global debug_package %{nil}

%description
Gtk4 Desktop Icons NG (DING) is a Gtk4/libadwaita fork of the Desktop Icons GNOME Shell extension.

%prep
%autosetup -n desktop-icons-ng-gtk4-%{version}

%build
meson setup build --prefix=%{_prefix} --buildtype=release
meson compile -C build

%install
rm -rf %{buildroot}
meson install -C build --destdir %{buildroot}

find %{buildroot}%{_prefix} -xtype f -o -type f -o -type l | sed "s|%{buildroot}||" > filelist

%files -f filelist
%license COPYING
%doc README.md HISTORY.md FEATURES.md ISSUES.md

%post
if command -v glib-compile-schemas >/dev/null 2>&1; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas >/dev/null 2>&1 || :
fi

%postun
if command -v glib-compile-schemas >/dev/null 2>&1; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas >/dev/null 2>&1 || :
fi
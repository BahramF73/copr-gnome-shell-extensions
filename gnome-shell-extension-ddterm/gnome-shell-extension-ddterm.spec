%global extdir      ddterm@amezin.github.com
%global gschemadir  %{_datadir}/glib-2.0/schemas

Name:           gnome-shell-extension-ddterm
Version:        63.0.1
Release:        %autorelease
Summary:        Drop-down terminal extension for GNOME Shell

License:        GPL-3.0-or-later
URL:            https://github.com/ddterm/gnome-shell-extension-ddterm
Source0:        https://github.com/ddterm/gnome-shell-extension-ddterm/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gettext
BuildRequires:  xsltproc
BuildRequires:  glib2-devel

Requires:       gnome-shell-extension-common

%description
ddterm is a drop-down terminal extension for GNOME Shell similar to Guake or Yakuake.
It provides a fast-access terminal that slides down from the top of the screen.

%prep
%autosetup -n ddterm-%{version}

%build
meson setup builddir
ninja -C builddir

# bundle step (important for GNOME extensions)
ninja -C builddir bundle

%install
rm -rf %{buildroot}

# install bundle (preferred instead of system-wide meson install)
DESTDIR=%{buildroot} meson install -C builddir

# convert the absolute symlink installed by meson into a relative one
rm -f %{buildroot}%{_bindir}/com.github.amezin.ddterm
ln -s ../share/gnome-shell/extensions/%{extdir}/bin/com.github.amezin.ddterm \
	%{buildroot}%{_bindir}/com.github.amezin.ddterm

%files
%license LICENSE*
%doc README.md

%{_bindir}/com.github.amezin.ddterm
%{_datadir}/applications/com.github.amezin.ddterm.desktop
%{_datadir}/dbus-1/services/com.github.amezin.ddterm.service

%{_datadir}/gnome-shell/extensions/*
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.ddterm.gschema.xml

%changelog
%autochangelog
%global extdir      kimpanel@kde.org
%global gschemadir  %{_datadir}/glib-2.0/schemas

Name:           gnome-shell-extension-kimpanel
Version:        0^20240512.git9a7c460
Release:        %autorelease
Summary:        KDE kimpanel protocol for gnome shell

License:        GPLv2
URL:            https://github.com/wengxt/gnome-shell-extension-kimpanel
Source0:        https://github.com/wengxt/gnome-shell-extension-kimpanel/archive/9a7c46042c5a6ac3bfc265a7ca1cc4cedf65a6f3.tar.gz

BuildArch:      noarch

BuildRequires:  gettext cmake
BuildRequires:  %{_bindir}/glib-compile-schemas
Requires:       gnome-shell-extension-common

%description
This extension implements the KDE kimpanel protocol for gnome shell. It provides a native
pop-up window for input method listings and an appindicator based tray icon for configurations.

%prep
%autosetup -n gnome-shell-extension-kimpanel-9a7c46042c5a6ac3bfc265a7ca1cc4cedf65a6f3

%build
%cmake
%cmake_build
glib-compile-schemas --strict --targetdir=schemas/ schemas

%install
mkdir -p %{buildroot}%{gschemadir}
%cmake_install
cp -pr schemas/org.gnome.shell.extensions.kimpanel.gschema.xml %{buildroot}%{gschemadir}

# Fedora and EPEL 8 handles post scripts via triggers
%if 0%{?rhel} && 0%{?rhel} <= 7
%postun
if [ $1 -eq 0 ]; then
  %{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || true
fi

%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || true
%endif

%files
%license COPYING
%{_datadir}/gnome-shell/extensions/%{extdir}
%{_datadir}/locale/*/LC_MESSAGES/gnome-shell-extensions-kimpanel.mo
%{gschemadir}

%changelog
%autochangelog

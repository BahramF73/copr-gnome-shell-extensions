%global extuuid		gtk4-ding@smedius.gitlab.com
%global extdir		%{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir	%{_datadir}/glib-2.0/schemas
%global gitname		desktop-icons-ng
%global giturl		https://gitlab.com/smedius/%{gitname}
%global srcdir		%{_builddir}/%{gitname}-%{version}/src

Name:		gnome-shell-extension-gtk4-desktop-icons-ng
Version:	100.23
Release:	1%{?dist}
Summary:	Libadwaita/Gtk4 port of Desktop Icons NG with multiple fixes and new features.

License:	GPL-3.0-or-later
URL:		https://extensions.gnome.org/extension/5263/gtk4-desktop-icons-ng-ding/
Source0:	%{giturl}/-/archive/Gtk4-%{version}/desktop-icons-ng-Gtk4-%{version}.zip
BuildArch:	noarch

BuildRequires:  gobject-introspection
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
Requires:       gnome-shell >= 50

%description
Gtk4 Desktop Icons NG is an extension and a program together for the GNOME Shell that renders icons on the desktop. It is a fork from DING.

%prep
%autosetup -n %{gitname}-Gtk4-%{version}
sed -e "/meson_post_install/d" -i meson.build

%build
%meson --localedir=%{_datadir}/locale
%meson_build

%install
%meson_install

%postun
if [ $1 -eq 0 ] ; then
  %{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
  %{_bindir}/glib-compile-schemas %{extdir}/schemas &> /dev/null || :
fi

%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
%{_bindir}/glib-compile-schemas %{extdir}/schemas &> /dev/null || :

%files
%{extdir}
/usr/share/locale/*/LC_MESSAGES/gtk4-ding.mo
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.gtk4-ding.gschema.xml

%changelog
%autochangelog
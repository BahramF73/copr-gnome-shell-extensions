%global extid   %{extname}@rastersoft.com
%global extname ding
%global extname_full desktop-icons-ng
%global uuid    org.gnome.shell.extensions.%{extname}

Name:           gnome-shell-extension-%{extname_full}-%{extname}
Version:        51.0.3
Release:        1%{?dist}
Summary:        DING Desktop Icons New Generation

License:        GPLv3+
URL:            https://gitlab.com/rastersoft/desktop-icons-ng
Source0:        %{url}/-/archive/%{version}/desktop-icons-ng-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  gobject-introspection
BuildRequires:  intltool
BuildRequires:  meson

Requires:       gnome-shell >= 46
Requires:       nautilus >= 46
Requires:       xdg-desktop-portal-gtk

%description
Adds icons to the desktop. Fork of the original Desktop Icons extension, with several enhancements.

%prep
%autosetup -n %{extname_full}-%{version} -p1
sed -e "/meson_post_install/d" -i meson.build


%build
%meson --localedir=%{_datadir}/locale
%meson_build


%install
%meson_install
%find_lang %{extname}


%files -f %{extname}.lang
%license COPYING
%doc README.md
%config %{_sysconfdir}/apparmor.d/desktop-icons-ng
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml
%{_datadir}/gnome-shell/extensions/%{extid}/


%changelog
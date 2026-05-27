%global extdir      arcmenu@arcmenu.com
%global gschemadir  %{_datadir}/glib-2.0/schemas

Name:           gnome-shell-extension-arcmenu
Version:        69.0
Release:        1%{?dist}
Summary:        Application Menu Extension for GNOME

License:        GPLv2
URL:            https://gitlab.com/arcmenu/ArcMenu
Source0:        https://gitlab.com/arcmenu/ArcMenu/-/archive/v%{version}/ArcMenu-v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  glib2-devel
BuildRequires:  %{_bindir}/glib-compile-schemas

Requires:       gnome-shell-extension-common

%description
ArcMenu is an application menu for GNOME Shell, designed to provide a more
familiar user experience and workflow.

%prep
%autosetup -n ArcMenu-v%{version}


%build

%install
make DESTDIR=%{buildroot} install

%find_lang arcmenu

%files -f arcmenu.lang
%license LICENSE
%{_datadir}/gnome-shell/extensions/%{extdir}
%{gschemadir}/*arcmenu*

%changelog
%autochangelog
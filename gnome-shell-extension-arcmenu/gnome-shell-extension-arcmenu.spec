%global extdir      arcmenu@arcmenu.com
%global gschemadir  %{_datadir}/glib-2.0/schemas

Name:           gnome-shell-extension-arcmenu
Version:        69.2
Release:        1%{?dist}
Summary:        Application Menu Extension for GNOME

License:        GPLv2
URL:            https://gitlab.com/arcmenu/ArcMenu
Source0:        https://gitlab.com/arcmenu/ArcMenu/-/archive/v%{version}/ArcMenu-v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  glib2-devel

Requires:       gnome-shell-extension-common

%description
ArcMenu is an application menu for GNOME Shell, designed to provide a more
familiar user experience and workflow.

%prep
%autosetup -n ArcMenu-v%{version}

%build
make extension

%install
rm -rf %{buildroot}

# Install using upstream build system (IMPORTANT)
make DESTDIR=%{buildroot} install

# Fedora policy: ensure schemas are installed in correct location
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas
cp -a schemas/*.gschema.xml %{buildroot}%{_datadir}/glib-2.0/schemas/ || :

%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas >/dev/null 2>&1 || :

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas >/dev/null 2>&1 || :

%files
%license LICENSE
%doc README.md RELEASENOTES.md

%{_datadir}/gnome-shell/extensions/%{extdir}
%{_datadir}/glib-2.0/schemas/*arcmenu*
%{_datadir}/locale/*/LC_MESSAGES/arcmenu.mo

%changelog
%autochangelog
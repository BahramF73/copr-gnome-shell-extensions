%global extdir      clipboard-indicator@tudmotu.com
%global gschemadir  %{_datadir}/glib-2.0/schemas

Name:           gnome-shell-extension-clipboard-indicator
Version:        66
Release:        %autorelease
Summary:        The most popular clipboard manager for GNOME

License:        MIT
URL:            https://github.com/Tudmotu/gnome-shell-extension-clipboard-indicator
Source0:        https://github.com/Tudmotu/gnome-shell-extension-clipboard-indicator/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  gettext make
BuildRequires:  %{_bindir}/glib-compile-schemas
Requires:       gnome-shell-extension-common

%description
Clipboard Indicator is a Gnome Shell extension which provides an applet for
managing the system clipboard. Among other functionalities, it allows viewing
the clipboard content, pinning and cut, copy, paste of images.


%prep
%autosetup

# rename some lingering locale files to the match the extension name
for lc in ja ko; do
  mv locale/$lc/LC_MESSAGES/$lc.mo locale/$lc/LC_MESSAGES/clipboard-indicator.mo
  mv locale/$lc/LC_MESSAGES/$lc.po locale/$lc/LC_MESSAGES/clipboard-indicator.po
done

%build
make


%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{extdir}
mkdir -p %{buildroot}%{gschemadir}
cp -pr schemas/org.gnome.shell.extensions.clipboard-indicator.gschema.xml %{buildroot}%{gschemadir}
cp -pr --parents metadata.json stylesheet.css *.js \
  locale/*/LC_MESSAGES/*.mo \
  schemas/ \
  %{buildroot}%{_datadir}/gnome-shell/extensions/%{extdir}
%find_lang clipboard-indicator


# Fedora and EPEL 8 handles post scripts via triggers
%if 0%{?rhel} && 0%{?rhel} <= 7
%postun
if [ $1 -eq 0 ]; then
  %{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || true
fi

%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || true
%endif


%files -f clipboard-indicator.lang
%license LICENSE.rst
%{_datadir}/gnome-shell/extensions/%{extdir}/metadata.json
%{_datadir}/gnome-shell/extensions/%{extdir}/stylesheet.css
%{_datadir}/gnome-shell/extensions/%{extdir}/*.js
%{_datadir}/gnome-shell/extensions/%{extdir}/schemas
%{gschemadir}


%changelog
%autochangelog

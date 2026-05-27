%global extid clipboard-indicator@tudmotu.com

Name:           gnome-shell-extension-clipboard-indicator
Version:        71
Release:        %autorelease
Summary:        Clipboard Indicator GNOME extension

License:        MIT
URL:            https://github.com/Tudmotu/gnome-shell-extension-clipboard-indicator
Source0:        https://github.com/Tudmotu/gnome-shell-extension-clipboard-indicator/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

Requires:       gnome-shell

%description
Clipboard Indicator is a Gnome Shell extension which provides an applet for
managing the system clipboard. Among other functionalities, it allows viewing
the clipboard content, pinning and cut, copy, paste of images.


%prep
%autosetup -n gnome-shell-extension-clipboard-indicator-%{version}

%build
# nothing

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}

cp -a * %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/

rm -f %{buildroot}%{_datadir}/gnome-shell/extensions/%{extid}/schemas/gschemas.compiled

%files
%license LICENSE.rst
%{_datadir}/gnome-shell/extensions/%{extid}

%changelog
%autochangelog
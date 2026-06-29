%global uuid text-extractor@aditya190803
%global extdir %{_datadir}/gnome-shell/extensions/%{uuid}
%global commit main

Name:           gnome-shell-extension-text-extractor
Version:        5
Release:        1%{?dist}
Summary:        GNOME Shell extension for OCR text extraction from screen areas

License:        GPL-3.0-or-later
URL:            https://github.com/Aditya190803/TextExtractor
Source0:        %{url}/archive/refs/heads/%{commit}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  glib2
BuildRequires:  zip

Requires:       gnome-shell >= 48
Requires:       tesseract
Requires:       tesseract-langpack-eng
Requires:       python3
Requires:       python3-pytesseract
Requires:       python3-pillow

%description
Text Extractor is a GNOME Shell extension that extracts text from a selected
area of the screen using Tesseract OCR and copies the result to the clipboard.

%prep
%autosetup -n TextExtractor-%{commit}

%build
# Nothing to build

%install
rm -rf %{buildroot}

# Install GNOME Shell extension files
mkdir -p %{buildroot}%{extdir}
cp -a build/* %{buildroot}%{extdir}/

# Do not ship helper inside extension directory
rm -f %{buildroot}%{extdir}/ocr_helper.py

# Install helper
mkdir -p %{buildroot}%{_bindir}
install -m 0755 build/ocr_helper.py %{buildroot}%{_bindir}/text-extractor-ocr

# Compile schemas
if [ -d %{buildroot}%{extdir}/schemas ]; then
    glib-compile-schemas %{buildroot}%{extdir}/schemas
fi

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{extdir}
%{_bindir}/text-extractor-ocr

%changelog
* Mon Jun 29 2026 Bahram Farahmand <bahram.0098.bf@gmail.com> - 5-1
- Package upstream main branch snapshot
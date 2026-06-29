%global uuid text-extractor@aditya190803
%global extdir %{_datadir}/gnome-shell/extensions/%{uuid}

Name:           gnome-shell-extension-text-extractor
Version:        1.1.0
Release:        1%{?dist}
Summary:        GNOME Shell extension for OCR text extraction from screen areas

License:        GPL-3.0-or-later
URL:            https://github.com/Aditya190803/TextExtractor
Source0:        %{name}-%{version}.tar.gz

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
%autosetup -n %{name}-%{version}

%build
# Nothing to build

%install
rm -rf %{buildroot}

# Install GNOME Shell extension files
mkdir -p %{buildroot}%{extdir}
cp -a build/* %{buildroot}%{extdir}/

# OCR helper should not be bundled inside extension directory
rm -f %{buildroot}%{extdir}/ocr_helper.py

# Install OCR helper system-wide
mkdir -p %{buildroot}%{_bindir}
install -m 0755 build/ocr_helper.py %{buildroot}%{_bindir}/text-extractor-ocr

# Compile GSettings schemas if present
if [ -d %{buildroot}%{extdir}/schemas ]; then
    glib-compile-schemas %{buildroot}%{extdir}/schemas
fi

%files
%license LICENSE
%doc README.md
%{extdir}
%{_bindir}/text-extractor-ocr

%changelog
* Mon Jun 29 2026 Bahram Farahmand <bahram.0098.bf@gmail.com> - 1.1.0-1
- Initial Fedora package
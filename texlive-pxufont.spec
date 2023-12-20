Name:		texlive-pxufont
Version:	67573
Release:	1
Summary:	Emulate non-Unicode Japanese fonts using Unicode fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pxufont
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxufont.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxufont.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The set of the Japanese logical fonts (JFMs) that are used as
standard fonts in pTeX and upTeX contains both Unicode JFMs and
non-Unicode JFMs. This bundle provides an alternative set of
non-Unicode JFMs that are tied to the virtual fonts (VFs) that
refer to the glyphs in the Unicode JFMs. Moreover it provides a
LaTeX package that redefines the NFSS settings of the Japanese
fonts of (u)pLaTeX so that the new set of non-Unicode JFMs will
be employed. As a whole, this bundle allows users to dispense
with the mapping setup on non-Unicode JFMs. Such a setup is
useful in particular when users want to use OpenType fonts
(such as Source Han Serif) that have a glyph encoding different
from Adobe-Japan1, because mapping setups from non-Unicode JFMs
to such physical fonts are difficult to prepare.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pxufont
%{_texmfdistdir}/fonts/vf/public/pxufont
%{_texmfdistdir}/fonts/tfm/public/pxufont
%doc %{_texmfdistdir}/doc/latex/pxufont

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

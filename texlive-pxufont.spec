%global tl_name pxufont
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7
Release:	%{tl_revision}.1
Summary:	Emulate non-Unicode Japanese fonts using Unicode fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/jptex/latex/pxufont
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pxufont.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pxufont.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The set of the Japanese logical fonts (JFMs) that are used as standard
fonts in pTeX and upTeX contains both Unicode JFMs and non-Unicode JFMs.
This bundle provides an alternative set of non-Unicode JFMs that are
tied to the virtual fonts (VFs) that refer to the glyphs in the Unicode
JFMs. Moreover it provides a LaTeX package that redefines the NFSS
settings of the Japanese fonts of (u)pLaTeX so that the new set of non-
Unicode JFMs will be employed. As a whole, this bundle allows users to
dispense with the mapping setup on non-Unicode JFMs. Such a setup is
useful in particular when users want to use OpenType fonts (such as
Source Han Serif) that have a glyph encoding different from Adobe-
Japan1, because mapping setups from non-Unicode JFMs to such physical
fonts are difficult to prepare.


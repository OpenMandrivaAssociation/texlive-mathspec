%global tl_name mathspec
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2b
Release:	%{tl_revision}.1
Summary:	Specify arbitrary fonts for mathematics in XeTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/mathspec
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathspec.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathspec.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The mathspec package provides an interface to typeset mathematics in
XeLaTeX with arbitrary text fonts using fontspec as a backend. The
package is under development and later versions might to be incompatible
with this version, as this version is incompatible with earlier
versions. The package requires at least version 0.9995 of XeTeX.


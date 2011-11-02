Name:		texlive-mathspec
Version:	0.2
Release:	1
Summary:	Specify arbitrary fonts for mathematics in XeTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/latex/mathspec
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathspec.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathspec.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The mathspec package provides an interface to typeset
mathematics in XeLaTeX with arbitrary text fonts using fontspec
as a backend. The package is under development and later
versions might to be incompatible with this version, as this
version is incompatible with earlier versions. The package
requires at least version 0.9995 of XeTeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xelatex/mathspec/mathspec.sty
%doc %{_texmfdistdir}/doc/xelatex/mathspec/README
%doc %{_texmfdistdir}/doc/xelatex/mathspec/mathspec.pdf
%doc %{_texmfdistdir}/doc/xelatex/mathspec/mathspec.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

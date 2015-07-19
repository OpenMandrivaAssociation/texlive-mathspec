# revision 15878
# category Package
# catalog-ctan /macros/xetex/latex/mathspec
# catalog-date 2009-09-30 20:39:21 +0200
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-mathspec
Version:	0.2
Release:	10
Summary:	Specify arbitrary fonts for mathematics in XeTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/latex/mathspec
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathspec.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathspec.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The mathspec package provides an interface to typeset
mathematics in XeLaTeX with arbitrary text fonts using fontspec
as a backend. The package is under development and later
versions might to be incompatible with this version, as this
version is incompatible with earlier versions. The package
requires at least version 0.9995 of XeTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 753780
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 718975
- texlive-mathspec
- texlive-mathspec
- texlive-mathspec
- texlive-mathspec


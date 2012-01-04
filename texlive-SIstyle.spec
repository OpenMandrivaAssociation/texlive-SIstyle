# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/SIstyle
# catalog-date 2008-07-16 16:54:56 +0200
# catalog-license lppl
# catalog-version 2.3a
Name:		texlive-SIstyle
Version:	2.3a
Release:	2
Summary:	Package to typeset SI units, numbers and angles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/SIstyle
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/SIstyle.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/SIstyle.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/SIstyle.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package typesets SI units, numbers and angles according to
the ISO requirements. Care is taken with font setup and
requirements, and language customisation is available. Note
that this package is (in principle) superseded by siunitx;
sistyle has maintenance-only support, now.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/SIstyle/sistyle.sty
%doc %{_texmfdistdir}/doc/latex/SIstyle/README
%doc %{_texmfdistdir}/doc/latex/SIstyle/SIstyle-2.3a.pdf
%doc %{_texmfdistdir}/doc/latex/SIstyle/fig1.eps
%doc %{_texmfdistdir}/doc/latex/SIstyle/fig1.mps
%doc %{_texmfdistdir}/doc/latex/SIstyle/fig2.eps
%doc %{_texmfdistdir}/doc/latex/SIstyle/fig2.mps
%doc %{_texmfdistdir}/doc/latex/SIstyle/graphs_scr.zip
#- source
%doc %{_texmfdistdir}/source/latex/SIstyle/sistyle.dtx
%doc %{_texmfdistdir}/source/latex/SIstyle/sistyle.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

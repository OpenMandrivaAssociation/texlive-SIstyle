Name:		texlive-SIstyle
Version:	59682
Release:	2
Summary:	Package to typeset SI units, numbers and angles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/SIstyle
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sistyle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sistyle.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sistyle.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/sistyle
%doc %{_texmfdistdir}/doc/latex/sistyle
#- source
%doc %{_texmfdistdir}/source/latex/sistyle

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

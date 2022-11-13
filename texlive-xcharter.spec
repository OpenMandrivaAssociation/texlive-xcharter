Name:		texlive-xcharter
Version:	63057
Release:	1
Summary:	Extension of Bitstream Charter fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/xcharter
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcharter.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcharter.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package presents an extension of Bitstream Charter, which
provides small caps, oldstyle figures and superior figures in
all four styles, accompanied by LaTeX font support files. The
fonts themselves are provided in both Adobe Type 1 and OTF
formats, with supporting files as necessary.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/*/*/xcharter
%{_texmfdistdir}/tex/latex/xcharter
%doc %{_texmfdistdir}/doc/fonts/xcharter

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}

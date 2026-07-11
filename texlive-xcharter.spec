%global tl_name xcharter
%global tl_revision 78931

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.26
Release:	%{tl_revision}.1
Summary:	Extension of Bitstream Charter fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/xcharter
License:	other-free lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xcharter.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xcharter.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package presents an extension of Bitstream Charter, which provides
small caps, oldstyle figures and superior figures in all four styles,
accompanied by LaTeX font support files. The fonts themselves are
provided in both Adobe Type 1 and OTF formats, with supporting files as
necessary.


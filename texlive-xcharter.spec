# revision 32055
# category Package
# catalog-ctan /fonts/xcharter
# catalog-date 2013-11-03 10:05:42 +0100
# catalog-license other-free
# catalog-version 1.00
Name:		texlive-xcharter
Version:	1.00
Release:	2
Summary:	Extension of Bitstream Charter fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/xcharter
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcharter.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcharter.doc.tar.xz
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
%{_texmfdistdir}/fonts/enc/dvips/xcharter/XCh_2bziiw.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/XCh_57c.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/XCh_57c3kj.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/XCh_774.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/XCh_774cbp.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/XCh_7xsilo.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/XCh_7ya.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/XCh_7yasjx.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/XCh_gev.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/XCh_gev73z.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/XCh_kaakcj.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/XCh_mbz2ag.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/XCh_nhq.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/XCh_nhqiuu.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/XCh_o3e.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/XCh_o3eiyz.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/XCh_rqpru4.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/XCh_rvnb4v.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/XCh_tsbasn.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/XCh_ttrny6.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/XCh_x4fzx5.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/XCh_xeu7sg.enc
%{_texmfdistdir}/fonts/map/dvips/xcharter/XCharter.map
%{_texmfdistdir}/fonts/opentype/public/xcharter/XCharter-Bold.otf
%{_texmfdistdir}/fonts/opentype/public/xcharter/XCharter-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/public/xcharter/XCharter-Italic.otf
%{_texmfdistdir}/fonts/opentype/public/xcharter/XCharter-Roman.otf
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-osfx-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-osfx-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-osfx-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-osfx-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-osfx-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-osfx-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-osfx-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-osfx-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-osfx-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-osfx-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-osfx-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-osfx-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-osfx-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-osfx-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-osfx-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-osfx-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-osfx-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-osfx-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-osfx-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-osfx-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-osfx-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-osfx-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-osfx-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-osfx-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-osfx-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-osfx-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-osfx-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-osfx-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-osfx-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-osfx-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-osfx-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-osfx-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-tlf-ts1.tfm
%{_texmfdistdir}/fonts/type1/public/xcharter/XCharter-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/xcharter/XCharter-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/public/xcharter/XCharter-Italic.pfb
%{_texmfdistdir}/fonts/type1/public/xcharter/XCharter-Roman.pfb
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-osfx-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-osfx-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-osfx-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-osfx-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-osfx-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-osfx-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-osfx-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-osfx-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-osfx-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-osfx-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-osfx-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-osfx-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-osfx-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-osfx-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-osfx-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-osfx-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-tosf-ly1.vf
%{_texmfdistdir}/tex/latex/xcharter/LY1XCharter-OsF.fd
%{_texmfdistdir}/tex/latex/xcharter/LY1XCharter-Sup.fd
%{_texmfdistdir}/tex/latex/xcharter/LY1XCharter-TLF.fd
%{_texmfdistdir}/tex/latex/xcharter/T1XCharter-OsF.fd
%{_texmfdistdir}/tex/latex/xcharter/T1XCharter-Sup.fd
%{_texmfdistdir}/tex/latex/xcharter/T1XCharter-TLF.fd
%{_texmfdistdir}/tex/latex/xcharter/TS1XCharter-OsF.fd
%{_texmfdistdir}/tex/latex/xcharter/TS1XCharter-TLF.fd
%{_texmfdistdir}/tex/latex/xcharter/XCharter.sty
%doc %{_texmfdistdir}/doc/fonts/xcharter/README
%doc %{_texmfdistdir}/doc/fonts/xcharter/xcharter-doc.pdf
%doc %{_texmfdistdir}/doc/fonts/xcharter/xcharter-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}

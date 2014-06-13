# revision 32717
# category Package
# catalog-ctan /fonts/xcharter
# catalog-date 2014-01-18 22:02:45 +0100
# catalog-license other-free
# catalog-version 1.02
Name:		texlive-xcharter
Version:	1.02
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
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_2bziiw.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_57c3kj.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_774cbp.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_7xsilo.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_7yasjx.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_c7a5t5.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_gev73z.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_ghsr6w.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_gjy6pd.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_gvpfwf.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_hrugnt.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_ic35ro.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_kaakcj.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_kn5oqz.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_mbz2ag.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_mgl6fo.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_nhqiuu.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_o3eiyz.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_ptibkq.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_rqpru4.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_rvnb4v.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_tsbasn.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_ttrny6.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_uggo2i.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_x4fzx5.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_xeu7sg.enc
%{_texmfdistdir}/fonts/enc/dvips/xcharter/xch_z56e5d.enc
%{_texmfdistdir}/fonts/map/dvips/xcharter/XCharter.map
%{_texmfdistdir}/fonts/opentype/public/xcharter/XCharter-Bold.otf
%{_texmfdistdir}/fonts/opentype/public/xcharter/XCharter-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/public/xcharter/XCharter-Italic.otf
%{_texmfdistdir}/fonts/opentype/public/xcharter/XCharter-Roman.otf
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
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Bold-tosf-ts1.tfm
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
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-BoldItalic-tosf-ts1.tfm
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
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Italic-tosf-ts1.tfm
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
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter-Roman-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-Bold-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-Bold-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-Bold-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-Bold-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-Bold-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-Bold-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-Bold-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-Bold-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-BoldItalic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-BoldItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-BoldItalic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-BoldItalic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-BoldItalic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-BoldItalic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-BoldItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-BoldItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-Italic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-Italic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-Italic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-Italic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-Italic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-Italic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-Italic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-Italic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-Roman-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-Roman-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-Roman-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-Roman-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-Roman-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-Roman-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-Roman-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/xcharter/XCharter1-Roman-tosf-t1.tfm
%{_texmfdistdir}/fonts/type1/public/xcharter/XCharter-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/xcharter/XCharter-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/public/xcharter/XCharter-Italic.pfb
%{_texmfdistdir}/fonts/type1/public/xcharter/XCharter-Roman.pfb
%{_texmfdistdir}/fonts/type1/public/xcharter/XCharter1-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/xcharter/XCharter1-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/public/xcharter/XCharter1-Italic.pfb
%{_texmfdistdir}/fonts/type1/public/xcharter/XCharter1-Roman.pfb
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Bold-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-BoldItalic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Italic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter-Roman-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter1-Bold-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter1-Bold-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter1-Bold-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter1-Bold-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter1-BoldItalic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter1-BoldItalic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter1-BoldItalic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter1-BoldItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter1-Italic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter1-Italic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter1-Italic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter1-Italic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter1-Roman-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter1-Roman-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter1-Roman-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/xcharter/XCharter1-Roman-tosf-t1.vf
%{_texmfdistdir}/tex/latex/xcharter/LY1XCharter-Sup.fd
%{_texmfdistdir}/tex/latex/xcharter/LY1XCharter-TLF.fd
%{_texmfdistdir}/tex/latex/xcharter/LY1XCharter-TOsF.fd
%{_texmfdistdir}/tex/latex/xcharter/T1XCharter-Sup.fd
%{_texmfdistdir}/tex/latex/xcharter/T1XCharter-TLF.fd
%{_texmfdistdir}/tex/latex/xcharter/T1XCharter-TOsF.fd
%{_texmfdistdir}/tex/latex/xcharter/TS1XCharter-TLF.fd
%{_texmfdistdir}/tex/latex/xcharter/TS1XCharter-TOsF.fd
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

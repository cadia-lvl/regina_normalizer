period_ptrn = r"\b(mán(ud)?|þri(ðjud)?|miðvikud|fim(mtud)?|fös(tud)?|lau(gard)|sun(nud)|jan|feb|mar|apr|jú[nl]|ágú?|sept?|okt|nóv|des)\.?|\b(I(II?|V|X)|(V|X|XV)I{1,3}|XI?[VX])\b"
                         
def make_period_dict():
    period_dict = {"(\W|^)mán(ud)?\.?(\W|$)": "\g<1>mánudag\g<3>",
                    "(\W|^)þri(ðjud)?\.?(\W|$)": "\g<1>þriðjudag\g<3>",
                    "(\W|^)miðvikud\.?(\W|$)": "\g<1>miðvikudag\g<2>",
                    "(\W|^)fim(mtud)?\.?(\W|$)": "\g<1>fimmtudag\g<3>",
                    "(\W|^)fös(tud)?\.?(\W|$)": "\g<1>föstudag\g<3>",
                    "(\W|^)lau(gard)?\.?(\W|$)": "\g<1>laugardag\g<3>",
                    "(\W|^)sun(nud)?\.?(\W|$)": "\g<1>sunnudag\g<3>",

                    "(\W|^)jan\.?(\W|$)": "\g<1>janúar\g<2>",
                    "(\W|^)feb\.?(\W|$)": "\g<1>febrúar\g<2>",
                    "(\W|^)mar\.?(\W|$)": "\g<1>mars\g<2>",
                    "(\W|^)apr\.?(\W|$)": "\g<1>apríl\g<2>",
                    "(\W|^)jún\.?(\W|$)": "\g<1>júní\g<2>",
                    "(\W|^)júl\.?(\W|$)": "\g<1>júlí\g<2>",
                    "(\W|^)ágú?\.?(\W|$)": "\g<1>ágúst\g<2>",
                    "(\W|^)sept?\.?(\W|$)": "\g<1>september\g<2>",
                    "(\W|^)okt\.?(\W|$)": "\g<1>október\g<2>",
                    "(\W|^)nóv\.?(\W|$)": "\g<1>nóvember\g<2>",
                    "(\W|^)des\.?(\W|$)": "\g<1>desember\g<2>",

                    "(\W|^)II\.?(\W|$)": "\g<1>annar\g<2>",
                    "(\W|^)III\.?(\W|$)": "\g<1>þriðji\g<2>",
                    "(\W|^)IV\.?(\W|$)": "\g<1>fjórði\g<2>",
                    "(\W|^)VI\.?(\W|$)": "\g<1>sjötti\g<2>",
                    "(\W|^)VII\.?(\W|$)": "\g<1>sjöundi\g<2>",
                    "(\W|^)VIII\.?(\W|$)": "\g<1>áttundi\g<2>",
                    "(\W|^)IX\.?(\W|$)": "\g<1>níundi\g<2>",
                    "(\W|^)XI\.?(\W|$)": "\g<1>ellefti\g<2>",
                    "(\W|^)XII\.?(\W|$)": "\g<1>tólfti\g<2>",
                    "(\W|^)XIII\.?(\W|$)": "\g<1>þrettándi\g<2>",
                    "(\W|^)XIV\.?(\W|$)": "\g<1>fjórtándi\g<2>",
                    "(\W|^)XV\.?(\W|$)": "\g<1>fimmtándi\g<2>",
                    "(\W|^)XVI\.?(\W|$)": "\g<1>sextándi\g<2>",
                    "(\W|^)XVII\.?(\W|$)": "\g<1>sautjándi\g<2>",
                    "(\W|^)XVIII\.?(\W|$)": "\g<1>átjándi\g<2>",
                    "(\W|^)XIX\.?(\W|$)": "\g<1>nítjándi\g<2>"}
    
    return period_dict
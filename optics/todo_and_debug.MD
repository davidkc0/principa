todo

1. export notebooks as PDF, for easy latex. I installed mactex for the xdf. But im getting

https://github.com/LaTeX-Package-Repositories/ucs/issues/2

Package ucs Warning: ucs package ignored with utf8 based engines.

)

! LaTeX Error: Unknown option `mathletters' for package `ucs'.

See the LaTeX manual or LaTeX Companion for explanation.
Type  H <return>  for immediate help.
 ...                                              

l.41     \usepackage
                    {fancyvrb} % verbatim replacement that allows latex
?
! Emergency stop.
 ...                                              

l.41     \usepackage
                    {fancyvrb} % verbatim replacement that allows latex
No pages of output.
Transcript written on notebook.log.


2. Compile the optics.tex again. It broke sometime after I tried to include the url, and the quote. I havent been able to fiure it out.



500 : Internal Server Error

The error was:

nbconvert failed: PDF creating failed, captured latex output:
Failed to run "['xelatex', 'notebook.tex', '-quiet']" command:
This is XeTeX, Version 3.141592653-2.6-0.999996 (TeX Live 2024) (preloaded format=xelatex)
 restricted \write18 enabled.
entering extended mode
(./notebook.tex
LaTeX2e <2023-11-01> patch level 1
L3 programming layer <2024-02-20>
(/usr/local/texlive/2024/texmf-dist/tex/latex/base/article.cls
Document Class: article 2023/05/17 v1.4n Standard LaTeX document class
(/usr/local/texlive/2024/texmf-dist/tex/latex/base/size11.clo))
(/usr/local/texlive/2024/texmf-dist/tex/latex/tcolorbox/tcolorbox.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/pgf/basiclayer/pgf.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/pgf/utilities/pgfrcs.sty
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/utilities/pgfutil-common.te
x)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/utilities/pgfutil-latex.def
) (/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/utilities/pgfrcs.code.tex
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/pgf.revision.tex)))
(/usr/local/texlive/2024/texmf-dist/tex/latex/pgf/basiclayer/pgfcore.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/local/texlive/2024/texmf-dist/tex/latex/graphics-def/xetex.def)))
(/usr/local/texlive/2024/texmf-dist/tex/latex/pgf/systemlayer/pgfsys.sty
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/systemlayer/pgfsys.code.tex
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/utilities/pgfkeys.code.tex
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/utilities/pgfkeyslibraryfil
tered.code.tex))
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/systemlayer/pgf.cfg)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-xetex.de
f
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-dvipdfmx
.def
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-common-p
df.def))))
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/systemlayer/pgfsyssoftpath.
code.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/systemlayer/pgfsysprotocol.
code.tex)) (/usr/local/texlive/2024/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/local/texlive/2024/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/basiclayer/pgfcore.code.tex
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/math/pgfmath.code.tex
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/math/pgfmathutil.code.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/math/pgfmathparser.code.tex
)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.code.
tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.basic
.code.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.trigo
nometric.code.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.rando
m.code.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.compa
rison.code.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.base.
code.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.round
.code.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.misc.
code.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.integ
erarithmetics.code.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/math/pgfmathcalc.code.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/math/pgfmathfloat.code.tex)
) (/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/math/pgfint.code.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepoints.co
de.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepathconst
ruct.code.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepathusage
.code.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/basiclayer/pgfcorescopes.co
de.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/basiclayer/pgfcoregraphicst
ate.code.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/basiclayer/pgfcoretransform
ations.code.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/basiclayer/pgfcorequick.cod
e.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreobjects.c
ode.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepathproce
ssing.code.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/basiclayer/pgfcorearrows.co
de.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreshade.cod
e.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreimage.cod
e.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreexternal.
code.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/basiclayer/pgfcorelayers.co
de.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/basiclayer/pgfcoretranspare
ncy.code.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepatterns.
code.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/basiclayer/pgfcorerdf.code.
tex)))
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/modules/pgfmoduleshapes.cod
e.tex)
(/usr/local/texlive/2024/texmf-dist/tex/generic/pgf/modules/pgfmoduleplot.code.
tex)
(/usr/local/texlive/2024/texmf-dist/tex/latex/pgf/compatibility/pgfcomp-version
-0-65.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/pgf/compatibility/pgfcomp-version
-1-18.sty)) (/usr/local/texlive/2024/texmf-dist/tex/latex/tools/verbatim.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/environ/environ.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/trimspaces/trimspaces.sty))
(/usr/local/texlive/2024/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/tcolorbox/tcbbreakable.code.tex
Library (tcolorbox): 'tcbbreakable.code.tex' version '6.2.0'
(/usr/local/texlive/2024/texmf-dist/tex/latex/pdfcol/pdfcol.sty
(/usr/local/texlive/2024/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)
(/usr/local/texlive/2024/texmf-dist/tex/generic/infwarerr/infwarerr.sty)
(/usr/local/texlive/2024/texmf-dist/tex/generic/iftex/iftex.sty))))
(/usr/local/texlive/2024/texmf-dist/tex/latex/parskip/parskip.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/kvoptions/kvoptions.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)))
(/usr/local/texlive/2024/texmf-dist/tex/latex/fontspec/fontspec.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/l3packages/xparse/xparse.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/l3kernel/expl3.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/l3backend/l3backend-xetex.def)))
(/usr/local/texlive/2024/texmf-dist/tex/latex/fontspec/fontspec-xetex.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/base/fontenc.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/fontspec/fontspec.cfg)))
(/usr/local/texlive/2024/texmf-dist/tex/latex/caption/caption.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/local/texlive/2024/texmf-dist/tex/latex/float/float.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/tools/enumerate.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/local/texlive/2024/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/local/texlive/2024/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/local/texlive/2024/texmf-dist/tex/latex/base/textcomp.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/upquote/upquote.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/eurosym/eurosym.sty)
(/usr/local/texlive/2024/texmf-dist/tex/latex/ucs/ucs.sty

Package ucs Warning: ucs package ignored with utf8 based engines.

)

! LaTeX Error: Unknown option `mathletters' for package `ucs'.

See the LaTeX manual or LaTeX Companion for explanation.
Type  H <return>  for immediate help.
 ...                                              

l.41     \usepackage
                    {fancyvrb} % verbatim replacement that allows latex
?
! Emergency stop.
 ...                                              

l.41     \usepackage
                    {fancyvrb} % verbatim replacement that allows latex
No pages of output.
Transcript written on notebook.log.


3. Have Chatgpt right out the answers
4. Give out my old interference reference papers from my backlog of notes.


4. Add a section on calculus, and things like simple functions, and something like a uniform coverage theorem or LDCT. dominated convergences theorem.
5. Talk about soap bubbles, and thin film interference

For 4. I am getting

gnb@Geoffreys-MacBook-Pro-2 principa-master-localcomp % cd optics
gnb@Geoffreys-MacBook-Pro-2 optics % pdftex lbc.tex              
This is pdfTeX, Version 3.141592653-2.6-1.40.26 (TeX Live 2024) (preloaded format=pdftex)
 restricted \write18 enabled.
entering extended mode
! I can't find file `lbc.tex'.
<*> lbc.tex

(Press Enter to retry, or Control-D to exit)
Please type another input file name: lbdc.tex
(./lbdc.tex
! Undefined control sequence.
l.1 \section
            *{The Lebesgue Dominated Convergence Theorem: A High-Level Overv...

?
! Undefined control sequence.
l.4 ...T states that if a sequence of functions \(
                                                  f_n\) converges pointwise ...

?
! Missing $ inserted.
<inserted text>
                $
<to be read again>

I looked at it in nano, and the characters don't seem weird. Hmmmm.....

entering extended mode
(./lbdc.tex
LaTeX2e <2023-11-01> patch level 1
L3 programming layer <2024-02-20>
./lbdc.tex:1: Undefined control sequence.
l.1 \section
            *{The Lebesgue Dominated Convergence Theorem: A High-Level Overv...

? h
The control sequence at the end of the top line
of your error message was never \def'ed. If you have
misspelled it (e.g., `\hobx'), type `I' and the correct
spelling (e.g., `I\hbox'). Otherwise just continue,
and I'll forget about whatever was undefined.

?
Process aborted

Process aborted

The problem is in the package loads???
Huh, so I added the \docclass, and it works. Then I tried again with PDF Latex on the optics, and it worked. Will comit everything to git now. 

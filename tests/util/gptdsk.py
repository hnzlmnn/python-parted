import base64
import bz2

disk_data=(
    'LRx4!F+o`-Q&}^%Mdbh!K7arJ|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBsDtK9zJF'
    '|rz-uM9^02B(UK>B&-%iDF)+b?&ox)ntNfGP@#6%RhP-+bci$7@R=0;AVnz0ZT>C<*~oR0$8'
    'SJs($D-seel=WT7VR@&A|r3PzhZL<*+(G5YA#+ft;gG6S8^Z*HpdT79!X{M>-dTEsOX{Hp~F'
    'ouB1lLDJeCKCk6(<21PV1cHLCL>KUVKmBmG}9(SCLm&IJy3{{OiAd-13*tgFpQppo}QBv35_'
    '(;o&lm@0%@iKo|rW-Mwln5F`|B>RQ#DwLnc#Aqa#f;$iYm>h|^4|v86m|Jrl_^$>`KGKx%|d'
    '2quKWWYb2cs(ChpN$RKhDtjsD^-mI>!7^%3YM-G`Pft;%CaLXBN9i%@r|O@ksl82-n_^_Au}'
    '!LZs(z{Zo~G3G9;by*O{p~fLF$`iGDFfbX{qL^`ce8*(<UPm)gGRx(c)=8N@x;lh=7_2f}TN'
    '7(KA%Xr9DTK^*yPPq|?;(GI~?=HAZby^-ZROGNI}XJwr^<>X{laLqYnZWj!?0N$O#vL~S)PJ'
    'p)ZlPe6^RWc4&?JpyN`Jq&^jJwVe@O-Y`LGMX`orl+XdBNNkVhnhx>N2K<t=|5EUKUBo>X{h'
    'u=YHw8ZBh);nrkYJNNYK&kPgHs|)bwg-Vh_~@A)b`e)PA7R4F{CK(rr&ddO&E}XbI^wU=XPw'
    'Oh6`rH9UfPr<#%AO$|*wCXZ81JqQ^z-l)?+8UsKw00E%H#0G|%Xk-SOXf%3&4FCp!GBh*+ko'
    '17a(@hF59;^xZHLykt#ib+|kpTrywVV?Hz{B880~}3onZ0AHF#>Tk@KHg~l6%?3Fa=1YEW{P'
    '-in)^2{A2*hdSYeom6(b&VpA{~fmR~UAjrxTfUyFij5J4CSBTnyZ>+6gKrJ#b(SwG{6;+1oc'
    'TF2swscl1+!<J~9nTe}2J_7NPxSEn7wX(b7F|D9d7L^v%x|R^7|~@cRw1aYG`LfKm$6<fWCw'
    'G}7EV?}Szzmm-XSE8Xq6Msr`N?6145&JhanwtYtG4ZpiCEIAIZStI7Mw%O}a|ZjZs8w{A@{6'
    'wh1w*Il9_bo>>j?7OtvbzA_{T5e)CAw!{M341S9hUJCbK?k)R=&r^3383U`7K+KjGOFwZN4{'
    '_ASHn#?(%BSJtpPP)!^cHuT`QGTQcu*ibr&+q*SXL~M*6{BGcG6q%NnWh?IbB@mc2q4Wx}Wo'
    '7#$=ClppD*Sp}@i*0zXvW;XL&u{3n*~KB<OnbjR}l+wNl~4%7wW0wTSQslfMiKc2_9iR$rGJ'
    '-MI$3xy-`F(4wcZ6xsT=(IkWJ6;EqLwP^1)qT!cFQR3e^R9PgUHX)=?hX}_$>uw6bnnnG2uz'
    'C`E3y`!;1Qj!AA4B-0hK>mC?!I<ThHXs<g8>tKsLmxTK>oAYab6DW&8B|wa{~$b_tB@g@8MP'
    'ow=PV-NQEo<tYrv>y=fx^<U8L+|0-Le+@@!W0xp8dFV9s@E!H+C69Y87TcZX#oT(jbO{iDhl'
    'EPQlsziVTucASxt29mI3i?}NZ}0_0uajx{^=rR)wwC$bm7SU56!H`yv!_=N*)cB|JSGE(ER3'
    'G#G%*z#V`V4Rv-*co?;1YQV)dw7%E-2o`Tb8oc3{b@1Bqe(G!SG;oyx-hRds*^pt9>TgM*1J'
    '!K`|jB&z}Hg{%i(@hCl@*re|#zmY)`%NRDzP4=T1&3UZAf<$tVn3>Ufd~NTgH3F=JSA9`GVu'
    'BXk{YCDzMuGsm;(eW?r(QfbYt{sYoo%;a^-jXGc4$KVgTU`JP7&H#ZtWwMK9Ma)y^xj#<orX'
    'Ys&vJHG2w$*ojR|W<nT7S(Lo(Uj_ft^JK#XXtCDeS$Orzxf3hh=#>n}#n}~w>!Z-LBsr~?X~'
    '5(qs5}CFYgj4Nsj8F0fxnd?DFzZMWJ{U#y$A#-`B-JG{e@ABwPTK>v$#4)1fMqQN~1`C7{v~'
    'uhDZPsj7<ai%~euE6a?5AG&o70*PJ_;Sl32gKY!8&dpr8oCNA#7Xh0o{u+k_Pseg2am<!vr2'
    '@Zfy2w@|R01P=d96TAbj8&Vap7~QZ)RV7WNex=N>QCu1MkgdVTgKCSBPzHRT!}8~8lv#km<E'
    'tCaQf=*YS`N5X3XLLG!^sSgQ;c`N+olpmy%X;J*ly|){qw*6wqz317W*h^)Yq6>|#yoqWgMt'
    'zH(p{qYzj`k=@`&DrZJ}Ai6c`T*qohX%>BY8LH&5A&+XZ0-P8$jHtu`Krs^-f%ISiEy(_uQU'
    'RblI+{NkO@KH0+h_P`7kJ&2HGOlRA2z~fiXu25OB4i)cYt9!@@*pBF>$*WGg4tXJ}ZJgEuO@'
    'Jmpc@YWP<5Ml#viEfPqkv#u#CZ${qXh*g(_M(da*t-zt#k)2+v(4?M%lAu9R@A&6o|fb@_YS'
    '2F*-cug_~sD*xB6I(<S`@DyeheTo?YY&^95X7PHa=Y^I$Y+BR<p5@bDFgZCbU^)t8skX`Kqm'
    '}7E<o1-rUSLc6zWL%`Anez<GV;oO_HW!1gE!yW-wzcDC&a}8TZTvQa#2oxn{bJ|I#_-4SGA1'
    'PGrvpxi#~SXS`!E=43h0dTVw7|ENqu6G7~5oV$Nt2B~?|<Gc11H#OiMRD+2RHzDd}PhA1+AY'
    'Mp1=ob)kAs%e6eFMb`p2}0_;RDIqWnPScZXZ?6%a<r<A&C5#F&ZuEV^`5Tq>#DG(<-zIGiZk'
    'vwI8cyz1CYxQ{BDGA>A`WU}{u6K88hMp5vkT`P3k6*Vxiu$)qoOeyatLlSPBzWH)3+gff73z'
    '?!5-JR*JE3%wwxX$YQn0W{iig%3R_VqFj%G9i?dqplvlP(5UaR~|ZE>JT}S2MmeBB7C%)@+-'
    'C#H>DKI%wQ1ht@uUHDhay-&xOqfx$SX*+=PF|Kn&!H8}bJCqreWGm_szE>p9rgPbBG*kxq=J'
    '$TE~%@B^w&8#E43xu6aCT(jmiW&=hskp@x?DjMW-$|uoTp&an5_H&epsyATICTRiLn+iTw6G'
    'R|Tf#CFD1=>hzx9t{Lye?YqYz}$gfz!W$2Pk#J)y|1d+EmR52SN_!M{*NfA*NTYfH$CdI{bH'
    'X8Ayi6r0Su>fzOfC393*vz@}(a{76tba=Wkw*c9hN8zEO@E1txF?m~wIAR6RTp9peE`nRTmG'
    'K}!*gxe^3DF@C#8K7(0LSjYbzz6O^c^urT$Q-jFm4=dR8Qd_@WSsssbz`@6YGtxo-~Vjdis_'
    'TwCE<`d>0Yur5v<0Xl{D(Y=aAo*9@h@Cbi(e!WjRaZV-kfvP8Up@k(3y>;nOL-E6b400B>2~'
    'cO*9_)WL~N@E!wB0Iy>SvRV(AkTl9}MvFddApfVj;CN-z4#+>Q42ca|u)EmJkoLI38ACzs@O'
    'ha`&^baH<=vNx9dP#0J}=N<?-?|h8}z`+-{5NUeDB-42`@0=q?w2rXhQ+mSb5O*QV%XuOfN1'
    '&RB}f;U%7)kowSh9NNiaHIh)it2uXd$VaLTt9&ww54#_s>z=xoh%0T9k%^{8q0kTJA@j{*wN'
    '}*x_W3^8dh37-m`|6jU*JjbU_O3G|(n$=3GLZO-dQI3v>F<8J7ZirsX)!6&(}#?lL+xXVLn~'
    'ISKTX&0WoW=05VT@YKWbkmV>nw<ZM+R}TwX1_IBX57ObAR!VPFaYrovA7hp0jy;@@X*nD385'
    ';&tEENw(C^tmLyPnh3p8WucePQgZ1qc30{}+#xqf4`UF*{ANI?*}&^7&?l)t(nw`6?>$z#%N'
    'AqZ+3j=7y*=KY3Z&b(mr8+_$Y`Kg%q`zI(1zWHn+#vu!GXSE$8Gt^!%2Yyu-{*-yXI^88J%B'
    'Q=DeT9?C;?-T+QV-2Y;7c!W;b>2c<(+Bq!J;2>eU;`Wf0Pg!KL$=mS9^3L&o$Y2&Lk-fZLbp'
    'Adu52~clCrq9^+N8QwiRd#dFJcmPqlX#nEPG|l;7OkBF>fEa-<6j4ZP0|-Snsim_>;I1PS2D'
    'WJVuq3z(@mYv2823W)V<GiRVQeNGO|!J*pPJ2zb~GylT%xYhW&K7D%;vuAL1g~;4;FP$3fLG'
    '8qM+|Bn??dWiRGjf!Yu?gdSGs#Aq%{Q^{0{#a$-{k?j0>Bnfu;Ht*srwGsdkX_^%8RJeXiDD'
    ')>&As0CN0IoxJD!P^3FSP`^IHPhnycP+gKrng);6ynRx%uWS%^^$%55s2n$2a}#e9OL4!LJC'
    '^Uj_DB-hDz5%j*V~QpJ4<5x;K9Q^$9bucbro+z^H&jPm6HCjT6&hTc%IFx4%z<W0a8j5AYW<'
    'WYnBrCRkA1#NKw9AJyH{5z%u1w}YJL5d0K(2xf$RDmM+k(Vk(NrVJ|DdOg#F*`PSv);|8$7<'
    '1R^w!AR2B#r|sXH=z{QBc_0<Gn7IKg=7YbYGl=r3!Q_ieQjl2@x~Yl#)<*0?p?_?2dma8j7p'
    '<=|YVazIl3NgzT}45*MO1RMA*J9$&l5Y=APYi+~)-E-tZk;gsX&XlT{dz>NaFfSGQ1*PXz4$'
    '%x@2`XOR3Lu#ba(_b>D(sF@l&Tb{RY_h$I88U1e@r5cBol1W^sZ_7eL@0y$Oa4O+=b@TUp&}'
    '|Hj^b<H~4GV7#GOC9=Y^`GnEW>v<@gV)4SJ{9;Vf*a){3DYQJtv2tSiETR6A`3DN;5NVs^gv'
    'LTX$v4y(i;=sh(^{`%f|Bdt{IiI=s!{QWSiSCxI)3w@%{`FjG^dW&kOpH&Bvvs$i*VJm``ff'
    '~4BUwJd?uX`DmN#pOqC;gV8x2sfF;FN7HxhzkPn73jCOKcBSAIL9B?b*30;q-saSR4T56Crf'
    '+3M^DK^i%#3X9RXB$xZD5|vsr<VHd79a4+0lGgC7K~=GUXeUaXV%7p;i;9La#Yrs)f|4M!N?'
    'b%KQxrRloJ^x(ReAVChoI)pA|Q8@_T&N5S?+qb7M)py5cudS!BBo}-M%Ow<c(Ec+PYe69`+l'
    'F+S>fE`wYmuUd_MViPuuD8}q>rsS89C@mt9mu7bfXSp(L%luawyAlxLsqRc2eJt@wXra;)-s'
    '$+c*i_j2kAml(QY^nJS>=ApwE}F(=ye5$lcjDYL)v-iG38GsU61aN(9JQEj!EW8UCbBO>44A'
    '=eOQkefEz}cDukz3QbQwF9P3t#aWD1|FU+{kSDn4T0(Upu{8bn9mMTzo)=&!IJP9=IvsMR?$'
    '{;FGRzng^eCzuBTx>rNDscqV-n!(*G-tqyft3OS)cgcNP+F?MV{rNOF?N|H<2E<6X;%MOl)o'
    '~04)>6Dm5^6BvvxwdEeSZqVZ(jL3ynQP9B5I}@hq~EVR~m?1;DaP$2X8)^elzl-abN*B*{50'
    '>ATZliHj=cxc?SMrgK3;IPT4Of1qPz3!*6fwS_*A?s|o-n$V|uM7O?%rob69{@L!=^7n&Su$'
    '8{8_eBJAv=~wUKu4619j6ueFaKAWNK1|I|1%jn!Z*_45Ox)ysp)dzx<O{QqMo&#>kb`Opcu_'
    'uv=|Q8!;6v8Hd0$VCbO)=Gx7&{HL(f8ZR5}(zs6a0=2Dvq;1<NP_aSkI35^p^|6y?GjwNkyo'
    '2b_S)3Qm`-!W(3BKs-^Dqvi6&Wjf_DfOk1C7?0@vOd;cEzJ<+a#fFsKkfaZ!w_s>M@Yu#^I#'
    'RhpJJ6VwPnwa$@?!yCks#tV-RJw@mLR>d28DT5CQfZ6u_Ycu14))7$hLvvnW{~aJF;hlplCV'
    'PC$zY0x8aPQ7{s`&q?WLmD6xoSB;NH@GyGx8RH|ek7B`X}N>imP`Y>_a+n*z{SIA4jDn6bB{'
    '+U$QCnO5zg=kd&Y5c46`S=0gm7#f4(Sxd@5=tZvDO?fXr8r^cLiJ)+nC1JH%k1u-GR`{>UWB'
    'dLLv+qYZ46urSnQY#Cy$ykhg6B8P<LQXoGS9*<c08(2U#oga;G*_4z?9Fz$TagDMz@J&jKA7'
    '9&|2vG)mHVDcJyVG9#u?TubrrJQ4%D0qEq@F3CVONTIF)GLbTrU9c}k6)`SoUOZt8MV0{Ikp'
    'pC|sRzM84pJ^@_DD`E33Y%)0@yQIeV`&v6PATg1J^+4klmC|Aqe&G38Egp4hU4+r#?nd6oyh'
    'JxehrMGt0vZ$0DCSCmfpP5cIOCvP5wzhHj1u7mtT~A=5q&EV3FEd_*W4(56I<38E087b!&Gf'
    'DRd4^O{;vIq(j62Z9{ZiHSw@Fea(@8547J1DXs%j>rTxNG56W6No85;Dbb&<$3o7-tOZ>2HA'
    'A>SQR*+KNdSF7d+{KF$x@T4$RmP#0YRp$U;0sA>B@icOZ33xWyE_-C<Tq*)w{9n1N%XS^<3t'
    'V=y(ZsqC`NCj>eP%1c%iFi3V?UKQV$z{l>vj+fXTCwZ4;l1+;VpoS+k0<87P-mtpadX-^y16'
    'smb@pJ90mtAX-n?OFpGZ-57SdtdBVS96avKG2l(16^aOKCu{41}r}QU}38QK}O`HVH4FKJtX'
    'eWH)G2q@WkIlslv*CR|~Xm=YU1v;fXYvu#LWNk$l44r|*k$hvq_Olg-~rdJiBPDxJdrQi9Hm'
    '^Y!*K*ELwKvHu~v4MpN&Tb7WmKbw<t+z9AT?|Z{VK}41&NE>?2K5qoXf#I@>eYaJmb@GA`q('
    'tbLxRJ-G-;E@T*$}6;ny5cz2t$S5a&s?f%!N#NLw&yjG#Lie>&oWR*VLS57vX5OwJtu!kWef'
    '`)F!bgg+IS7#kewY%QP?sCvleLE83MN3yg*%9PnD)11<7!aR_1NEzhq<vdQTcsoo6T5*U@$D'
    '@Evu!mnR*#gmkOh9yCIuLs4P5Io~VGX<)Wc4RRC-F#b$Y+4%Na}-a-Amrv=LQaZKF`qL%@X^'
    'QU2Q<IlBvdL#L1=>2hT%fhl@h<{b*fFv9|A{zua=V;PrPO(fHpxnd~?)9dx_gm|XI8Q{&+9-'
    '+qwP7#uV&GXuW&v<(y`iFL$*<WQa$GY-|C2b;DN69dsb@#75lGS4sDx2gon!AUMXv+26;P2`'
    'IrnLH{7e&?r1hRyyo>)$NNuR|}Z-|p-tf8$dEW1+r4$YfBP-&$b7UlVginAFF|v-j}-t0CH?'
    ')$V*L|4CW)`%iKg4p+b{(0gx9#?O$jUj_RLSSm1z>5umNH99Q3<-p(vAZH|kEF+FimyvHI+&'
    'tSkB*;gV*M@#1ogd01U?G4Y7cQYajaMD!6O{6i2rlwQAp*xfP|T+sa`H{Vl%uYiPtb#!<bc4'
    'K&tPA&-i3)clK$%!>|v_(bg`2z;R*o@I`l(<9}IZZ*w#m!00y9?-<OA^`{s-1UmGK{+i{ctP'
    'H?zEAlX&N2H^Oe=SR|6rt!O8&bHq0K1GnKZ+Bgd>pM>O=<X~HMBy+xmQIz+^fZG~i19(jmBx'
    'iKP+)==$%J=GF=vQqtdYQ^P~mZqsd|&?Ep36&v4CBi1yRM7b8qpnXv6@Vp^H$w0YC}J7(%a+'
    'ilKc+G0f=l(9~JgGOmOme&GURh#C@=hukiR4qz!hvMUQ*Wy-~&<a8Up>TC3fH1pl_G`R{kxX'
    'Ac)0Fo@rd9Aju>Wn}Wp1L#5zqYqj`{{7RgSIZL*)2l@VdCZrcxn>y5%gun{{{h8ggz^fv=7k'
    'Q<+wr)s#?D5V!EZl4-A97>|U`cg4hQ!q9rR|)ds-azQuUJi-di#1-4Fiso0KbY_^#*3_3vOx'
    '=Ce#=3R*dfDP6c(`3D0ce;h<6OV1--gh5~b9`XXE7nRtu_*Yc!bfL%DptxT3@!|w1=nq#men'
    'w`EEg40jcxxg9J?OsD7!h8)VBVerZZgH5H=~-YT%0Z1gtH8Q)och6gkiGSy8c>)sk!MRU5Re'
    '+I>nr5;T5kMKt%uBq1S8=wOlW0lw_7S7>TfX0`(m01RRQag)`8qv2mq;L<(4O%>(Y7&c?#UE'
    'qa$&XB=fcX4@AfNF7E((#bEnJFzMu=?lZ4R%pMV)FZ=u;7*V7Mf$;Dh)L<>*7Iu(I%>#ah>?'
    'FJU?%Vb>3qRU;C+!*x+QPeJsvAGy37L)p9>GW=MYabS@eS&cr`(x;dBHqiRC~XtK#d(8U;Pf'
    'd`~OhJ{j16P5!z>@v>Lcc6VkmB=&hK_Om2>dl+ivG+qp@bl#*oC8F~cD$8s|M5-IV)UxExK1'
    'XeJ!NZ8QK)}+OrOirak#&HZKkvdZ^wPpS;eULQ%liGBh5WnGHrF-7|o=uW8$*7GfR0202v>6'
    'Vh;err=iIt5i4aY;`C4Se#D&Kb%XzpaF*d)@u5bn6ce@PXN}=U?Vl;V^Qvv1U;D$kG?z8P?2'
    'dz-n6T7^Ir3anR_9Z2TKq2U9&Bk}(>jO8P2FuHTT8My;JTq5%zM9}x7OjS(_v4iWy|;HPkoP'
    'b{usQLm8F5Rw-C8g%cH_DZro@(SiH`0n8m%+?^z)spL#y$1%wMiK!hY!)Xp?ur@uLOpL?EZY'
    'rpH|AYk`bduMiCoEYu&R4P$SD*Z(y?p*q74c*vBy#@$}Awb@@B0kEe<+jL)forC|wrMxXc)8'
    'a3QNj|?b$FDG*`BC@z>JbOgBh_`#OK$?>LsJGbXQqTEmuA!zoGSAhR;;y>7YuY)bn-<3F~5t'
    'kPt{IGND|vuCrK6mKx1?bf5HgA{$?M^k#55D=u7yPbEhFQy%s&ZID`?f1jY=mv6(F+3Ynie-'
    'v3K<ZWmLRpud|+;s(}VSM-o%qV$I>vSIT*%&Orh&u8Wqz2&gXFW^wgNlGKgduvZ_Ar*=XhC9'
    '06}!uHq*KI(0*AdmS}wxNX3A&0iUSSB5woxv?+os|xQP{R^Q6nn<s-M}@Tspwgz76-HKp;vW'
    '{6b~N~NQz*~whz*w~Xji`%~@94@&O>mFythYjjN*Yhh0pDi~#-Ste|-GTIvS?1$i*PE2~9Lw'
    'M2n;dA&9J!P$YCG6Y(w5e&k3TCH%f`s{0D{r`!vD1U1iI}&nq05S(=$idVxMo?%WSywB-v(a'
    '|Eid&b$70j*8F*mSJ7nCGPjPjKp{&F7{WH=?1i3|#n}TVAKTn5C7IL8=3^(P-pp4lL$d@dZ7'
    'b?-C_{tY*m6EfNgcWKZyO%+H|*@I6^sbtH>_<gYGgk+#BYk8tFB!(R<_LdeN`MOt|YpMLvTw'
    '59^8SR+oXx@AaRI87VPm;lIrAPlb+=(2#qfc`KX41wRwrxd+1gzv>`txc!*xjNrZkXhdUNoe'
    'p#JvjH_i_-8E&*Gu{u6nM<UVsyHr<A{$0oP@Rw-+f<ZA9KSW>rxP(!<r*Zg+;gvgOBJ%!Z|I'
    'e!C`1@SXcB<2=;`?7O5BO|UwyMI%ve0yET2&n((A7fyd*45w;SSD+<mVm$kwr3H|DO*?diIv'
    'lo5gmLqXH9k(a+fR$9b)C%|-fc?!}T1$k6GAJg(iwZmK2;Yi++3?h1wlRZHC-PA#W;#$KJhQ'
    'HXq=Hgc>DjOLeZ1Yabus%;`jcP-XrM}v2|MPW$J9M9SbkRcU<Q1vlqI)R}%bz2S@00plzYqw'
    'RTgguwap%L<NhfM5L)K_+f4=5RQbcDAf87i_q!2ufW7DPN+wWBKGn4;6!Q)Y!?EXUwvk&O=*'
    '0MJ>9lrBQFIUSbko380B%j|hQ>2Mveab6RsI(muv;^Eo(mB$vj-FOAYo9<+SOa5@yCn!+9W1'
    'd$>UW#mNBvwj7e+o^>tLZixO3-0bn_3ZY;fqC!M7T|+-!ppr}SjGY#95(eMv|-UyY9K?MK3~'
    '?dQ40nl1Tu;~Tu17%gAwY3t{uKSUs2VMj2*|EJ(4SR8L@|1JCY8ZoB$0w7~HcJ#El#<>f4_L'
    '^&Vm41QLGm*-qokwwcvJ_@N8)aS_^#9A8G)+bLh-x=+2(d7fP<QDQJ%9x^PQlX#CzJ+Bhz?g'
    '@6D>nTPo@0_3%~nNln6Rc=Avr$kdyg74dTRq<N!cKeP3qTvGy!|T>E&&{rk#$tR3h%v6$kX)'
    '^Q+5C6CpeM*d^fRm;@oY>|F)dJk*&XQ$7yfMe#u8?p{33pSm(Yutu#6a#xASiC3*44l+L^gy'
    '4iK${UEKkVFOMOM;RrrWG_1DoXVuA)!?+J{J>?Q@vK8fb_RaK<M!+DwL|@}u%ucHUfYl5LqJ'
    '*k3%(6`g0Q&0Sh%7QkEt?7GeC*>_H2$Cu9dm|^;hxYH*AH&L$i{ncgI$t{6=W0l`#UI;M&J%'
    '}1qhjSOl4;Az6qGDdwiouX4ASeYCK=g?$N`fY2q7T5QYa4m{npBZ0^_8I4Q&cQlkt$ITQ_m<'
    '$@zs2rQcF<n-*lkmu&}hH5LuDU+bIA}_D9&rypiUlcp*Oe9+W=$Y4!N|$WIX{9QoXUe(F#?U'
    'D?8K$%sd@y%aB$h2MvJHW2dD$2s90QRtyQ^4yK-eN-pIX~K?~d|%+<1oH5IG$$0J?IBJWKgt'
    'u19HV+y`{53y>>*9f{5qiXQM(TW0A`Jl;!xqCMtEx|j$;XPlR`@vVWyo<-xb=mpaxTN$_s{+'
    'Q<`)ThsD}cQ3IAqmY0~Y4}QS*{cQs!1Aa6>ePq3CdiyjU<35%{nI$Q`2zhuw>|hMi((>}blm'
    'WXS=7Gd0dvqhVLwW<HFFWmUr)MG^#PyN~TPPm?3EA6kNgx|$hkkmHo3?2yG`)6gvQst9pAeE'
    '&nUuL)UiO!(;A?CR6dc-22{86F=jvaqq8qR9q8;Bu3iRMk#ukjFfAR$3lnl98a)eEj(}e)<W'
    'OPZQ6N*E}$SxqH3Isp)1Uo4o!j(frfu2Rvb`lK=^5E|w1G?YF<O!Zc4k&jaRrom<xrGyCf@p'
    'v@A=_z?cEd`C;l|icVJ?nUgfmW<awY1n%1WdV&jGSPHp8+J9w`*hCw)5P%1v7A38n#50I`IC'
    'SwjVF(A{0KSeIEYp##A}UacUR<QJ6y^rZ~&ndLP?l!2-RGfEky1D6Q)@;N~0fDbJxt^jpTyK'
    '*$fc?~)^?36T0FBQiM<sup+T<{oyN)zqjPE?7xD0q2L=E~`w!c<ON4}i7G4tPfpyCme1I3!J'
    'yt{`bZ*$8%$qV#0?*bp}%J#Q8T>!o}wDZ41_kPWi9g*^Wj5j<3&XSxuF6uh|%(jO%&!3cP%>'
    'm=fe4Wl+}la!Vu$$8y%Hx839A+~L1a|18bQcZher3dgv<;#N*Z$f@y3E!YQNeuFDN|}r_(&G'
    'ua?CA}1Lpc>g6EP}nYeQa;)4p~ckmrD)>|ix#$K%PvqXS4{HtNFq7!!A@)0b&`oSv!>{;Ru`'
    'JjA_LtRcf7^q@J?o3d8ee2ksMClrIlJ-iN>r1o<A*Nmhtee0C0hfK_b43s)Vm0_dpsAoDTLj'
    'ne(nq<=*gr{9>y3?VL4JOT4IVB86sqSP0r-FfufpOPaky(+WsagFlN)mmBK-)4Hkig}&XqbL'
    '|rY5#ej>+Gk8A$^z58O$zPM7CsRJwt`VTmDQ0*vn1OHyN@xk8)j5dAbNhPTyHXfkK8;IoQ>R'
    'Y{n|19ys&a@kay1S*8Y(Se%Pfy}+Nv_5OhBm-uc5TibeE+#Sug_B4aSusD#fPI%&CY;hh$4q'
    'nyVneBLCds5B&4*0rfqv3Ca2_TR;**X9>B>;)m$jbq18kZ%dA){jy@lVpnz`8v#V&X{QYQfp'
    'eI~JoXuv(=4<o5e2?_A_lrj9(3=j9c>p3VKyCqQUQkir&Y?C#F*8B<|h??{Xq~#&#Z%_%v><'
    '@&6X2$&?oXLR&lM}(5ezU#!cKnOfzqi5N*+qYzmo^*wcRRWh>9eiq_*F0H(C1ooG&#Pq=Ob6'
    'vpGg*Tj6Cbx=5lQ8yVL1;x;7!9Ps%VZZFXV-HI;ExhbE6b6ZQBI01WW_;zWlSK<&x~9%Fx4c'
    'PtCcs$(E{hT{U(#%+Jkjo5Y<B=NRV={(qm7!U+dLoD_O+E6;66K}pJo$Y5@{c2l&&?eAIfD~'
    '|O;$Q;{w89~FuBc<((kM`_DXl3s`c42dcAJr(y2m@~<#|OC$b1*fMa7RwJGiWQgN7H|oAoFF'
    '<R`uolJVecH_a(XxH<AB%d@R9|1yO6L3`j;EJKuokylqfp&Q<)NPCY~&-|j-w)Zq2c)wqHC&'
    'QKScBnt}Yem>r>N~(@nx`_<sk>`KJU84xFeV5QPs*^-B6<5t`Wyu$NaF5Mu8g`bcwaejZu{H'
    '}D_h|9b+<R}N~apdpQ}XxwJhc+<{v)7gWsnrOx|hOOElkrpm`QNuKJh$U+X%;h&XA3?*+0{Q'
    'p*Cl(k@vTKe~(dG{_lp@y0J0ma)it5430w$fvn&jut1HOSX4#NK{e;3vw_PM}8gO4>+hcOEE'
    'sfz;EPG3xghU5Qj$x$1jia&Hjt>PrPBJ1R7)q%~PYz%8@>np}F6og&o-735RVkHG{!g!(S`S'
    'MHt<xS+^h`{{B6oRn<EuLhR$T7=?^5svMf*!6@j;4UOwZi}{&;>z%kB5?y@zGrDd)XR>FxXH'
    '1v)o4WK*!0V}u+;;A+v073dLTln$H>TwtOc=*8{;Xd~@kr7m(}VsL`C@e(3l>3@%q!V(v@Ga'
    ';>Ph2uFsWfNKew9Xak$<_JzD)C!pR&sB|gU@bHIUXm5Umz=<J)qDrvZIs>%Jajn7^LyWgk`3'
    'w|}vu)_=v4H++!6a5{GlJWjQ35^+Jqrl)*)-4)jtXoExgkbTbZOU+j*5!ZVOY~J~CFXVnP{='
    'mVH=fF6<uv;!J!cXc5=^NNTtbK?LkL!~UmUY&#GB!GD#{(>dE?8iDby`c{(<u*OLY>(&MRBP'
    'v1f-XNA2w%`E;BT1|+t!`sbzKW3+zdLGkuI3)sUj(N{g2I4D>Q<h)21xN|+swi=p()P6R`;5'
    '`u4Fuq44Q-bCr<?&Y$zla#dArdSK6Z)w)UAkDMg{S(z;|3fSebB8*q(|bbsZyCxm~2o)`|8c'
    '5YYOb*;n!STLPSGCi50dM4;t;bjc6*E5Ov_ZdhI2RrBP%(7={@VS<N&AOKBx4IKC<D_mVV$I'
    'V+=MC+wlRUr5SQn#rZx(bfKQdX|?^tGO<?Dy}(MQFpi->xkvnCK;8ebRHPF+WOt!!%4S^<~u'
    'll3tptj2zno}9sXT|8O190MW`mMQ+<Kg^-mmKS+c`R)|yGz0N$I1shK<S(aLDAn)V1QW2=d)'
    'DYP3(=5z^2i}EZqChK`nE{=+K>V5kZbdQ-j=0xPpsUTwKdUDWVg0gLq6mpCtH7oPhDpAbQey'
    '*yTEAYGBoFn_+3%^g#?TPxD?ZV8xu|&^BB;{3uPPzf%uFaFeuzeGw!oIV|O6$HBjKXwHi>wc'
    'E%$SaodlidyHDLvdUNyc4{fQnaeNPtNMx!F*S6s+mz=a?r6VD;o==(%NJ}MTZAxV)LU=#*g1'
    'lpP`s&IblDr%bF{Ts^dTj}okFxnIpOZ9kCbZhFk{kQ7cf^wA<A1(Fu-+Jj1!((r-h#wNPVmW'
    '<X?Zm?z=O=yTZ=rOqUUH*VMAb;)U(jyUcTY!`TF(PO%f?%EF1q5q<&6S*YoU&XIiJJYVR)X5'
    '0)7jArxp}t!u#V%It8*-cavWJojm&N%l8`zSSBFok3lFo?gpdDPlfJItu4~{8{7U|gW0CS0S'
    '|946}VAkL65a1>PXJh5@@&Ys;td<msEYKXG1L#aVO<}WXzqx+0-emL@?#HU)A2@B{}5VCx{k'
    'mA5)c4u>;4fg&Xucxx9j8nUd}*l__d_ksPOP_LVbZvny%X`1ae=sSi^a0wx#b_3NqikbTEWU'
    'kcv|eC4i_JFM$x^XNK%Z?nTekA_FZYJ?E&ssGWm6C?-QPDAPR8N|Ut@*_1$1g{*HY%}Edrn#'
    'fXhoIbK<8g#L#^(3K08EZAa_xn0Tl`X2$14BA&h7DF*5=X|5AWq^S{Y~4=0rCVT^-L<%p^q`'
    '7&MQXKl4OID`dgRw!xt487Oxdo%j$&C8R9duBYARLvvm;S-Ii;<+xQgj&NLpI-%AW3Wl~tL-'
    'oeYxd?_|Y+`_bR6|F-!}vL}MQBCh?xg>E6yO1^uuwXCS>Ep&lc!&IYB4&1AUDT%{iD(%y6u#'
    '2{T!PZ=EvC#grg20El%GRBocr_3<3E?uiGhh7xgAjYZ;tnWxmis><|R7h5*$L$gorXea_}x>'
    'sdAz=k)Z_8|9*lQ~z)Cv{banVISm?Nlw=2_Gz5HzUm#5`q#6Q8J+6uaC14t7FUB&{U^;@bt^'
    'ZLnvx2Tj_+S3b^7}6v6Q>RirQq++ijzNGp&C4by3rH;fwG-bF05ao+1-g!z*;N$82M9c@@Me'
    '?r$OEDhCm|pdq$dt*1Z&BtR9yGqj_X)RuqrI5ny1F_?hnJ6Ex}-E#H2Gt7Uyd5&@+5Ewr{EI'
    'Nry%GMhxoWHCrJ&I32Ed<*9A02=D?P;ODr|8JZSU#MKMALTsQ<7%)v+8>6CV8>heiKvu__*l'
    '@a63_;ZQql5+II#Li$@<OcG^$wHDPJ%_8=Z?CAwUr#&ESLeAJx>C;&o)mrh`sXn$H$l2!A!^'
    'zMIQBC+Hv0d(@M1AU;pjOO>g<0Bkav^yo(fZTslOg`u@ZNC9(;n0ST52`i6ABs|^;Te;#xP3'
    'Cw*vz4(PR6&X*_|=EqklQ%hI_|3xgxv1X(rh+f_1+&tzC1?C)G*pApM}-hT<*H;cJS4z<m%5'
    '9}E{3OgSYre=QDIqp=`>eg+?(q1j|;c{vu_bqBYzZbOMC>BX-^P68wW8iC0$Fv(R`p>9u%s8'
    '><+(c*cY>sRcKI)lgJxl$di8q-MFGZKBxDsjRo4tOozmy8S={~d0lyc(^~hSSrekmP&ijQ_='
    'ZtZMN3@1HrAK*fsV)g336qSpQ!Aw^R32pGRvr!U??eN??Mg@Qu986kjJQFOOD&7-cEa?@qz0'
    '*@9HhJ$@X@<@ib4jFW_obIlTZdVJTpAALL&VH5frt3i3jLNu3{~gHl0Y)GJhW+EGT2?m}u)@'
    '%@#<Ke+U6<UOK-&cDW_&-S!_6%zsCbUgYi;7$vv(VtsP|rMc-2yAtYu_z<vhH6B%?xp*yJ%N'
    '3#V%>e3@l3rO)DxLMuHj#BI`(J6roTHP5TSpcrEpMJg?)wFdn}u$+e*M<(UsEJ&yUk>~yd2M'
    'ko=v@AS$hJ?z=FEslV9g|Y2;dhpGQ;T|mhQ|ByFY0*SW^cqNf{BX{`T6LXwe9uSE>P?Fw(;6'
    'ZJc_@o&W@o|rA{~PO}CikjVM7i;rO?UvDA{)Q8Y2$Jg>k0Y4KxeQAE*|d>uTFQvmD&-)LUvs'
    '2HMxp9y3oiU+yvQ!N&2CI=NVcWoZ4{-(S9Qh*>7|M%5BZlK?*-CGyxsNY_>wmvqzx-V*t#-p'
    'D+sb`N`<3Y{Tq%T5?$Dz<X=j)Zd!dTclServSej{c{LNd~6tF+w7n?7GI*Ye!(D&t*iy15O)'
    'Z0U9W!x2+j`Y04k|E7$iac(x@hw(44AOP>G{?RNfITTm7gN?YwQjCjZU25pOf968{^$Im3Qm'
    'P_N0Gu2{fNVz~LKa}+g_WllDfDr?KQ+Gd*U^2K6-uU0S9bY~Xr2r=2@jnck-jUw*LgjQP-`i'
    '<A{Yip##Y*vWh^two2#v{R5LzGZzcmi=+g$rX>GNda*ia%vEse((pmm)Oe#KLjR9`i<4C66o'
    'VuTLrSC1jsjUy<lf4M0kD%Cpbf9)1njEDsg;~ZPbDk^3wxY03PkbtutopRu$;jsUsgsd)H4O'
    'F8ue!wkGI6?d>)QboPO-19B0lbQE{WL~$*$$g6^u1;3p2<=e1&)|=zMkWGNChfbBu8{S9CY6'
    't!+DWP~rI{?&MWzwGiO9yMaj$?-bB`)Wgbfv)v{zfCNPk+eQ6!w!91WE+VuKa(C8OtOKF2cL'
    '%?+ZybI1$4&4jbNbrV{XaR6e67;W@aWwdB=OvT7FGTxpDegxaf-omk*K4)QGs_Z(7OE-xXtR'
    'p0XZ&sTU%WxJ#;M*RIO9!o*kMgf*WtQa#o@7B?y-Hy*86(+UnIUZj#KD>qQ{XE590y-;kiri'
    'tH+Ck>$99m)fcww0={Li-7PRyEz_;*CxAXt?_6k$|#{Un~VJ<Ijn(>%$3CM&GZ_^3FzER^A{'
    'oQla;0V3GGj3^-UmJMrYF2YsiDoVxRhc=-AXwnR>DIKAV5N?}0X*68Lm6uLrSK5>eE%Ds!r)'
    'Ns#Urhp5_3OFf=ZKz1*%|2BAO7-%1@ebB*00p(d>LfJBu#BAVbQ%=&YEBnW(yKPB+o<t@@)}'
    '3wA{4U$T?M`c__(jn8Vx;|SX&lsj+dp4h4CaSJOy>fsOJjoA#2GuMM{KJO5`<Z)#-<n==4~o'
    'B*G-FZm?*O<v71)4+}B3U^QdR646C!wRqC>Va`mF+JD!dQw4#BBH7&31ES7qlemB-I<`WV7L'
    '|k`k`DN*#X4%&jYYEvg#b(z&EuMupC|jD1da!lUAvp^xhkQv?jo)^zO{qMvXW5c5P1b0|mfy'
    'KY<@<K(A$RuA&y#Y6Q#h4XANNVTVfD#D^N(lRzDe>G{R;SUuKJrxm@~rU>wJ%eo;^jPs%dI}'
    'e^2?43G|gTVFP`Hje0#+m}9qjzemPq`r0K4N3v_#^zseIzn93Qs;z{LMOPA+(CM&ciCCUkgj'
    '4}h<CVv#szC43P}Slca_3<k8=P3a92;{5?z}^o6I?fU)?!J;i0RC^GWnw5=%8(7if%4RoF+-'
    'cr(?N!j=FClQfWnpz3uieeTz@v_$q#;{tQe_<pWGx+O>V_q-o9uem$0JAbyv7Dz}DsMEJh^4'
    'XP7qY#Uzd{*s01GL6jZl(mX72Rxv_(=6KXmvW!&oGfeBVGQ9#=#m63LRnq8=N5&p{}*yaI8c'
    'x?wngO'
)

def disk() -> bytes:
    return bz2.decompress(bz2.decompress(base64.b85decode(disk_data)))

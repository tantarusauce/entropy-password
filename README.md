# CLI Password Generator

![Python](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A simple and secure password generator written in Python.

> Uses Python's `secrets` module for cryptographically secure random generation.

Supports both **interactive** and **command line** modes.

---

## Features

* Cryptographically secure password generation
* Interactive CLI mode
* command line argument mode
* Entropy calculation
* Custom character sets
* Additional user-defined characters
* Supports very long passwords (limited by system memory)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/tantarusauce/entropy-password.git
cd entropy-password
```

Run the script:

```bash
python entropy-password.py
```

---

## Usage

### Interactive mode

Run the script and answer the prompts:

```bash
python entropy-password.py
```

```
Enter the password length (numbers only).
> 64
Allow uppercase letters? (y/n)
> y
Allow lowercase letters? (y/n)
> y
Allow numbers? (y/n)
> y
Enter additional characters (type 'auto' for common symbols)
> !@#
Copy to clipboard? (y/n)
> y
```

Example output:
```
Generated password:

aT37pLdP2y0ziQgXAHhuWnD#nqYfmOCTkIr9FGtMbB8oeJ@V2clUKE!xSR41N5js

Length: 64
Character set size: 65
Entropy: 302.02 bits
Copied to clipboard.
```

---
### Example: very long password

```bash
python entropy-password.py
```

```
Enter the password length (numbers only).
> 1109
Allow uppercase letters? (y/n)
> y
Allow lowercase letters? (y/n)
> y
Allow numbers? (y/n)
> y
Enter additional characters (type 'auto' for common symbols)
> auto
Copy to clipboard? (y/n)
> n
```

Example output:
```
Generated password:

o[p?iXoG*"aMfNI{x7?jjynfm'V^~{5T0"3<iFO>?>S`[XIAX@\IOau!Hp8er12w:&?bT(\4nd$j~A(*9|t)4W*EkKSU&#'i=L2Zvk=Q`RX:c`${pN@yl]SSK]]od:+WR6\g^H3,%4jovOyq\D\.;~|l5>0<sxm7+x9|@!!-,#3)/S->C<~^D(:8`-gC-:13&ne>tTEC/AtSPQMI/'a@29?bJ0"c]ZDaUlUoI_;2gDaWD~=F%2ut+kWrRlimU]?FdvQD0cD\l>mWe:3<g}k;6dA"^L2|fgn4xQ+>Br'XOb!,VCM<=t}>J8gfEdtcS~WH\?e0qUrM#-(~)277;{19nw[C!Kkf,5.G/i(hU*ydA8NSG8$@_P}&$Y5W=0x{uJJ9=6,]'KHoSn>fBh}MYQ}m4de1bs.~2'QtrbRkEw`^8N[p^[:#d>ygY:p<I=w@R7-/W'_h^aKicH]K(1{GW]qtU%<$?^,v:K&u0"Mnf~\@;8G)zp#zkC,C5'U4O9%BT4_hCm=#ZPX"Th},B:(gD}J{C#F;rUCKY=+-Ep`oPqUj6+e.13B)6qKc~}-ToLkPu?i~*<][H{'Bpc`g|>n#kqVq\$OVI.f8<OVI/zlD2BAzxha"[Ns8AqP{_,{$[T_l4'Xa)s^V9`^RjlG1]BJL".gQ=!QxF*<h[fs9u0u'N@@fmz*A}&nk8|A:Qb$T4P-PS,M%%r|_#Q1@/C{4/N5RQGN<u*eL1O)-9"v|{2/W_RM<]!z#F(&=,-qeI"5,ryM*kms0xdlNqJ1@2Z63dtI$>xuwr!8M!yZ.i/E#jVLez&L^s3wYz3ZHYhS;eJ7z/r6.ab?O!HGvOJYe7?Da9Py!Lh57LqJVQS3F6KK0E5mFzwq4|v/6h6"GwppXs@"`G(71&*P.];5BcnNz$ZEV;%w1)y`rvGYE-Z+cPA$Bs35$Hd}Tj^l_qEb%o+tyV7%nT4X0iVEKGW&;9ZRgm;x?c|vpP(iYB%\aL%%w+Y.Zfp(!W[(|O0FjOd)XfF}.8Fj`t\Ua9luAFCY]z+w7)*4n;L6Z|simo5J\D_+ob3c&[bhcNvgIEhvr)~.vu7LkHjMXjB[HlZ`RXOyR:sb6u_xD*xRM'TbsY

Length: 1109
Character set size: 94
Entropy: 7138.03 bits
```

---

### command line mode

Generate a password directly from the command line:

```bash
python entropy-password.py --length 32 --uppercase --lowercase --numbers
```

Example output:
```
Generated password:

6jXwq9atV7urH7xCFEMeQLfvgcoSiU4h

Length: 32
Character set size: 62
Entropy: 176.31 bits
```

---

### With symbols

Automatically include common symbols:

```bash
python entropy-password.py --length 3939 --uppercase --lowercase --numbers --symbols auto
```

Example output:
```
Generated password:

:<On/Y6uhMJ"|>U#J3;6Gy$2:~95v3'jUYmvZm9ev?L[p)?5Ydbnkk(78:Dwmb+25KC+;{F&egp|je?RFILj*v9<,b!pbX![acc\DYP1gRk>\O"JSk>#jvM5%BND]P5a90l+!].xA(`cwB,9iG]uc.~jBt}@z,d@:DN4Kvll}@5)$v7&#R=neOv+P4wy{GimS9S)>j@iuO)B(8NOFciHH1+&J^_xkyr1+}B|_Hp8"{Q^<.oBbU){=B}UcU>eC+LDR[GbZO9=Kt-}=kU*=j"Ps'Z1F[L.D4?=8uyI7j"5E4/D%WRdO?v~E*8XM5SB`O,,f4,%g'sV0%tUN}1Gk_~$qC{=_$S&f'r*`mo5s_I&&b/"Z}Jv;emu2NZF\p7O(88@f!gm0Tv&%-Pxia~|o&Tqk>XbeMuXu11{\w%6olsd4hwm0Liukr;x[=FBsb:vvRWnvPHjUf#9Xrd4!dwVa$NwzBww;}?C$7K"{#FzysJrH*]|rS`3>VK3ws\_\W0^):lM)O%Y<3myLFbxKJV$J3D,R<\,s~r1,@{:HpgwZ'6py!IN)dEM}CXI`H=\*Oz\b?"b~vz(4J&c[*rl$|T/V"zg';HyFI+;M.AKA#8jI!EXhkTe]2:Pg?6\<Z@5vdZttYBvxU"JG_;./I/1%a+s~I6XAM+<lHL?yQj#g7!It1w{Y_^0O[Q^UC?TPWVo_hB^@wVA+kg14/,zkg4948M5(KiB3Zf8_ii"TIrq[9{K4yU=R+Mj8'1-A3/f~#c]TX:-*l6BYAYr!h+wEMWh8SUrUbSuGM#|EP*a7Puj0mKQ>E6YubBiy=G)VXzGUk6A?$euht"t=:f,lq/zyEr^Tm}#deOf*E-6uY}W|O7VG03T[NXoh[G}i8MtxkpO]3Ri}s"bu)GqaA&@*%!ZOr{=qGWNgQO=<de]0=ZN0SdmZVVjXPP2xgF{GNL7~VWaG'M/|QCJ/@oa_<nd;/xUQwwqF`fID^74"$c4*O%<o\~EzVyNvu\PA3eO/9igm')C~A(nG1$P>`9JXY1H^Y[`8oi36Cj:.{q"pgl~!mH(`$45G1peQAaxIHH]hb-rBao9l_2q;(E$0%\[[zSI}rds[Rex9x5*(.x*WtpGBN5TJ-z9!<q]d>JVK#+M^q!~mCLnD={;uc]_j<VCAvTV~H/HB.~})zY!_.#eM?jX:o{d%oid;wm2o-K44RDq,Vf1Q+|qZ4h_Pk(E_fUc^s3p(.X@q(8L;Co4/zgcjb_zjHpOc^xnsyD6i4$'.:YFa}Nt-KODxChu&i<K#+q8Jg`@ct*9m}t$yYNwgyRg:)j{;4H3Y0\W_&15=-h}<Jq*T`P&1pr<gG[3{>P)iSSo7>p*2$Vsjzpg&;J:MSoP`6;OG`7]3I&!FyVywPx/xK[/C7BB1<8}?f.;XF@)I)y:'eXMS*X}]O=U1g2@%,&u+'//:'78/,h2Y}YB|l#~LY8!~(MV,0K-+7J#l`'1$[;]hWRCZw3vq?;#}m|qJxR6|<+Q]E'1%5.q4xc(SkQM(m.U4q%CX69c>F_W6A/`{=el/M!&[{m2f.)t'".[#GtREEGs:S9'ZDR0?RehYsyK,SRKI|:>^*ofJ#=cb3YS1ZR%IQ%MBu.m#nl1oN2,2|(m0h;md3Z;d&i4tQBRh9JB6a]|$i{Dl3Hp%99+pCRX3tFjk-F{:(NESL+TI^([W7.~wDw|TltaZo^0z@0c=\&6|"d9w*$;JeUCn^(.DN}`B$%J!sZf|TFn<<@zLT.;j636@0r'sE/Di}uOb,0kv[5k|0@zB'6s^ZV`?kGE8=Qy*F/i{dWz$si6QZ2l*OS-y]IA\n,+a>?z"rV5?hd[8Kd17x=?V6.x'Qf#/2?1PA~oT,^$Pij'p?C7(Bf`8TS/[*i/d1CE[hGsYg7*7Ce~8)m-U#Fg{b/R]>ytEY2'"sM+9LMa)DJc6Qr^fT&U7"3au]Yxz:>I!X&m7JjyGiaQ$A.}KxQ7sB^za"nT%M!-DWnU19R0(mX{*./@A{%XIcAinf_=m,c_)2-})Q2U3f0n^sCj'}OD0Q^"J))a<oL'OFf#8yDwfUvvl=Q'luW=V;z8G=sT!|#-?T&k]%J2u"i$RW)oph%Ln}rq5nIyZ+-['VJaRc8)$5M$*r*"MAq:-U,[6P1XEi{Tl><7h5CZv~}JSad3rTCnge$`CGcTP6zJGY|;6ogxoA6r&'^9?4~c"]Q(-uvkwt#az;j=t!B_~qO37TWQ\pu@l4R(K`_Di8#EV?8L@a`0\&)jbp[e7y,%}2FCky,r}b'{h10kf%fd(ep5G[sk;-z5DjO?F<&PK<eWq#.c?1*-:)Nl/P2DM!W|E)"5NF/qjdA+C&S'x\Ih!6^uIZRy!sUXR\>7)\m2cL'b-ldk5T_@([5B!$5jOv5.2'@kH"<~,E"p1&OzK2sL'jxWzwC4{c[0L4BI4xr)h'~n88_r)=SIdTtX/ceM)E@f~RBMdlX%xNINzA;n/4Dq6j,[u8b@LqUvGK'[_H4?4\J:\nyA{4(fv8]MMx@HKwDB(p*%0#Nk]i7;~EU5km5OuA~c;}SP?aAZhxv^zLWKKiKZ:%KDfwNf?Q9r:es\cn9(CyT79PHM!H{lW]zn2vgz{ISiWnF[Q|L#V`sb3\rh\Ud(ZpA3|83xcMN3_<&eei7)\s-7hpNF.EPFtosJo7zq9hVH\@'KH_f%GLD3lz:Jg]Ee6pLMM0(uKlx(}o9WBd^+~!?`/n~S;{M'*>|bdBVVQDn>Sb`[T)W/#G"<1]>6:2O*BN"&`-6XL)lNLy:)fTJkg1~qS3G3W2w=L&]4cbJ'p.%T_X(]nfj1A~`OgSYeAbK_l8N{c^rX3|@+>xk&9Ng#LXTp2K?$|":<BVf&VIy9xHp8]|D!tSFEPI:"3:2"1?&g$pfB5w=f@]pY&V@>PR,,Bab8jSL$,85Tdsi\c>$C^]^kimK_G}|#|X`f2o:-RG.>/F~F`oSw|dl6XeVH6w1,^b\(=|7DfY<J9S-Rw:ert{N67/{LC\`N\\"NLajeghZF0?oL(eu-aQu0~%cmf|unDBEWN_Wu\%yg<Ndqt$E,M@{qe&q8++pRYRScQaX"v^RqoI/P#u>"!bt[m>&y>]&V8A*=0<2<;WRS2n~KCV8hE_g>Y{!_Kt[)1=}7Znu9u0c^QiSq~U^`C?%#<m07abcID#g-%vf{+;2>LUIbO$q9q\]-YkPJL52g1{v2+!n9,rqKVTZOj.WjD+klFraWG:)Z$!gRnN[pT$0+1_kW0:ao`-m)!|1oh^Yf!Hkl</SD_@3e)EuF^%@^.Q|R_<sbH37Q>}S`tHyHYuv@6M%bIpwK;V8J%N?*A~i>|+x4c7<v=[*b(_J@HDQ;4$Q[HUQ*$A2+c%~.~`-hW.?pt.G(o,sC$[X0nl\n#&\PEH(6bEo:Yo!il=^3uh!sLny3_iPmEpIA5^r3razM#=#F,0wYet4Wj]W2=d%GI_@9"uH??fxZ3+'/>t#v%E0!+rH(QN5,2_6XhjAXy-U_a7I7XZ'}&a>kwD:+V*-YPP?F2-8mvXD#[?X-Gz3`\tmtARL]2WIU:aTHrIlEz;|7Z!Ewbkk";?HgA@-hFRt=WOOha&|]UA6$x)Z,5PtK(4vUBA*.=eeLt!ZKU6`"~Jy+TjsPKCPP+Q]2mVO,j'GXLn1CFF$#CCgZx~D]#0<T5c]5`Ep\Cp\Rx}mPq*;v>t|hsbZ55wnT-Yh/lX0lHv4iHwdY`!&\lbA>N>u`>@LaHk.<`jd*rLpdZU%adV.qooUV=n.#t@|xFpa<\e{;WN-C'g}CwQn7zD^h*ztAJ;5d.rF;Ky64oNa*xqhT:OFs!cZZy^`%r@,O,,fNR<Q9:M<rwAQtyJ9Nm"i}D,Er>U5YT-u}`xnh{etWY0o"W'SU=;qnY,"^bzH@7S/{|$klo][+>UFgIQGf:&-4^<(=)]>9haqs9}4rEg@lzLWvsk.Am-sOId(w*lPZ<CGe.S+

Length: 3939
Character set size: 94
Entropy: 25687.52 bits
```

---

## Security Notes

This tool uses Python's `secrets` module, which provides
cryptographically secure random number generation suitable for
passwords and security tokens.

No passwords are stored, transmitted, or logged.

### Does it guarantee at least one character from each selected set?

~~Not yet (version 0.3).~~

~~Currently the generator is fully random and does not enforce character requirements.~~

~~This may change in a future release.~~
YESSS!!!! 🎉 Each selected set is guaranteed at least one character!

### Clipboard Warning

If the `--copy` option is used, the generated password will be copied
to the system clipboard. Some operating systems or clipboard managers
may store clipboard history.

For maximum security, avoid using clipboard copy on shared systems.

---

## License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this code.

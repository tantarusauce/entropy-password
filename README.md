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
> 32
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

KqHm21StJ#HTsWLwx!!zQF4J#7yCYCg7

Length: 32
Character set size: 65
Entropy: 192.72 bits
Copied to clipboard.
```

---
### Example: very long password

```bash
python entropy-password.py
```

```
Enter the password length (numbers only).
> 1227
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

PE\|ZUy'8Ou=_^6Fxe`uM/yPzf8ijk!g3sVAEdREQ+JdrEHInvf_wN/@]^yf^5nFT"Oe@xqSC"-`cR,RFgWl0MSztMjjr3@\sOgd*AIoq667~~/9/#A9}4K's3dd.4&eys}y(=[LDN6d:t`!U&M/+ELb@J@_'mM:Rn3'>\_uEd27hBXSJQM)jEa|;v;o=&e]")K?#N|ZTF.)!}.2,>x+:~Y+bwZr.hAjqO9&aZ/Hk8spM8n17udD}/QfGqHMu+H;u2/8@!KN0a%zJP5!$7Sv-SP&bBX)|Ebd649929^9FiP_f!F<!n&Zt?[J`2cj;6pTBLvLo"Vg$%kf@cFVi,|&1Vv\0+(^U|'qS!`ZIO5~|69>f<MP&CRI5pE<'E7@BxwM"-4l2r:yW$.<Pf!o1e]lc'>|l&@bn(7/Fx$aBQL}ZWSu{MNo8DY>Ga?'i.9sqL`MBe-z~f>/hwP[\o!VXq3_ZygC1X7$oo+>AJb^b-0gOV2|x3B"xLC3l61Ca86KnMjTv9ze[3Md)n4Mt"<:i}4?3H.m7(>X,O]`tGN?9~t\svvZXYzREzKgEz)w".Z}@,TsyLD8R|@C9&yaRl"-PS~\FeRQDE<?P#$)G)SEL@H\6(?YV:~u<@~#W!#(#o:KHQXuf3VIq\Awjws(b})+\mf#n_bK.{<3BlEa"5qcn1z*ip:PeA}{5td/du<5tw&I_6b)GJ{yW:h,C6OOYu;>.8M?)XIdF!PTbIDFvW!v|JxQEAxJ9^5/L|Ft45LCmq.qn:D<9rz):'#[oG:t3czobOM+BBiP4%iK};|UZ['$LS)(h<8/F*f^MIQrLo*oG;(Xit<QkN>>#&-V!=z#eNw%Opcp0S^n\r\9U(5<<vZq_)]>9<`tB_-FJ(4!1uoOjTen`.`IGP,Y+8XN.FA;ftS}-0Z^E[ZSkvA-f+!^9GEjL+?=6B9890?/ZwMqu^<%=iI\|Ww+;,uC.1b1cb`&,{[X5C'fGLomFhppjb7Z,.$*W8CFTw,hL-pq!>5^3WuY"Z|{klW%%[nVoH4O:>ur1[W'g/>ki"D$o.48(=xLLT5p'&`"{wn9"|Mp{8kSazj$g[f06d1WG$k2X,:Wy<g\hSg`)h594t$eJ-v-xmTy),M`$vxqn'/a[2#4(}PlM#%Wn|>@6*Dn|0V6N~cCzbzM1bU8ZV&*bz]v?(K[(GGlaZRMAEGVR7Bi,0LvM9Qr'(Gd~unKWD+r_dgdBo[J*o8        

Length: 1227
Character set size: 94
Entropy: 8042.48 bits
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

Fcli1bjFgBoyckwPps7TNg2apbQ4zo5o
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

RjXSm'"ug}Romcp_*BoD?2X?wZuvdY['LsA;yGSJ40|ngXQ[ivCf(UA:e/FrJHKdFr)J]hNplL7'[<INS$9i'8x]D/`E#})iC}&[Tx"nMN7a"q2b%)D6K+Pk$Uhz3KyV!@{XU9,5_:2ZW+%@^6m0Ti|wmP'YvG;[J_=JMV-c*4?E1iIJ8@`CPy0y[A=<yD8Yxi86,CK"be9HodLIo\;0vPv$<z,s_OA*t7"N6bQYG4H8ZDiLM5o;=}4{*;!LT45@I;50=ey!KzC8(^^zrj9PB$9[@!r/P'5f^83[&jxi<B?Ix7rVxc0K{&yN@:7%jO2~H-)8<|U`}Ww#t'1Y7nz,*HcUe:X%hZnXZvPzT?b;d!/rOx/>_A{6EdQ&F!t8riC!=YXr4@i$c]bq%vO81EPKv"UwTm?\)=V3L[c&I6t@'eC4I-,9Y2Ini?H|2*~"=JZ$"K?xc;S`vcMv}O&jH.!gb<Q5(s5?sn>4;^oPHBir/!B,2+KwB"TkIs~Q`~-2HwHr$~hJ!&a3/0T^sGh:R;7_1yPqPE-j[45vTl$<200fHzmH1H]+|OHdkn/"IF1@zs.ry|%|vCzrm|xk-"wZ0Cro#6~Ys$YY4[hRi0Vq`z>\>^Wa^<j:adY[D0@o!^o_]O*ZCCpq5STUC>a0"vnXa+F66_Hp<CD6ypUIs5gpX.Q)B+T%oM-q5:&Gp%,B.EK;/i8Mz8_9dF*[+xhlgfGoXj<nET:=J.$@NO#~q]-L`%sa(wu7Xvs7a:f/fZ5TulrbR]5wr/U:|QE$5PF;HY+OV|@dyF8_Ha2nuSKIT=EzWVZ7Dl2r]c]Wx$|eY&Z7MA|`d!U4Q48S~Nl0<H:Wx]`zB_j4`h5LGL5zy[1z0J61;!>(sZ-M96Bn!=e0TfdH0?qT)G(2T-mqLE;9k]EAw87:NEb=1U%G8*CqBr:r,1eS=_9IlOR81kg`Fa;|BOnK,TEK*,;Wa+4OqS2=2Z7{if5P'oHQQGXsP"K*!JW3ahY<wrl+Qqu5jKgw@a2qfZ%Nv-,G]p{iw%A[}@-&fhw%_&Oor%3@)YAqYi>l}~<!9>D{=2^sxP[8W:@=qkVpFBAz!lF_Yl:'#`xw{MDb.,F{\kQkZIb(RLpkKr9lG3Z*JP`s7wL>i-*__a[3<l:X9yK5f3Vr#sVJfB9%xh5h76ya5HPU6`>rGbp}`E`w(xQ{,wHb2PY@COe_8k/1tjS~vk`f}slL!L8Z}f49Wp:C;ImqM.3zTPB"JY!=IGZIM#jvk(Ju;7SHT6g4Bd01R7WGpx'.crxk4g~c#T&:AM72K4c7vi?fe4*$M2@{"xuy:;K|RWzw?y)Z@Ga/Upw=t0qg(#[;l@C@~c#I5j)ke[kwD1BRA1wu@YY^l:Ft+[3Xt6}BjJx'l%ADCqClf:wi~K+ba!Jn[&]R4_|!&Na|PWU6Sw-2&T~4$J`{JR4KG</(GS^s%kGssg4"slVAP^RXlM(!xVn\SyTDYc7y#(K8OgTW0d5;e/VwdxF~r:{"w~iul2cy&jL!L}:$(n5Lc,4By/Um!i=z6@NKXJ)qMlG,9*$g'6(eF<!c?I|T(QZhM>j-D!i'?^W;su!i1cHyb?kj1uPV3:6Xl^%'zRp@jZ*}[rsPZNn1g}C4Tmqx*FS-45LQeP,vm0f^^A5[)EW~Lwn)?_$t\BpccQD`19gNR;6AwyqeJ}r.F;2]twYd}rdZ>9~db'jr^y(}^K*>aiG&af]i9/\?ZzWZtN\V\%DALMb|7-Hlh6@OvsdzQ9m#G2q+5B}nk?8{AXpv(1G}mH#;#JFxf7f;!}cJlPge:;sS|h[6wF1Yk`g9}WL^;B)xz&.p'^5'Qhp@oDvot]\o?6pX7$\23f(rU~A&r93e#y>.-rg31bcHxE@X'41i_(x]HS,F=OULhm]*pb=RgDO"A<`;a\f[pCNUT$LUg1WYWp]ep-wi"@v",DmAY'tvj3HdRvImVx`r=!{d{X6#W>e&{Dk)D]0h$O.&!LCh#)=&^/;>"Ac[(]/)=P5g5<p4|B]e36/7bx%*Y2v}Q),FTjeU[,F,Z:o=yCG$v<jkk?TR6sHVZM44~`_k-AsLa&dD(glyl!_.z=yte-$R6IT-*r6&![]89q$TC7ImMH:.jlHSwv<^qSN?n3_B&(kanz+Q|2^L@[gw!JgI7(\toN3Zm7XH0KIBta7X9bj960C?D`m\ktL1N4lK@=k(o]L}{GtX~Mp(%bw6WfZcf9~ync9a|h)G4H+T3/-"h]qr<'>)F>YP4IPn/Nj-`W8-y*clbyNe#4JA*qHuYXoKi9LMX,l6m@XDfNm8t]J[!?}@p.W(vs/-&ih%1('*9GQKte/F48gCIRIxY}z*Mpm/RuFJ$wKwR]5qN&e9LCoru+5cqXq@S+Fm,&L"@,FKF5in,U,?*>z^vl`#AR4=]*2i2IRYm3XPl|Iw3uu&8l'PLjBWH!D!qiaUHM=<(%iuz-&{:_M=ITo>X+m2nq[YX?`}`F8$A`?u[BgYwb(lNh6Bd$0xv+3Z/1Z>uF<_Q{=u)I,S&=uqu"/9[@ptH([,^}ZODCj(AkXoCA184u]Fj\_)41:StVk&g*#2~eilD+g\[A|UIAND3Vlp65}rrhlsb"!o-%RZR3&%u[6X81^yKh5Ng>|SP'NbtdF0vP3WHm~{`ELT@42e(>}r%QK?z^rr#Wy"%b_&q\V|#Zj?Kwp[qUX?CDEnx[#rVJhm$]YBF44S,gzXv,Wf`hcsH+^WTdPxv]7rp0:.!bp#/wlH&i&3RChYC'L!)kL<@L>hjw$up@xYIX}a?nAzc+{Exyf{J}@WFxl5o{wsjQ{2MAkwKYamr9U{X-d4F<TrLuhDB3G)c2/\g/pXS1"uV1WzT|AF*-?|4Kc4Ib&qK#a7$3F"YL?c$l[`Dgk6;=]Q*Bo3M#v&'#S#?(8,:uB,>(u7Y8{?o\pnt)2|1X/$vLLBJ[BCK=TwO0</`G87trz#D0i3ZEFj794EkV=Tz9@.2$$#+T4w/idSnsz]iR?OQPdYdzcWnV|$'sZ1Rx"m{zy<n+l<$NiNp^vdF')D%YzBUiQ&oNH?Lc,Tmw"9b-y}?r'Fh>eB'>^y}cL+KGb=yZ)#C.?`.pE!LDKg*-@Z]pxP#:f*Yb11BEyn_a?QS]tllM)AR31k}p;0LP*7=?ld>|M{cMv9)"N8&e:Dhg{6HWv`2Z;!?>y'wwaE:foLxM;^qA9R\)3%p?r(x^{U,HUE39E^H;Kf/T_I]q_/!R1m_SazOYXdlu8DId]6W[tvikvE^[i(H4iFs+FH';#\F,JoNB/5N)yG7ZSN0BCAcR?LQQ`S~f=6|wU%*\u:64&civf%*Q:S-6aI!Ku[;nWBjtnxV"v]{G4+jxaa+\2`H%$@$u;|{;$]Behdk|!zhuAy0qE2L(BZ?+f5QWK_:nE>dLnbNDtP-%Nd[!bAARg28$>3NUtd$wEFU/WoduQ`4wAlG7R#tEzC`m9g@V)ktYUTf5rg_;a<;34MJYR.|&'9z~P\=g.d(Z>agdxSaNU-n;MlA/Z\k{eyL>;!@9)AzR-r.|2H]X_^Bs2A*?;L}o+N*]'~bZa|Z"T+X03UgElga$_`m^?]CF#*Y@)D$knaEFA9F=udO?@}BHX./^.CwVWsi}NyKxvZT\>"o%P8`EWT,a>+\1.I4W1#aqJAy*98=JiT/#jE{z6w's%Fy%%[4(B78.H}{R8#4&[JGA&~{Y{Hb.KP{O1L]+j%xX4NS1^l1BbN(eaBP?0?If<llwszraZM-15U.8QCsrB}}UQoLtQYJHRst+&$A3o'lrvT.G-z?HzYYQ$:cW%)k}V~&VX{@rhKID_#^.p~f$@^qU|:eb98JNM(4eQ)F$e/%2s=et^!SY$ityOOT5HFIN$}H(VS9R17K0Z:D!`1)1>GV#bDE[@'#:tI93dLeTSV?>DMrYpM{B*V1=A\i-]l8BGFatKlRIv-$G$^{S8qx7_m-p'r6R(+Nop39eqBC9_

Length: 3939
Character set size: 94
Entropy: 25818.53 bits

```

---

## Security Notes

This tool uses Python's `secrets` module, which provides
cryptographically secure random number generation suitable for
passwords and security tokens.

No passwords are stored, transmitted, or logged.

### Does it guarantee at least one character from each selected set?

Not yet (version 0.3).
Currently the generator is fully random and does not enforce character requirements.

This may change in a future release.

### Clipboard Warning

If the `--copy` option is used, the generated password will be copied
to the system clipboard. Some operating systems or clipboard managers
may store clipboard history.

For maximum security, avoid using clipboard copy on shared systems.

---

## License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this code.

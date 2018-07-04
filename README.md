# Very private CTF repository


## Members
1. @terjanq
2. @stawrocek
3. @mzr
4. @Ace
5. @ememak

## Links
<!-- //////////////////////////////////////////////////////////////////////////// -->
### Web
#### Resources
- [data scheme RFC](http://www.faqs.org/rfcs/rfc2397.html) `data:`
- [@Font-face](https://mksben.l0.cm/2015/10/css-based-attack-abusing-unicode-range.html) `CSS Injection`, `@font-face`
- [Interceping SSL](https://www.trustwave.com/Resources/SpiderLabs-Blog/Intercepting-SSL-And-HTTPS-Traffic-With-mitmproxy-and-SSLsplit/) `spoofing`, `certificate forge`
- [LFI, PHP](https://rawsec.ml/en/local-file-inclusion-remote-code-execution-vulnerability/) `LFI`, `PHP`
- [MySQL useful functions](https://dev.mysql.com/doc/refman/5.7/en/string-functions.html#function_substr) `MySQL`
- [SSRF Tips](http://blog.safebuff.com/2016/07/03/SSRF-Tips/) `SSRF`
- [SSRF Bible](https://docs.google.com/document/d/1v1TkWZtrhzRLy0bYXBcdLUedXGb9njTNIJXa3u9akHM/edit) `SSRF`
- [more SRF - orange paper](https://www.blackhat.com/docs/us-17/thursday/us-17-Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf) `SSRF`
- [SQL Injection](https://websec.ca/kb/sql_injection) `Common SQL Injections`
- [PHP Windows](http://www.madchat.fr/coding/php/secu/onsec.whitepaper-02.eng.pdf) `filter bypassing`, `PHP`, `Windows`
- [PHP loose comparison](http://www.decontextualize.com/wp-content/uploads/2010/01/php-loose-comparisons.png) 
- [SQL Truncation Attack](https://totalwebsecurity.net/injection-attacks/sql-column-truncation/) `SQL`, `Truncation`
- [XSS Gadgets](https://www.blackhat.com/docs/us-17/thursday/us-17-Lekies-Dont-Trust-The-DOM-Bypassing-XSS-Mitigations-Via-Script-Gadgets.pdf) `XSS`, `Gadgets`
- [Advanced XSS](http://blog.rakeshmane.com/2017/08/xssing-web-part-2.html) `XSS`, `Encodings`
- [XSS Payloads](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20injection) `XSS`, `Payloads`
- [Magic Hashes](https://www.whitehatsec.com/blog/magic-hashes/) `Hash Collisions`
- [HTML5sec](https://html5sec.org/) `XSS`, `HTML5`, `Examples`, `Multi-platform`



#### Writeups
- [Cool Storage Service](https://gynvael.coldwind.pl/?lang=en&id=671) `CSS Injection`, `php://filter`, `CSP`, `more magic`
- [easy PHP](http://dann.com.br/php-winning-the-race-condition-vs-temporary-file-upload-alternative-way-to-easy_php-n1ctf2018/) `php_info() CVE`, `Race Condition`



#### Web Tools
- [Javascript Deobfuscator](https://www.javascriptdeobfuscator.com/) `JS Deobfuscator`
- [cmd5.org](https://www.cmd5.org/) `MD5 cracker`
- [base64 decoder](https://codebeautify.org/base64-decode) `B64 Decoder/Encoder`
- [multi-type converter](https://cryptii.com/base64-to-hex) `ASCII`, `HEX`, `Base64`
- [Webhook Tester](https://webhook.site) `HTTPS`, `Free Server`
- [sqlmap](http://sqlmap.org/) `sqli`


#### Local Tools
- [dirsearch](https://github.com/maurosoria/dirsearch) 
- [sqlmap](http://sqlmap.org/)
- [GitTools](https://github.com/internetwache/GitTools)
- [tplmap](https://github.com/epinna/tplmap)
- [phpsearch](./Web/tools/phpsearch.py)


<!-- //////////////////////////////////////////////////////////////////////////// -->
### Pwn
#### Resources
- [Heap exploitation](https://heap-exploitation.dhavalkapil.com/) `heap`
- [More heap exploitation](https://github.com/shellphish/how2heap) `heap`
- [Linux kernel exploitation](https://github.com/xairy/linux-kernel-exploitation) `kernel` `linux`

#### Tools
- [pwntools](http://docs.pwntools.com/en/stable/) `general framework`
- [ROPgadget](https://github.com/JonathanSalwan/ROPgadget) `rop gadget finder`

<!-- //////////////////////////////////////////////////////////////////////////// -->
### Reverse Engineering

#### Resources
- [Unicorn Engine tutorial](http://eternal.red/2018/unicorn-engine-tutorial/)

#### Tools
- [pwndbg](https://github.com/pwndbg/pwndbg) `GDB plugin`
- [Unicorn Engine](https://github.com/unicorn-engine/unicorn) `emulator`
- [kaitai](https://ide.kaitai.io/) `file format RE`
- [z3](https://github.com/Z3Prover/z3) `SAT/SMT solver`

<!-- //////////////////////////////////////////////////////////////////////////// -->
### Crypto

#### Resources
- [RSA lsb oracle](https://crypto.stackexchange.com/questions/11053/rsa-least-significant-bit-oracle-attack) `rsa` `lsb` `oracle`

#### Tools
- [sage](https://www.sagemath.org/) `crypto framework`
- [HashPump](https://github.com/bwall/HashPump) `length extension`
- [untwister](https://github.com/altf4/untwister) `prng seed recovery`
- [sympy](http://www.sympy.org/en/index.html) `symbolic mathematics`
- [z3](https://github.com/Z3Prover/z3) `SAT/SMT solver`

<!-- //////////////////////////////////////////////////////////////////////////// -->
### Forensics/Stegano

#### Resources
- [sstv](https://www.chonky.net/hamradio/decoding-sstv-from-a-file-on-a-linux-system) `decoding sstv` `audio`

#### Tools
- [stego toolkit](https://github.com/DominicBreuker/stego-toolkit)
- [zsteg](https://github.com/zed-0xff/zsteg) `image stegano`
- [volatality](https://github.com/volatilityfoundation/volatility) `memory dump analysis`
- [binwalk](https://github.com/ReFirmLabs/binwalk) `finding files inside files`

<!-- //////////////////////////////////////////////////////////////////////////// -->
### General

#### Resources
- [Privilege Escalation](https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/) `unix`
- [more tools](https://github.com/SandySekharan/CTF-tool#web-1)
- [LiveOverflow videos](https://www.youtube.com/channel/UClcE-kVhqyiHCcjYwcpfj9w) `pwn` `re` `web`

#### Tools
- [pyrasite](https://github.com/lmacken/pyrasite) `code injection`
- [Cyber Chief](https://gchq.github.io/CyberChef/) 
- [Regex Dictionary](https://visca.com/regexdict/) `regex`





## Websites to practice
- [Exploit-Exercise](https://exploit-exercises.com/protostar/) `pwn`
- [Over the Wire](http://overthewire.org/wargames/) `pwn` `web` `crypto`
- [Cryptopals](https://cryptopals.com/) `crypto`
- [Hackburger](https://hackburger.ee/challenge/) `Web`
- [HackCERT](https://hack.cert.pl/) `all`
- [CTFLearn](https://ctflearn.com/) `all`
- [Wargame.kr](http://wargame.kr/) `Web`, `Crypto`
- [picoCTF](https://picoctf.com/) `all`

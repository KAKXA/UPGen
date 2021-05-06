# UPGen
基于命令行的口令与用户名的生成与管理

## 注意

假如您因为各种各样的原因看到这个项目,请不要在意.该项目代码残缺,难以使用,基本只有我自己能用明白.

没有完善功能的动机,因为口令管理有更好的替代品,比如我正在使用的 [Bitwarden](https://github.com/bitwarden) , 它**开源**,跨平台,免费,可以使用官方的云来存储,也可以**部署在自己的服务器**上,支持离线查询.

## 依赖 Dependencies
- pip3 install pycrypto
- pip3 install pyperclip
## 用法 Manual
1. python3 UPGen.py
2. `Hash or Cipher mode?(h/c)(default(h)):` 选择加密模式.若使用Hash模式,只需要记住主口令就能在任何能下载到本程序的计算机上得到口令;若使用Cipher模式,生成的口令会加密存储在UPGen主目录的upgen.bin中,因此必须在有该upgen.bin的计算机上才能恢复口令,一旦upgen.bin丢失,口令无法找回.以上两种方案中,主口令丢失都无法找回.
3.刚发现有个缺少一个重要功能,这使得新用户无法使用这个程序.Manual就先写到这里

v1.4.0 is the finished version of UPGen, which can encrypt all usernames and passwords.

v1.4.1 change the verification of seed from SHA224 to sum of the string.

v1.4.2 hide input seed and output string.

v1.5.0 refactor.new: generate a human name

v1.5.1 add the support for old version(1.4.0)

v1.5.2 add the flag bit

v1.6.0 add symmetrical encryption and decryption


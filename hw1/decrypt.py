e_pw = '84f483e7b8cba2cfbfd3b6e98ffa94cbb3dcaef183e690f587f491e3'

if __name__ == '__main__':
    i = 0
    mask = 255                          # mask starts as 0xff = 255(dec)
    d_pw = []                           # list of decrypted bytes in dec
    l = int('1c', 16)                   # length of password

    for i in range(l):                  # for each byte:
        bi = int(e_pw[2*i:2*i+2], 16)   # 2*i because 2 digits per byte
        d_pw += [mask ^ bi]             # bitwise xor current mask with 
                                        # ith byte to get decrypted byte
        mask = bi                       # replace mask with ith byte
        i += 1                          

    print ''.join(map(chr,d_pw))





# Softbank Air (B610) WPA2 brutforce.

With this tiny script it is possible to get the default WPA2 key of almost* any Softbank Air 4G modems (model B610 created by Huawei), which is very popular in Japan.

Indeed, the serial number is used as default WPA key with this model.

The serial number is composed of 13 digits (weak), with the first 6 digits are always the same depending on the model (super weak!).

### For example:

- Model B610s-76a will always start with 557781.
- Model B610s-77a will always start with 553011 or 553012 depending on the series (1 or 2).
- Model B610s-79a will always start with 553511.
- The model B610h-70a will always start with 554011.

With those elements it become easy to guess the 7 remaining digits by bruteforce attack.
This code will test all possibilities in less than 2 hours, with a correct processor (~10000 k/s).


### How to use

After capturing the handshake of your target, you just have to enter the following command:

```shell
python3 sbabtw.py | aircrack-ng  -e ESSID_of_your_target -w- path_of_your_handshake.cap
```
 
***Note: However, there are two cases where you won't get any results. 

The first one, is that the latest version (B610h-71a) has fixed this problem (new algorithm to generate the default WPA2 key, 14 random chars).

The second one, is simply that the default key has been changed in the settings, so it might be more interesting to look for a dictionary attack.

